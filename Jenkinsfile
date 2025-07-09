pipeline {
    agent any

    stages {
        stage('Clonar o repositório') {
            steps {
                git branch: 'NPS_StarClass',
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
                bat '"C:\\Users\\adm.luiz.vinicius\\AppData\\Local\\Programs\\Python\\Python312\\python.exe" NPS_ANUAL.py'
            }
        }
    }

    post {
        success {
            emailext(
                subject: "SUCESSO: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                body: """<p>O job ${env.JOB_NAME} finalizou com sucesso.</p>
                         <p>Veja mais detalhes em: <a href='${env.BUILD_URL}'>${env.BUILD_URL}</a></p>""",
                to: 'bielgagg94@gmail.com'
            )
        }

        failure {
            emailext(
                subject: "FALHA: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                body: """<p>O job ${env.JOB_NAME} falhou.</p>
                         <p>Veja mais detalhes em: <a href='${env.BUILD_URL}'>${env.BUILD_URL}</a></p>""",
                to: 'bielgagg94@gmail.com'
            )
        }
    }
}
