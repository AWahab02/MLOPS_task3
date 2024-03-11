pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out to main branch'
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/Lazer430/MLOPS_ClassTask_2_i200432.git']])
            }
        }
        stage('Build') {
            steps {
                echo 'Building'
                withPythonEnv('python') {
                    sh 'make install'
                }
            }
        }
        stage('Test') {
            steps {
                echo 'Testing'
                withPythonEnv('python') {
                    sh 'make test'
                }
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying'
                script {
                    def branch = "${env.BRANCH_NAME}"
                    println("Current Branch is:"+ branch)
                    
                    if (branch == "main"){
                        println("Deploying to main")
                    }
                    else {
                        println("Deploying to dev")
                    }
                }
            }
        }
    }
}
