pipeline {
    agent {
        docker { image 'python:3' }
    }
    stages {
        stage('Build') {
            steps {
                sh 'pip3 install virtualenv'
                sh 'source myvenv/Scripts/activate'
                sh 'pip3 install -r requirements.txt'
                sh 'python3 manage.py test'

            }
        }
        stage('run tests') {
            steps {

                sh 'pytest -s -v --html=report.html tests/home/test_login.py  --browser zalenium'

            }
        }

        }
     }
