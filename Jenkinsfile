pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/BolaWagdy/QR-flask-app.git'
            }
        }
        stage('Set up Python') {
            steps {
                sh ```
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install -r requirements.txt
                    pytest app.py
                ```
            }
        }
        stage('Build Docker image') {
            steps {
                sh 'docker build -t app_py .'
            }
        }
    post {
        always {
            cleanWs()
        }
    }
}
}
