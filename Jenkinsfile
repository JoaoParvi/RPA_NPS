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
                bat '"C:\\Users\\adm.luiz.vinicius\\AppData\\Local\\Programs\\Python\\Python312\\python.exe" NPS_StarClass.py'
            }
        }
    }
}