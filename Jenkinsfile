pipeline {
    agent { docker { image 'python:3.9' } }
    stages {
        stage('Checkout') {
            steps { git 'https://github.com/YOUR_USERNAME/my-api.git' }
        }
        stage('Install Dependencies') {
            steps { sh 'pip install flask' }
        }
        stage('Run Tests') {
            steps { sh 'python app.py &' }
        }
    }
}
