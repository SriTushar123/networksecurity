import os
import pandas as pd
import sys
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.entity.config_entity import ModelTrainerConfig
from networksecurity.entity.artifact_entity import DataTransformationArtifacts
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import (
    RandomForestClassifier,
    AdaBoostClassifier,
    GradientBoostingClassifier
)
from sklearn.tree import DecisionTreeClassifier
from networksecurity.utils.main_utils.utils import evaluate_models

class ModelTrainer:
    def __init__(self,data_transformation_artifact:DataTransformationArtifacts,model_trainer_config:ModelTrainerConfig):
        try:
            self.data_transformation_artifact=data_transformation_artifact
            self.model_trainer_config=model_trainer_config
        except Exception as e:
            raise NetworkSecurityException
        
    def train_model(self,X_train,y_train,X_test,y_test):
        models={
            "Decision Tree":DecisionTreeClassifier(),
            "AdaBoost":AdaBoostClassifier(),
            "Random Forest":RandomForestClassifier(verbose=1),
            "Gradient Boosting":GradientBoostingClassifier(verbose=1),
            "Logistic Regression":LogisticRegression(verbose=1)
        }
        params={
        "Decision Tree": {
            'criterion':['gini', 'entropy', 'log_loss'],
            # 'splitter':['best','random'],
            # 'max_features':['sqrt','log2'],
        },
        "Random Forest":{
            # 'criterion':['gini', 'entropy', 'log_loss'],
            
            # 'max_features':['sqrt','log2',None],
            'n_estimators': [8,16,32,128,256]
        },
        "Gradient Boosting":{
            # 'loss':['log_loss', 'exponential'],
            'learning_rate':[.1,.01,.05,.001],
            'subsample':[0.6,0.7,0.75,0.85,0.9],
            # 'criterion':['squared_error', 'friedman_mse'],
            # 'max_features':['auto','sqrt','log2'],
            'n_estimators': [8,16,32,64,128,256]
        },
        "Logistic Regression":{},
        "AdaBoost":{
            'learning_rate':[.1,.01,.001],
            'n_estimators': [8,16,32,64,128,256]
        }
        }

        report=evaluate_models(X_train=X_train,X_test=X_test,y_test=y_test,y_train=y_train,model=models,params=params)
        sorted_report=dict(sorted(report.items(),key=lambda x:x[1],reverse=True))
        best_model,best_model_score=list(sorted_report.items())[0]

        model=models[best_model]
        model.fit(X_train,y_train)
        y_pred=model.predict(X_test)
        

