# cancer-dl

# Chest Cancer Detection Using Deep Learning with MLOps

This project focuses on detecting chest cancer from medical images using deep learning techniques. It integrates MLOps practices for robust and reproducible model development, deployment, and monitoring.

## Project Overview

- **Data Source**: Chest cancer images from Kaggle.
- **Model**: VGG16 with a transfer learning approach.
- **Processes**:
  - **Data Ingestion**: Automated data ingestion pipeline.
  - **Training**: Initial training of a base model and modification of the model for improved performance.
  - **Evaluation**: Rigorous evaluation of model performance using various metrics.
  - **Prediction**: Generation of predictions using the trained model.

## MLOps Tools and Techniques

- **MLflow**: Used for tracking experiments and hyperparameter tuning.
  ![Hyperparameter Tuning with MLflow](static/mlflow.png)

- **DAGsHub**: Visualized data pipeline for streamlined data processing and management.
  ![Data Pipeline Display with DAGsHub](static/workflow.png)

- **DVC (Data Version Control)**: Implemented for data versioning to ensure reproducibility.

- **Flask Application**: Built a web app to provide an interface for users to upload images and receive predictions.
  ![Flask App Interface](static/flask.png)

- **Docker**: Dockerized the application for consistent deployment across environments.

- **GitHub Actions**: Implemented CI/CD pipelines for continuous integration and deployment.

- **AWS**: Deployed the application on AWS for scalable access.

## Getting Started

To get started with this project, follow these steps:

1. Clone the repository:  
   ```bash
   git clone https://github.com/SathvikNayak123/cancer-dl.git
   ```
2. Install the necessary dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Initialized DVC:
    ```bash
    dvc init
    ```
4. Run app
    ```bash
    python app.py
    ```

## Deployment

The model and application are deployed on AWS, ensuring scalability and high availability. 
The deployment process is automated using Docker and GitHub Actions for seamless updates and maintenance.

## P.S
For details about project and workflow and commands for AWS deployment, refer **worklow.md**
