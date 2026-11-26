pipeline{
    agent any

    environment {
        APP_NAME = "python-desktop-app"
        PYTHON = "python3"
    }

    stages {
        
        stage ('Clean Workspace'){
            steps {
                cleanWs()
                echo "Fresh workspace ready."
            }
        }

        stage('Git Checkout'){
            steps{
                git branch: 'main',
                    credentialsId: 'github-creds',
                    url: 'https://github.com/soumilj94/python-desktop-app.git'
                echo "Code pulled from source branch. Commit ID: ${env.GIT_COMMIT}"
            }
        }

        stage('Setup Python Environment'){
            steps{
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                    pip install pytest
                '''
            }
        }

        stage('Run Tests'){
            steps{
                sh '''
                    . venv/bin/activate
                    pytest test_app.py -v --tb=short
                '''
            }
        }
        
        stage('SonarQube analysis'){
            steps{
                withSonarQubeEnv('sonar-server'){
                    sh '''
                        ${SCANNER_HOME}/bin/sonar-scanner \
                        -Dsonar.projectKey=python-desktop-app \
                        -Dsonar.projectName=python-desktop-app \
                        -Dsonar.sources=. \
                        -Dsonar.exclusions=venv/**
                    '''
                }
            }
        }
        
        stage('Quality gate'){
            steps{
                timeout(time: 2, unit: 'MINUTES'){
                    waitForQualityGate abortPipeline: false
                }
            }
        }

        stage('Package App'){
            steps{
                sh '''
                    . venv/bin/activate
                    pip install pyinstaller
                    pyinstaller --onefile app.py
                '''
                echo "App Packaged. Binary in dist/app"
            }
        }
        
        stage('Archieve artifact'){
            steps{
                archieveArtifacts artifact: 'dist/app', allowEmptyArchive: false
                echo "Binary archived in jenkins - downloadable from build page"
            }
        }
    }

    post{
        success{
            echo 'BUILD #${BUILD_NUMBER} SUCCEEDED'
        }
        failure{
            echo 'BUILD #${BUILD_NUMBER} FAILED - check logs'
        }
        always{
            sh 'rm -rf venv dist build || true'
            echo "Cleanup done."
        }
    }
}