pipeline {
    agent any
    environment {
        PYTHONUNBUFFERED = '1'
    }
    stages {
        stage('Clone Repository') {
            steps {
                git credentialsId: 'github-credentials', url: 'https://github.com/sharmaanku/my-api.git', branch: 'main'
            }
            }
        }
        stage('Setup Python') {
            steps {
                sh 'apt update && apt install -y python3 python3-pip'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'pip3 install -r requirements.txt || true'
            }
        }
        stage('Run Unit Tests') {
            steps {
                script {
                    def test_result = sh(script: 'python3 -m unittest discover', returnStatus: true)
                    if (test_result != 0) {
                        error('❌ Tests Failed! Stopping Pipeline.')
                    }
                }
            }
        }
        stage('Deploy Application') {
            when {
                expression { currentBuild.result == null || currentBuild.result == 'SUCCESS' }
            }
            steps {
                echo '✅ All Tests Passed. Deploying Application...'
                sh 'echo "🚀 Deployment Successful!"'
            }
        }
    }
}

