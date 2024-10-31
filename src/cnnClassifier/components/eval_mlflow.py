import tensorflow as tf
from tensorflow.keras.utils import to_categorical
from pathlib import Path
from cnnClassifier.config.artifact_entity import EvaluationConfig
from cnnClassifier.utils.common import save_json
import mlflow
import mlflow.keras
from mlflow.models.signature import infer_signature
from urllib.parse import urlparse
import dagshub

class Evaluation:
    def __init__(self, config: EvaluationConfig):
        self.config = config

    def _load_valid_dataset(self):
        # Load the dataset using tf.keras.utils.image_dataset_from_directory
        self.valid_dataset = tf.keras.preprocessing.image_dataset_from_directory(
            self.config.training_data,
            validation_split=0.30,
            subset="validation",
            seed=123,
            image_size=self.config.params_image_size[:-1],
            batch_size=self.config.params_batch_size
        )

        self.valid_dataset = self.valid_dataset.map(
            lambda x, y: (x, to_categorical(y, num_classes=self.config.params_classes))
        )
        # Normalize the images
        normalization_layer = tf.keras.layers.Rescaling(1./255)
        self.valid_dataset = self.valid_dataset.map(lambda x, y: (normalization_layer(x), y))

    @staticmethod
    def load_model(path: Path) -> tf.keras.Model:
        return tf.keras.models.load_model(path)

    def evaluation(self):
        self.model = self.load_model(self.config.path_of_model)
        self._load_valid_dataset()  # Use the new method for validation data
        self.score = self.model.evaluate(self.valid_dataset)
        self.save_score()

    def save_score(self):
        scores = {"loss": self.score[0], "accuracy": self.score[1]}
        save_json(path=Path("scores.json"), data=scores)

    def log_into_mlflow(self):
        mlflow.set_registry_uri(self.config.mlflow_uri)
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme

        dagshub.init(repo_owner='SathvikNayak123', repo_name='cancer-dl', mlflow=True)

        # Define an example input for the model signature
        example_input,_ = next(iter(self.valid_dataset))
        example_output = self.model.predict(example_input)
        signature = infer_signature(example_input.numpy(), example_output)

        with mlflow.start_run():
            mlflow.log_params(self.config.all_params)
            mlflow.log_metrics(
                {"loss": self.score[0], "accuracy": self.score[1]}
            )
            # Model registry does not work with file store
            if tracking_url_type_store != "file":
                # Register the model
                mlflow.keras.log_model(self.model,
                                    "model",
                                    signature=signature,
                                    registered_model_name="VGG16Model")
            else:
                mlflow.keras.log_model(self.model, "model")
