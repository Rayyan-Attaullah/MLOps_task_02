pipeline {
    agent any
    
    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-credentials') // Replace with your Jenkins credential ID for DockerHub
        DOCKER_IMAGE_NAME = 'rayyanattaullah/mlops_task_02' // Replace with your Docker image name
        GIT_REPO = 'https://github.com/Rayyan-Attaullah/MLOps_task_02.git'
    }
    
    stages {
        stage('Checkout SCM') {
            steps {
                checkout([$class: 'GitSCM', 
                          branches: [[name: '*/main']],
                          userRemoteConfigs: [[url: "${GIT_REPO}"]]
                ])
            }
        }
        
        stage('Set up Docker Buildx') {
            steps {
                script {
                    // Ensure Docker Buildx is set up (required for building multi-platform images)
                    sh 'docker buildx create --use || echo "Buildx already configured"'
                }
            }
        }
        
        stage('Login to Docker Hub') {
            steps {
                script {
                    docker.withRegistry('https://index.docker.io/v1/', 'dockerhub-credentials') {
                        echo 'Logged in to Docker Hub successfully'
                    }
                }
            }
        }
        
        stage('Build and Push Docker Image') {
            steps {
                script {
                    // Build Docker image and push it to Docker Hub
                    sh """
                        docker build -t ${DOCKER_IMAGE_NAME}:latest .
                        docker push ${DOCKER_IMAGE_NAME}:latest
                    """
                }
            }
        }
        
        stage('Log Docker Images') {
            steps {
                sh 'docker images'
            }
        }
    }
    
    post {
        always {
            cleanWs() // Clean up workspace after pipeline completion
        }
        
        success {
            echo 'Pipeline completed successfully!'
        }
        
        failure {
            echo 'Pipeline failed. Please check logs for more details.'
        }
    }
}
