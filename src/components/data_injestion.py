import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from dataclasses import dataclasses

@dataclass
class DataInjestionConfig:
    train_data_path = os.path.join('artifacts\data_injestion', "train.csv")
    test_data_path = os.path.join('artifacts\data_injestion', "test.csv")
    row_data_path = os.path.join('artifacts\data_injestion', "row.csv")

class DataInjestion:
    def __init__(self):
        self.injestion_config = DataInjestionConfig()

    def  initiate_data_injestion(self):
        df1 = pd.read_csv('Data\Normal.csv')
        df2 = pd.read_csv('Data\Type_H.csv')
        df3 = pd.read_csv('Data\Type_S.csv')

        df1['Class']=df1['Class'].replace('Nrmal','Normal')
        df2['Class']=df2['Class'].replace('type_h','Type_H')
        df3['Class']=df3['Class'].replace('tp_s','Type_S')

        df = pd.concat([df1,df2,df3])

        os.mkdir(os.path.dirname(self.injestion_config.row_data_path),exist_ok=True)
        df.to_csv(self.injestion_config.row_data_path,index=False,header=True)

        train_set,test_set = train_test_split(df,test_size=0.2,random_state=22)

        train_set.to_csv(self.injestion_config.train_data_path,index=False,header=True)
        test_set.to_csv(self.injestion_config.test_data_path,index=False,header=True)

        return(self.injestion_config.train_data_path,
                self.injestion_config.test_data_path)
