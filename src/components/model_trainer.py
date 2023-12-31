import os
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from dataclasses import dataclass
import yaml
from src.utils import save_obj
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC


@dataclass
class ModelTrainerConfig:
    model_trainer_filepath = os.path.join('artifacts\model_trainer','model.pkl')

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()
    def initiate_model_trainer(self, train_arr, test_arr):
        x_train, y_train, x_test, y_test = (train_arr[:,:-1], train_arr[:,-1],test_arr[:,:-1],test_arr[:,-1])

        params = yaml.safe_load(open('params.yaml'))
        parameter = params['LogisticReg']

        model = LogisticRegression()
        model.set_params(**parameter)
        model.fit(x_train, y_train)

        save_obj(self.model_trainer_config.model_trainer_filepath,model)

        return (x_train, y_train, x_test, y_test,model,parameter)