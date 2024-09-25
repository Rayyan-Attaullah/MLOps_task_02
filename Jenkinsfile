pipeline {
    agent any
    
    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-credentials') 
        DOCKER_IMAGE_NAME = 'rayyanatttaullah09/mlops_task_02' 
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
                    bat """
                        docker build -t ${DOCKER_IMAGE_NAME}:latest .
                        docker push ${DOCKER_IMAGE_NAME}:latest
                    """
                }
            }
        }
        
        stage('Log Docker Images') {
            steps {
                bat 'docker images'
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
