pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'pip3 install virtualenv'
                sh 'pip3 install -r requirements.txt'

            }
        }
        stage('run tests') {
            steps {
                sh 'python3 -m pytest -s -v --html=report.html tests/home/test_login.py  --browser zalenium'

            }
        }

        }
     }
