pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                // Get some code from a GitHub repository
                git 'https://github.com/2206-devops-batch/flask-demo.git'

                // Run venv
                sh "python -m venv .venv"

                // Run pip install
                sh "pip install -r requirements-dev.txt"
                
                // Run pytest
                sh "pytest app-test.py"
            }
        }
    }
}
