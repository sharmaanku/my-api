pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git credentialsId: 'github-credentials', 
                    url: 'https://github.com/sharmaanku/my-api.git', 
                    branch: 'main'
            }
        }

        stage('Build') {
            steps {
                sh 'echo "Building the project..."'
                sh 'mkdir -p build && touch build/artifact.txt'
            }
        }

        stage('Run Unit Tests') {
            steps {
                sh 'echo "Running unit tests..."'
                sh 'python3 -m unittest discover tests'
            }
        }

        stage('Deploy') {
            steps {
                sh 'echo "Deploying application..."'
            }
        }
    }
}

