pipeline {
    agent {
        docker {
            image 'my-custom-python-image:latest' // Replace with your custom image name and tag
            args '-u root' // Use root user inside Docker (be cautious with this!)
        }
    }
    triggers {
        pollSCM '*/5 * * * *'
    }
    stages {

        stage('Setup Python Environment') {
            steps {
                echo "Setting up Python Environment..."
                sh '''
                apt-get update
                apt-get install -v python3.11-venv
                python3 -m venv venv
                '''
            }
        }
        stage('Build') {
            steps {
                echo "Building.."
                sh '''
                . venv/bin/activate
                pip install -r requirements.txt
                '''
            }
        }
        stage('Deliver') {
            steps {
                echo 'Deliver....'
                sh '''
                echo "doing delivery stuff.."
                '''
            }
        }
    }
}