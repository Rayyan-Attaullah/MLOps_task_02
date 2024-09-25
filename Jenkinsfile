pipeline {
    agent any

    environment {
        // Jenkins credentials ID where DockerHub credentials are stored
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-credentials') // Use Jenkins credentials for Docker Hub login
        DOCKER_USERNAME = "${DOCKERHUB_CREDENTIALS_USR}"
        DOCKER_PASSWORD = "${DOCKERHUB_CREDENTIALS_PSW}"
    }

    stages {
        stage('Checkout Code') {
            steps {
                // Checkout the repository code
                checkout scm
            }
        }

        stage('Set up Docker Buildx') {
            steps {
                script {
                    sh '''
                        # Install Docker Buildx if not already available
                        docker buildx version || docker run --rm --privileged multiarch/qemu-user-static --reset -p yes
                        docker buildx create --use
                    '''
                }
            }
        }

        stage('Login to Docker Hub') {
            steps {
                script {
                    // Use the environment variables to log in to Docker Hub
                    sh '''
                        echo $DOCKER_PASSWORD | docker login -u $DOCKER_USERNAME --password-stdin
                    '''
                }
            }
        }

        stage('Build and Push Docker Image') {
            steps {
                script {
                    // Build the Docker image and push it to Docker Hub using the Makefile commands
                    sh 'make docker'
                    sh 'make push'
                }
            }
        }

        stage('Log Docker Images') {
            steps {
                script {
                    // Log Docker images for verification
                    sh 'make images'
                }
            }
        }
    }

    post {
        always {
            // Clean up the workspace after the pipeline execution
            cleanWs()
        }
    }
}
