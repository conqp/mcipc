pipeline {
  agent any
  stages {
    stage('Run pytest') {
      steps {
        sh 'pip install --user --upgrade pytest'
        sh 'pip install --user --upgrade -r requirements.txt'
        sh 'python -m pytest'
      }
    }

    stage('Run SonarQube') {
      steps {
        withSonarQubeEnv(installationName: 'mcipc', credentialsId: '4cdfb484-a052-41be-8739-3e1c232b5f38') {
          sh '/opt/sonar-scanner/bin/sonar-scanner'
        }

      }
    }

    stage('Send E-Mail') {
      steps {
        mail(subject: '[mcipc] build successful', body: 'https://jenkins.richard-neumann.de/blue/organizations/jenkins/mcipc/activity', from: 'jenkins@richard-neumann.de', to: 'mail@richard-neumann.de')
      }
    }

  }
}