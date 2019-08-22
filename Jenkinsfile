pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                sh 'python --version'
            }
        }
        stage('Test') {
            steps {
                dir ('lib') {
                    git branch: "master", credentialsId: "2cfb403c-be21-4fac-94d7-c8cd5c531feb", url: "https://gitlab.dicelab.net/JAC-IDM/python-lib.git"
                }
                dir ('requests_lib') {
                    git branch: "master", credentialsId: "2cfb403c-be21-4fac-94d7-c8cd5c531feb", url: "https://gitlab.dicelab.net/JAC-IDM/requests-lib.git"
                }
                sh """
                virtualenv test_env
                source test_env/bin/activate
                pip2 install mock --user
                pip2 install elasticsearch --user
                pip2 install requests --user
                ./test/unit/elastic_libs/list_repos2.py
                ./test/unit/elastic_libs/list_dumps.py
                ./test/unit/elastic_libs/get_latest_dump.py
                ./test/unit/elastic_class/Elastic_init.py
                ./test/unit/elastic_class/ElasticCluster_init.py
                ./test/unit/elastic_class/ElasticSearch_init.py
                ./test/unit/elastic_class/ElasticSearchDump_init.py
                ./test/unit/elastic_class/ElasticSearchDump_chk_status.py
                ./test/unit/elastic_class/ElasticSearchDump_dump_db.py
                ./test/unit/elastic_class/ElasticSearchRepo_create_repo.py
                ./test/unit/elastic_class/ElasticSearchRepo_delete_dump.py
                ./test/unit/elastic_class/ElasticSearchRepo_delete_dump_all.py
                ./test/unit/elastic_class/ElasticSearchRepo_delete_repo.py
                ./test/unit/elastic_class/ElasticSearchRepo_init.py
                ./test/unit/elastic_class/ElasticStatus_init.py
                deactivate
                rm -rf test_env
                """
            }
        }
        stage('SonarQube analysis') {
            steps {
                sh './test/unit/sonarqube_code_coverage.sh'
                sh 'rm -rf lib'
                sh 'rm -rf requests_lib'
                script {
                    scannerHome = tool 'sonar-scanner';
                }
                withSonarQubeEnv('Sonar') {
                    sh "${scannerHome}/bin/sonar-scanner -Dproject.settings=sonar-project.JACIDM.properties"
                }
            
            }
        }
        stage('Artifactory upload') {
            steps {
                script {
                    server = Artifactory.server('Artifactory')
                    server.credentialsId = 'svc-highpoint-artifactory'
                    uploadSpec = """{
                        "files": [
                            {
                                "pattern": "./*.py",
                                "recursive": false,
                                "excludePatterns": [],
                                "target": "generic-local/highpoint/elastic-lib/"
                            },
                            {
                                "pattern": "./*.txt",
                                "recursive": false,
                                "excludePatterns": [],
                                "target": "generic-local/highpoint/elastic-lib/"
                            },
                            {
                                "pattern": "./*.md",
                                "recursive": false,
                                "excludePatterns": [],
                                "target": "generic-local/highpoint/elastic-lib/"
                            },
                            {
                                "pattern": "*.TEMPLATE",
                                "recursive": true,
                                "excludePatterns": [],
                                "target": "generic-local/highpoint/elastic-lib/config/"
                            }
                        ]
                    }"""
                    server.upload(uploadSpec)
                }
            }
        }
    }
}
