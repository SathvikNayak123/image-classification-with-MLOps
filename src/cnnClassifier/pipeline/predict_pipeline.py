import numpy as np
import tensorflow as tf
from pathlib import Path
from PIL import Image
from cnnClassifier.config.config_entity import TrainingConfig

class Prediction:
    def __init__(self):
        self.model = self.load_model('artifacts/training/model.h5')
        self.label_map= {0: "adenocarcinoma", 1: "large.cell.carcinoma", 2: "normal", 3: "squamous.cell.carcinoma"}

    @staticmethod
    def load_model(model_path: Path) -> tf.keras.Model:
        """Load the pre-trained Keras model."""
        return tf.keras.models.load_model(model_path)

    def preprocess_input(self, image: tf.Tensor) -> tf.Tensor:
        """Preprocess the input image for prediction."""
        image = Image.fromarray(image).convert("RGB")
        image = np.array(image)

        image = tf.image.resize(image, (224, 224))
        image = image / 255.0 
        return tf.expand_dims(image, axis=0)

    def predict(self, image: tf.Tensor) -> np.ndarray:
        """Generate predictions for a given input image."""
        processed_image = self.preprocess_input(image)
        predictions = self.model.predict(processed_image)
        return predictions

    def predict_class(self, image: tf.Tensor) -> int:
        """Predict the class label for a given input image."""
        predictions = self.predict(image)
        predicted_class = np.argmax(predictions, axis=1)[0]
        predicted_label = self.label_map.get(predicted_class, "Unknown")
        return predicted_label
