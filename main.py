from cnnClassifier.pipeline.stage03_training import TrainModelPipeline
from src.cnnClassifier import logger
from src.cnnClassifier.pipeline.stage01_ingestion import DataIngestionPipeline
from src.cnnClassifier.pipeline.stage02_prepare_base_model import BaseModelPipeline

STAGE_NAME="Data Ingestion"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataIngestionPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME="Preparing base model"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = BaseModelPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME="Training model"
if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = TrainModelPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e