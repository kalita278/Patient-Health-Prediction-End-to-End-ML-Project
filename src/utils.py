import os
import pickle
import numpy as np
from sklearn.metrics import roc_auc_score, accuracy_score, precision_score, recall_score, f1_score
import json

def save_obj(file_path,obj):
    dir_name = os.path.dirname(file_path)
    os.makedirs(dir_name,exist_ok=True)
    with open(file_path, 'wb') as file__obj:
        pickle.dump(obj,file__obj)

def save_json(file_path,obj):
    dir_name = os.path.dirname(file_path)
    os.makedirs(dir_name,exist_ok=True)
    with open(file_path, 'w') as file__obj:
        json.dump(obj,file__obj)


def outlier_treatment(data):
    for col, j in zip(data.columns[0:6], np.arange(6)):
        q1 = data[col].quantile(0.25)
        q3 = data[col].quantile(0.75)
        iqr = q3-q1
        upper_fence = q3 + 1.5*iqr
        lower_fence = q1 -1.5*iqr
        df_include = data.loc[(data[col] >= lower_fence) & (data[col] <= upper_fence)]
        mean = df_include[col].mean()
        data[col]=np.where(data[col]>upper_fence,mean,data[col])
        data[col]=np.where(data[col] < lower_fence, mean,data[col])

    return data

def evaluate_metrix(x, y, model):


    y_proba = model.predict_proba(x)
    y_pred = model.predict(x)

    roc_auc_scr = round(roc_auc_score(y, y_proba,multi_class='ovr'),4)
    accuracy = round(accuracy_score(y, y_pred),4)
    precision = round(precision_score(y, y_pred,average='weighted' ),4)
    recall = round(recall_score(y, y_pred, average='weighted'),4)
    f1 =  round(f1_score(y, y_pred,average='weighted'),4)

    return roc_auc_scr, accuracy, precision, recall, f1