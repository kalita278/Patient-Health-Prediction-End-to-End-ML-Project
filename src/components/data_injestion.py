import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
import pymysql
from src.components.data_validation import DataValidation
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer
from src.components.model_evaluation import ModelEvaluation

@dataclass
class DataInjestionConfig:
    train_data_path = os.path.join('artifacts\data_injestion', "train.csv")
    test_data_path = os.path.join('artifacts\data_injestion', "test.csv")
    row_data_path = os.path.join('artifacts\data_injestion', "row.csv")

class DataInjestion:
    def __init__(self):
        self.injestion_config = DataInjestionConfig()

    def  initiate_data_injestion(self):

        a = pymysql.connect(user='root',host='127.0.0.1',passwd='mrinal',db='patient_condition')
        df1 = pd.read_sql_query('select * from normal',a)
        df2 = pd.read_sql_query('select * from type_h',a)
        df3 = pd.read_sql_query('select * from type_s',a)

        df1['Class']=df1['Class'].replace('Nrmal','Normal')
        df2['Class']=df2['Class'].replace('type_h','Type_H')
        df3['Class']=df3['Class'].replace('tp_s','Type_S')

        df = pd.concat([df1,df2,df3])

        os.makedirs(os.path.dirname(self.injestion_config.row_data_path),exist_ok=True)
        df.to_csv(self.injestion_config.row_data_path,index=False,header=True)

        train_set,test_set = train_test_split(df,test_size=0.2,random_state=22)

        train_set.to_csv(self.injestion_config.train_data_path,index=False,header=True)
        test_set.to_csv(self.injestion_config.test_data_path,index=False,header=True)

        return(self.injestion_config.train_data_path,
                self.injestion_config.test_data_path)

#if __name__ == '__main__':
 #   obj = DataInjestion()
  #  train_data, test_data = obj.initiate_data_injestion()
   ##data_validation.initiate_data_validation(train_data, test_data)
    #transform_obj = DataTransformation()
    #train_arr,test_arr = transform_obj.initiate_data_transformation(train_data, test_data)
    #model_trainer = ModelTrainer()
    #x_train, y_train, x_test, y_test,model,parameter = model_trainer.initiate_model_trainer(train_arr, test_arr)
    #eval = ModelEvaluation()
    #eval.initiate_model_evaluation(x_train, y_train, x_test, y_test,model,parameter)
