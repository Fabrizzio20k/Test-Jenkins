pipeline {
    agent any

    options {
        buildDiscarder(logRotator(numToKeepStr: '5'))
    }

    stages {
        stage('Checkout Repo') {
            steps {
                checkout scm
            }
        }
        
        stage('Test (En Contenedor Python)') {
            agent {
                docker {
                    image 'python:3.13-slim'
                    reuseNode true 
                }
            }
            steps {
                sh '''
                    # 1. Crear y activar un entorno virtual dentro del workspace
                    python -m venv venv
                    . venv/bin/activate
                    
                    # 2. Instalar dependencias desactivando la caché (evita errores de permisos)
                    pip install --no-cache-dir -r requirements.txt
                    
                    # 3. Ejecutar las pruebas (en su propia línea)
                    pytest tests/ --cov=app --cov-report=xml:coverage.xml
                '''
            }
        }
        
        stage('SonarQube Analysis') {
            environment {
                scannerHome = tool 'SonarScanner'
            }
            steps {
                withSonarQubeEnv('SonarQube-Server') {
                    sh "${scannerHome}/bin/sonar-scanner"
                }
            }
        }
        
        stage('Quality Gate') {
            steps {
                timeout(time: 1, unit: 'HOURS') {
                    waitForQualityGate abortPipeline: true
                }
            }
        }
    }
}