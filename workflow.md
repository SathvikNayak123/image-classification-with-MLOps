# Workflows

1. Create GitHub repo with `.gitignore`.
2. Create environment.
3. Set up `setup.py`.
4. Install `requirements.txt`.
5. Run `template.py`.

6. Update `config`, `params`, and `schema.yaml`.
7. Update `utils/common.py`.
8. Update `constants/__init__.py`.

Repeat for every stage(e.g data ingestion , training, evaluation, etc):
- Update `config.yaml`.
- Update `entity_config`.
- Update `configuration_manager`.
- Update components.
- Update pipeline.
- Update `main.py`.

10. Run `main.py`.
11. Create class `PredictPipeline` in pipeline.
12. Create Flask app.

13. Dockerize the application.
14. Create `.github/workflows/cicd.yaml`.

## Setup GitHub Secrets:

- `AWS_ACCESS_KEY_ID=`
- `AWS_SECRET_ACCESS_KEY=`
- `AWS_REGION=` demo>> us-east-1
- `AWS_ECR_LOGIN_URI=`   demo>> 566373416292.dkr.ecr.ap-south-1.amazonaws.com
- `ECR_REPOSITORY_NAME=` demo>> simple-app`

# AWS-CICD-Deployment-with-Github-Actions

## 1. Login to AWS console.

## 2. Create IAM user for deployment

### With specific access:

1. **EC2 access**: It is a virtual machine.
2. **ECR**: Elastic Container Registry to save your Docker image in AWS.

### Description: About the deployment

1. Build Docker image of the source code.
2. Push your Docker image to ECR.
3. Launch your EC2 instance.
4. Pull your image from ECR in EC2.
5. Launch your Docker image in EC2.

### Policy:

1. `AmazonEC2ContainerRegistryFullAccess`
2. `AmazonEC2FullAccess`

## 3. Create ECR repo to store/save Docker image

- Save the URI: `demo>> 136566696263.dkr.ecr.us-east-1.amazonaws.com/mlproject`

## 4. Create EC2 machine (Ubuntu) 

## 5. Open EC2 and Install Docker in EC2 Machine:

```bash
#optional
sudo apt-get update -y
sudo apt-get upgrade

#required
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker ubuntu
newgrp docker
```

## 6. Configure EC2 as self-hosted runner:

setting >actions >runner >new self hosted runner >choose os >then run command one by one