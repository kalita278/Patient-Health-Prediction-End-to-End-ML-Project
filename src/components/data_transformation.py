import os
import pandas as pd
from dataclasses import dataclass
from src.utils import save_obj, outlier_treatment
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
import numpy as np


@dataclass
class DataTransformationCofig:
    data_tranformation_path = os.path.join('artifacts\data_transformation','preprocessor.pkl')

class DataTransformation:
    def __init__(self):
        self.data_tranformation_config = DataTransformationCofig()
    
    def get_transform_data(self):


        num_cols = ['P_incidence','P_tilt','L_angle','S_slope','P_radius','S_Degree']

        preprocessor = Pipeline([('Impute',SimpleImputer(strategy ='mean')),('scaling',StandardScaler(with_mean=False))])

        return preprocessor
    
    def initiate_data_transformation(self, train_path,test_path):

        train_data = pd.read_csv(train_path)
        test_data = pd.read_csv(test_path)
        train_data = outlier_treatment(train_data)
        test_data = outlier_treatment(test_data)

        preprocessing_obj = self.get_transform_data()

        input_feature_train = train_data.drop("Class",axis=1)
        target_feature_train = train_data['Class']

        input_feature_test = test_data.drop('Class',axis=1)
        target_feature_test = test_data['Class']

        input_feature_train_arr = preprocessing_obj.fit_transform(input_feature_train)
        input_feature_test_arr = preprocessing_obj.fit_transform(input_feature_test)

        train_arr = np.c_[input_feature_train_arr,np.array(target_feature_train)]
        test_arr = np.c_[input_feature_test_arr,np.array(target_feature_test)]


        save_obj(self.data_tranformation_config.data_tranformation_path,preprocessing_obj)

        return (train_arr,test_arr)

