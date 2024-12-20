from cnnClassifier.components.eval_mlflow import Evaluation
from cnnClassifier import logger
from cnnClassifier.config.config_entity import ConfigurationManager


STAGE_NAME="Model evaluation "

class EvaluateModelPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        eval_config = config.get_evaluation_config()
        evaluation = Evaluation(eval_config)
        evaluation.evaluation()
        evaluation.log_into_mlflow()

if __name__ == '__main__':
    try:
        logger.info(f"\n>>>>>> Model evaluation started <<<<<<\n")
        obj = EvaluateModelPipeline()
        obj.main()
        logger.info(f"\n>>>>>> Model evaluation completed <<<<<<\n")
    except Exception as e:
        logger.exception(e)
        raise e
