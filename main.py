from src.cnnClassifier.pipeline.training_pipeline import TrainingPipeline
from src.cnnClassifier import logger


if __name__ == '__main__':
    train = TrainingPipeline()
    try:
        logger.info(f"\n>>>>>> Data Ingestion started <<<<<<\n")
        train.DataIngestionPipeline()
        logger.info(f"\n>>>>>> Data Ingestion completed <<<<<<\n")

        logger.info(f"\n>>>>>> Preparing base model started <<<<<<\n")
        train.Model_Prep()
        logger.info(f"\n>>>>>> Preparing base model completed <<<<<<\n")

        logger.info(f"\n>>>>>> Training model started <<<<<<\n")
        train.TrainTopLayers()
        logger.info(f"\n>>>>>> Training model completed <<<<<<\n")

        logger.info(f"\n>>>>>> Model evaluation started <<<<<<\n")
        train.MLFlow_Eval()
        logger.info(f"\n>>>>>> Model evaluation completed <<<<<<\n")
    except Exception as e:
        logger.exception(e)
        raise e