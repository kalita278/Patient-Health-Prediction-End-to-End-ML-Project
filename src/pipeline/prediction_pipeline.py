import pickle


class PredictionPipeline:
    def __init__(self):

        self.model = pickle.load(open('artifacts\model_trainer\model.pkl','rb'))
        self.preprocessor = pickle.load(open('artifacts\data_transformation\preprocessor.pkl','rb'))

    def predict(self,data):

        data = self.preprocessor.transform(data)
        prediction = self.model.predict(data)

        return prediction

