pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                script {
                    checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/AWahab02/MLOPS_task3.git']])                }
            }
        }
        
        stage('Build') {
            steps {
                withPythonEnv('python'){
                    sh 'make install'
                }
            }
        }
        
        stage('Test') {
            steps {
                withPythonEnv('python'){
                    sh 'make test'
                }
            }
        }
        
        stage('Deploy') {
            steps {
                script {
                    if (env.BRANCH_NAME == 'main') {
                        echo 'deployed to main'
                    } else if (env.BRANCH_NAME == 'dev') {
                        echo 'deployed to dev'
                    } else {
                        echo "Branch not supported for deployment"
                    }
                }
            }
        }
    }
}
