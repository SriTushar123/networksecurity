import pandas as pd
import numpy as np
from networksecurity.exception.exception import NetworkSecurityException
import yaml
import sys,os
import pickle as pkl
from sklearn.model_selection import RandomizedSearchCV
from sklearn.metrics import r2_score

def read_yaml(file_path):
    try:
        with open(file_path,"rb") as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise NetworkSecurityException(e,sys)

def write_yaml_file(file_path: str, content: object, replace: bool = False) -> None:
    try:
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w") as file:
            yaml.dump(content, file)
    except Exception as e:
        raise NetworkSecurityException(e, sys)

def save_object(file_path,file_obj):
    try:
        dir_name=os.path.dirname(file_path)
        os.makedirs(dir_name,exist_ok=True)
        with open(file_path,"wb") as obj:
            pkl.dump(file_obj,obj)
    except Exception as e:
        raise NetworkSecurityException(e, sys)

def save_np_array(file_path,array):
    try:
        dir_name=os.path.dirname(file_path)
        os.makedirs(dir_name,exist_ok=True)
        with open(file_path,"wb") as obj:
            np.save(obj,array)
    except Exception as e:
        raise NetworkSecurityException(e, sys)

def evaluate_models(X_train,X_test,y_train,y_test,model,params):
    report=dict()
    for key,val in model.items():
        para=params[key]
        mod=val
        rs=RandomizedSearchCV(estimator=mod,param_distributions=para)
        rs.fit(X_train,y_train)
        mod.set_params(**rs.best_params_)
        mod.fit(X_train,y_train)
        y_pred=mod.predict(X_test)
        score=r2_score(y_test,y_pred)
        rep={key:score}
        report.update(rep)
    return report


        

