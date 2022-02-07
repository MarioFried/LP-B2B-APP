pipeline {
    agent any
    stages {
        stage ("Git CheckOut") {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[credentialsId: 'Git-Home-Exercise', url: 'https://github.com/MarioFried/LP-B2B-APP.git']]])
            }
        }
        stage ("Build Docker Image") {
            steps {
                script {
                    sh 'docker build -t docker2mfried/flask-lp-b2b:latest .'
                }
            }
        }
        stage ("Push Docker Image - DockerHub") {
            steps {
                script {
                    withCredentials([string(credentialsId: 'DockerHubCredentials', variable: 'DockerHubCredentials')]) {
                        sh 'docker login -u docker2mfried -p ${DockerHubCredentials}'
                    }
                    sh 'docker push docker2mfried/flask-lp-b2b:latest'
                }
            }
        }
        stage ('Deploy APP on Kubernetes Cluster'){
            steps {
                script {
                    sh 'kubectl get nodes'
                    sh 'kubectl apply -f lp-b2b.yml'
                    sh 'kubectl get all -o wide'
                }
            }
        }
    }
}
