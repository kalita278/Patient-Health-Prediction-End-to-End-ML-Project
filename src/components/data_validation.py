import os
import pandas as pd
import numpy as np
from dataclasses import dataclass
import yaml

@dataclass
class DataValidationConfig:
    train_data_validation_path = os.path.join('artifacts\data_validation','train_data_validation.txt')
    test_data_validation_path = os.path.join('artifacts\data_validation','test_data_validation.txt')
class DataValidation:
    def __init__(self):
        self.data_validation_config = DataValidationConfig()

    def initiate_data_validation(self,train_data,test_data):

        train_df = pd.read_csv(train_data)
        test_df = pd.read_csv(test_data)

        train_data_cols = list(train_df.columns)
        test_data_cols = list(test_df.columns)

        schema = yaml.safe_load(open('schema.yaml'))
        keys = schema.keys()

        train_validation_status = []
        test_validation_status = []
        os.makedirs(os.path.dirname(self.data_validation_config.train_data_validation_path),exist_ok=True)

        for col in train_data_cols:
            if (col in keys) and (str(train_df[col].dtypes) in schema[col]):
                status = True
                train_validation_status.append(status)
            else:
                status = False
                train_validation_status.append(status)
        if False in train_validation_status:
            train_data_validation_status = False
            with open(self.data_validation_config.train_data_validation_path,'w') as f:
                f.write(f"train_data_validation_status: {train_data_validation_status}")
        else:
            train_data_validation_status = True
            with open(self.data_validation_config.train_data_validation_path,'w') as f:
                f.write(f"train_data_validation_status: {train_data_validation_status}")
            
        for col in test_data_cols:
            if (col in keys) and (str(test_df[col].dtypes) in schema[col]):
                status = True
                test_validation_status.append(status)
            else:
                status = False
                test_validation_status.append(status)
        if False in test_validation_status:
            test_data_validation_status = False
            with open(self.data_validation_config.test_data_validation_path,'w') as f:
                f.write(f"test_data_validation_status: {test_data_validation_status}")
        else:
            test_data_validation_status = True
            with open(self.data_validation_config.test_data_validation_path,'w') as f:
                f.write(f"test_data_validation_status: {test_data_validation_status}")
        
        return (self.data_validation_config.train_data_validation_path,
        self.data_validation_config.test_data_validation_path)

