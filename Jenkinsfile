pipeline {
    agent any
    stages {
        stage('Validar Python') {
            steps { bat 'python --version' }
        }
        stage('Instalar dependencias') {
            steps { bat 'python -m pip install -r requirements.txt' }
        }
        stage('Ejecutar procesamiento') {
            steps { bat 'python scripts/procesamiento.py' }
        }
        stage('Validacion final') {
            steps { echo 'Pipeline ejecutado correctamente' }
        }
    }
}
