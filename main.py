from src.cnnClassifier import logger
from src.cnnClassifier.pipeline.stage01_ingestion import DataIngestionPipeline

STAGE_NAME="Data Ingestion"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataIngestionPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e