pipeline {
    agent any

    environment {
        IMAGE_NAME = "flask-cicd-app"
        IMAGE_TAG = "latest"
        CLUSTER_NAME = "flask-cluster"
    }

    stages {

        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate

                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Unit Tests') {
            steps {
                sh '''
                . venv/bin/activate

                export PYTHONPATH=$WORKSPACE

                pytest -v
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                docker build -t ${IMAGE_NAME}:${IMAGE_TAG} .
                '''
            }
        }

        stage('Verify Docker Image') {
            steps {
                sh '''
                docker images | grep ${IMAGE_NAME}
                '''
            }
        }

        stage('Load Image into Kind') {
            steps {
                sh '''
                kind load docker-image ${IMAGE_NAME}:${IMAGE_TAG} --name ${CLUSTER_NAME}
                '''
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh '''
                kubectl apply -f k8s/deployment.yaml --validate=false
                kubectl apply -f k8s/service.yaml --validate=false
                '''
            }
        }

        stage('Verify Deployment') {
            steps {
                sh '''
                kubectl rollout status deployment/flask-app
                kubectl get pods
                kubectl get svc
                '''
            }
        }
    }

    post {
        success {
            echo '✅ Application deployed successfully!'
        }

        failure {
            echo '❌ Deployment failed.'
        }
    }
}
