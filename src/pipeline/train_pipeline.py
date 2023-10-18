from src.components.data_injestion import DataInjestion
from src.components.data_validation import DataValidation
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer
from src.components.model_evaluation import ModelEvaluation


class TrainingPipeline:
    def __init__(self):

        self.data_injestion = DataInjestion()
        self.data_validation = DataValidation()
        self.data_transformation = DataTransformation()
        self.model_trainer = ModelTrainer()
        self.model_evaluation = ModelEvaluation()
    
    def train(self):
        train_data, test_data = self.data_injestion.initiate_data_injestion()
        self.data_validation.initiate_data_validation(train_data, test_data)
        train_arr,test_arr = self.data_transformation.initiate_data_transformation(train_data, test_data)
        x_train, y_train, x_test, y_test,model,parameter = self.model_trainer.initiate_model_trainer(train_arr, test_arr)
        self.model_evaluation.initiate_model_evaluation(x_train, y_train, x_test, y_test,model,parameter)
