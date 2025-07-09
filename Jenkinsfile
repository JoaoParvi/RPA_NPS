pipeline {
    agent any

    stages {
        stage('Clonar o repositório') {
            steps {
                git branch: 'NPS_Diaria',
                    url: 'https://github.com/JoaoParvi/RPA_NPS.git'
            }
        }

        stage('Instalar dependências') {
            steps {
                bat '"C:\\Users\\adm.luiz.vinicius\\AppData\\Local\\Programs\\Python\\Python312\\Scripts\\pip.exe" install -r requirements.txt'
            }
        }

        stage('Executar script Python') {
            steps {
                bat '"C:\\Users\\adm.luiz.vinicius\\AppData\\Local\\Programs\\Python\\Python312\\python.exe" NPS_Diario.py'
            }
        }
    }

    post {
        always {
            script {
                emailext(
                    subject: "RESULTADO: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                    body: """
                        <p>Job <b>${env.JOB_NAME}</b> executado com status: <b>${currentBuild.currentResult}</b>.</p>
                        <p><a href='${env.BUILD_URL}'>Ver detalhes no Jenkins</a></p>
                    """,
                    mimeType: 'text/html',
                    to: 'bielgagg94@gmail.com'
                )
            }
        }
    }
}
