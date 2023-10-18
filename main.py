from src.pipeline.train_pipeline import TrainingPipeline


def train():

    train_pipeline = TrainingPipeline()

    train_pipeline.train()
if __name__=='__main__':
    train()