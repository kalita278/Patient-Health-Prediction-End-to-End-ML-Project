import os
from dataclasses import dataclass
from src.utils import save_json, evaluate_metrix
import mlflow
from urllib.parse import urlparse

@dataclass
class ModelEvaluationConfig:
    model_evaluation_filepath = os.path.join('artifacts\model_evaluation','model_evaluation.json')

class ModelEvaluation:
    def __init__(self):
        self.model_evaluation_config = ModelEvaluationConfig()
    def initiate_model_evaluation(self, x_train, y_train, x_test, y_test, model, parameter):


        roc_auc_scr_train, accuracy_train, precision_train, recall_train, f1_train = evaluate_metrix(x_train, y_train, model)
        roc_auc_scr_test, accuracy_test, precision_test, recall_test, f1_test = evaluate_metrix(x_test, y_test, model)

        scores = {"Training Accuracy of the Model {}".format(model):
            {
            'roc_auc': roc_auc_scr_train,
            'accuracy': accuracy_train,
            'precision': precision_train,
            'recall': recall_train,
            'f1': f1_train
            },
            "Testing Accuracy of the Model {}".format(model):
            {
            'roc_auc': roc_auc_scr_test,
            'accuracy': accuracy_test,
            'precision': precision_test,
            'recall': recall_test,
            'f1': f1_test
            }
        }

        save_json(self.model_evaluation_config.model_evaluation_filepath, scores)

        

        mlflow.set_tracking_uri("https://dagshub.com/kalita278/Patient-Health-Prediction-End-to-End-ML-Project.mlflow")
        os.environ['MLFLOW_TRACKING_USERNAME'] = "kalita278"
        os.environ['MLFLOW_TRACKING_PASSWORD'] = "eb766988711ad6134d253dc8b82c079114a8a36c"


        with mlflow.start_run():

            mlflow.log_params(parameter)

            mlflow.log_metric("accuracy", accuracy_test)
            mlflow.log_metric("precision", precision_test)
            mlflow.log_metric("recall", recall_test)
            mlflow.log_metric('f1', f1_test)
            mlflow.log_metric("roc_auc_score", roc_auc_scr_test)

            tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme

            if tracking_url_type_store !="file":
                mlflow.sklearn.log_model(model, "model", registered_model_name="{}".format(model))
            else:
                mlflow.sklearn.log_model(model, "model")
                
        return scores

        
