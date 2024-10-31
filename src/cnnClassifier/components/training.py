import os
import tensorflow as tf
from tensorflow.keras import layers
from tensorflow.keras.utils import to_categorical
from cnnClassifier.config.config_entity import TrainingConfig
from pathlib import Path


class Training:
    def __init__(self, config: TrainingConfig):
        self.config = config

        self.augmentation_layers = tf.keras.Sequential([
            layers.RandomFlip("horizontal"),
            layers.RandomRotation(0.05),
            layers.RandomZoom(0.1)
        ])

    def get_base_model(self):
        self.model = tf.keras.models.load_model(self.config.updated_base_model_path)

    def data_augmentation(self, x):
        x = self.augmentation_layers(x)
        return x

    def load_datasets(self):
        # Load datasets from the directory
        self.train_dataset = tf.keras.preprocessing.image_dataset_from_directory(
            self.config.training_data,
            validation_split=0.2,
            subset="training",
            seed=123,  # Set seed for reproducibility
            image_size=self.config.params_image_size[:-1],  # Resize images
            batch_size=self.config.params_batch_size
        )

        self.valid_dataset = tf.keras.preprocessing.image_dataset_from_directory(
            self.config.training_data,
            validation_split=0.2,
            subset="validation",
            seed=123,  # Set seed for reproducibility
            image_size=self.config.params_image_size[:-1],  # Resize images
            batch_size=self.config.params_batch_size
        )

        if self.config.params_is_augmentation:
            self.train_dataset = self.train_dataset.map(
                lambda x, y: (self.data_augmentation(x), to_categorical(y, num_classes=self.config.params_classes))
            )
        else:
            self.train_dataset = self.train_dataset.map(
                lambda x, y: (x, to_categorical(y, num_classes=self.config.params_classes))
            )

        self.valid_dataset = self.valid_dataset.map(
            lambda x, y: (x, to_categorical(y, num_classes=self.config.params_classes))
        )

        # Normalize pixel values to [0, 1]
        normalization_layer = tf.keras.layers.Rescaling(1./255)
        self.train_dataset = self.train_dataset.map(lambda x, y: (normalization_layer(x), y))
        self.valid_dataset = self.valid_dataset.map(lambda x, y: (normalization_layer(x), y))

    @staticmethod
    def save_model(path: Path, model: tf.keras.Model):
        model.save(path)

    def train(self):
        self.load_datasets()  # Load datasets instead of using generators

        self.steps_per_epoch = tf.data.experimental.cardinality(self.train_dataset).numpy()
        self.validation_steps = tf.data.experimental.cardinality(self.valid_dataset).numpy()

        # Use repeat() if necessary i.e dataset is not large enough
        self.train_dataset = self.train_dataset.repeat()
        self.valid_dataset = self.valid_dataset.repeat()


        self.model.compile(
            optimizer=tf.keras.optimizers.Adam(learning_rate=self.config.params_learning_rate),
            loss=tf.keras.losses.CategoricalCrossentropy(),
            metrics=["accuracy"]
        )

        self.model.fit(
            self.train_dataset,
            epochs=self.config.params_epochs,
            steps_per_epoch=self.steps_per_epoch,
            validation_steps=self.validation_steps,
            validation_data=self.valid_dataset
        )

        self.save_model(path=self.config.trained_model_path, model=self.model)
