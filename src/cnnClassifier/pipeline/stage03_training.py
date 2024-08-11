from src.cnnClassifier.config.configuration import ConfigurationManager
from src.cnnClassifier.components.training import Training
from src.cnnClassifier import logger

STAGE_NAME="Training model "

class TrainModelPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        training_config = config.get_training_config()
        training = Training(config=training_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train()

if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = Training()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e