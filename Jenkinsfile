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
                    git branch: "master", credentialsId: "2cfb403c-be21-4fac-94d7-c8cd5c531feb", url: "https://gitlab.code.dicelab.net/JAC-IDM/python-lib.git"
                }
                sh """
                virtualenv test_env
                source test_env/bin/activate
                pip2 install mock==2.0.0 --user
                pip2 install elasticsearch==7.0.2 --user
                pip2 install urllib3==1.24.3 --user
                ./test/unit/elastic_libs/list_repos2.py
                ./test/unit/elastic_libs/list_dumps.py
                ./test/unit/elastic_libs/get_latest_dump.py
                ./test/unit/elastic_class/create_snapshot.py
                ./test/unit/elastic_class/create_snapshot_repo.py
                ./test/unit/elastic_class/delete_snapshot.py
                ./test/unit/elastic_class/delete_snapshot_repo.py
                ./test/unit/elastic_class/get_cluster_health.py
                ./test/unit/elastic_class/get_cluster_nodes.py
                ./test/unit/elastic_class/get_cluster_stats.py
                ./test/unit/elastic_class/get_cluster_status.py
                ./test/unit/elastic_class/get_disks.py
                ./test/unit/elastic_class/get_dump_list.py
                ./test/unit/elastic_class/get_info.py
                ./test/unit/elastic_class/get_master_name.py
                ./test/unit/elastic_class/get_nodes.py
                ./test/unit/elastic_class/get_repo_list.py
                ./test/unit/elastic_class/get_shards.py
                ./test/unit/elastic_class/is_active.py
                ./test/unit/elastic_class/elasticsearch_init.py
                ./test/unit/elastic_class/elasticsearch_update_status.py
                ./test/unit/elastic_class/elasticsearchdump_init.py
                ./test/unit/elastic_class/elasticsearchdump_chk_status.py
                ./test/unit/elastic_class/elasticsearchdump_dump_db.py
                ./test/unit/elastic_class/elasticsearchdump_update_dump_status.py
                ./test/unit/elastic_class/elasticsearchrepo_create_repo.py
                ./test/unit/elastic_class/elasticsearchrepo_delete_dump.py
                ./test/unit/elastic_class/elasticsearchrepo_delete_dump_all.py
                ./test/unit/elastic_class/elasticsearchrepo_delete_repo.py
                ./test/unit/elastic_class/elasticsearchrepo_init.py
                ./test/unit/elastic_class/elasticsearchrepo_update_repo_status.py
                ./test/unit/elastic_class/elasticsearchstatus_chk_all.py
                ./test/unit/elastic_class/elasticsearchstatus_chk_disk.py
                ./test/unit/elastic_class/elasticsearchstatus_chk_mem.py
                ./test/unit/elastic_class/elasticsearchstatus_chk_nodes.py
                ./test/unit/elastic_class/elasticsearchstatus_chk_server.py
                ./test/unit/elastic_class/elasticsearchstatus_chk_shards.py
                ./test/unit/elastic_class/elasticsearchstatus_chk_status.py
                ./test/unit/elastic_class/elasticsearchstatus_get_all.py
                ./test/unit/elastic_class/elasticsearchstatus_get_cluster.py
                ./test/unit/elastic_class/elasticsearchstatus_get_disk_status.py
                ./test/unit/elastic_class/elasticsearchstatus_get_dump_disk_status.py
                ./test/unit/elastic_class/elasticsearchstatus_get_gen_status.py
                ./test/unit/elastic_class/elasticsearchstatus_get_mem_status.py
                ./test/unit/elastic_class/elasticsearchstatus_get_node_status.py
                ./test/unit/elastic_class/elasticsearchstatus_get_nodes.py
                ./test/unit/elastic_class/elasticsearchstatus_get_shrd_status.py
                ./test/unit/elastic_class/elasticsearchstatus_get_svr_status.py
                ./test/unit/elastic_class/elasticsearchstatus_init.py
                ./test/unit/elastic_class/elasticsearchstatus_update_status2.py
                deactivate
                rm -rf test_env
                """
            }
        }
        stage('SonarQube analysis') {
            steps {
                sh './test/unit/sonarqube_code_coverage.sh'
                sh 'rm -rf lib'
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
                    server.credentialsId = 'art-svc-highpoint-dev'
                    uploadSpec = """{
                        "files": [
                            {
                                "pattern": "./*.py",
                                "recursive": false,
                                "excludePatterns": [],
                                "target": "pypi-proj-local/highpoint/elastic-lib/"
                            },
                            {
                                "pattern": "./*.txt",
                                "recursive": false,
                                "excludePatterns": [],
                                "target": "pypi-proj-local/highpoint/elastic-lib/"
                            },
                            {
                                "pattern": "./*.md",
                                "recursive": false,
                                "excludePatterns": [],
                                "target": "pypi-proj-local/highpoint/elastic-lib/"
                            },
                            {
                                "pattern": "*.TEMPLATE",
                                "recursive": true,
                                "excludePatterns": [],
                                "target": "pypi-proj-local/highpoint/elastic-lib/config/"
                            }
                        ]
                    }"""
                    server.upload(uploadSpec)
                }
            }
        }
    }
}
