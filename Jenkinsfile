pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                git url: 'https://github.com/Ariaryy/test-junit', branch: 'main'
                bat "mvn clean package"
            }
        }
            
        stage('Build & Test') {
            steps {
                bat "mvn clean package"
            }
        }
            
        stage('Docker') {
            steps {
                bat "docker build -t junit-test-demo:latest ."
            }
        }
    }
    post {
        // If Maven was able to run the tests, even if some of the test
        // failed, record the test results and archive the jar file.
        success {
            junit '**/target/surefire-reports/TEST-*.xml'
            archiveArtifacts artifacts: 'target/**/*.jar, target/site/jacoco/**', fingerprint: true
        }
    }
}
