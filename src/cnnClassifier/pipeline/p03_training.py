from cnnClassifier.config.config_entity import ConfigurationManager
from cnnClassifier.components.training import Training
from cnnClassifier import logger

class TrainModelPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        training_config = config.get_training_config()
        training = Training(config=training_config)
        training.get_base_model()
        #training.train_valid_generator()
        training.train()

if __name__ == '__main__':
    try:
        logger.info(f"\n>>>>>> Training model started <<<<<<\n")
        obj = TrainModelPipeline()
        obj.main()
        logger.info(f"\n>>>>>> Training model completed <<<<<<\n")
    except Exception as e:
        logger.exception(e)
        raise e