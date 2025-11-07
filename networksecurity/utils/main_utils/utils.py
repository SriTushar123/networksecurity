import pandas as pd
import numpy as np
from networksecurity.exception.exception import NetworkSecurityException
import yaml
import sys,os
import pickle as pkl

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