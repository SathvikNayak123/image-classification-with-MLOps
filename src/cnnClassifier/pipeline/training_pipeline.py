from cnnClassifier.config.config_entity import ConfigurationManager
from cnnClassifier.components.data_ingestion import DataIngestion
from cnnClassifier.components.prepare_base_model import PrepareBaseModel
from cnnClassifier.components.training import Training
from cnnClassifier.components.eval_mlflow import Evaluation
from cnnClassifier import logger
import os
from dotenv import load_dotenv

load_dotenv()

class TrainingPipeline:

    def __init__(self):
        self.config = ConfigurationManager()

    def DataIngestionPipeline(self):
        data_ingestion_config = self.config.get_data_ingestion_config()
        data_ingestion = DataIngestion(os.getenv("mongoURI"),
                                    os.getenv("fileID"),
                                    config=data_ingestion_config)
        data_ingestion.download_file_from_mongo()
        data_ingestion.extract_zip_file()
    
    def Model_Prep(self):
        prepare_base_model_config = self.config.get_prepare_base_model_config()
        prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model()
    
    def TrainTopLayers(self):
        training_config = self.config.get_training_config()
        training = Training(config=training_config)
        training.get_base_model()
        training.train()

    def MLFlow_Eval(self):
        eval_config = self.config.get_evaluation_config()
        evaluation = Evaluation(eval_config)
        evaluation.evaluation()
        evaluation.log_into_mlflow()