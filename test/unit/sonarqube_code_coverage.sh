#!/bin/bash
# Unit test code coverage for SonarQube to cover all modules.
# This will run the Python code coverage module against all unit test modules.
# This will show the amount of code that was tested and which lines of code
#	that was skipped during the test.

coverage erase

echo ""
echo "Running unit test modules in conjunction with coverage"
coverage run -a --source=elastic_class test/unit/elastic_class/get_cluster_health.py
coverage run -a --source=elastic_class test/unit/elastic_class/get_cluster_nodes.py
coverage run -a --source=elastic_class test/unit/elastic_class/get_cluster_status.py
coverage run -a --source=elastic_class test/unit/elastic_class/get_dump_list.py
coverage run -a --source=elastic_class test/unit/elastic_class/get_info.py
coverage run -a --source=elastic_class test/unit/elastic_class/get_nodes.py
coverage run -a --source=elastic_class test/unit/elastic_class/get_repo_list.py
coverage run -a --source=elastic_class test/unit/elastic_class/is_active.py
coverage run -a --source=elastic_class test/unit/elastic_class/Elastic_init.py
coverage run -a --source=elastic_class test/unit/elastic_class/ElasticCluster_init.py
coverage run -a --source=elastic_class test/unit/elastic_class/ElasticSearch_init.py
coverage run -a --source=elastic_class test/unit/elastic_class/ElasticSearchDump_init.py
coverage run -a --source=elastic_class test/unit/elastic_class/ElasticSearchDump_chk_status.py
coverage run -a --source=elastic_class test/unit/elastic_class/ElasticSearchDump_dump_db.py
coverage run -a --source=elastic_class test/unit/elastic_class/ElasticSearchRepo_create_repo.py
coverage run -a --source=elastic_class test/unit/elastic_class/ElasticSearchRepo_delete_dump.py
coverage run -a --source=elastic_class test/unit/elastic_class/ElasticSearchRepo_delete_dump_all.py
coverage run -a --source=elastic_class test/unit/elastic_class/ElasticSearchRepo_delete_repo.py
coverage run -a --source=elastic_class test/unit/elastic_class/ElasticSearchRepo_init.py
coverage run -a --source=elastic_class test/unit/elastic_class/ElasticStatus_chk_all.py
coverage run -a --source=elastic_class test/unit/elastic_class/ElasticStatus_chk_disk.py
coverage run -a --source=elastic_class test/unit/elastic_class/ElasticStatus_chk_mem.py
coverage run -a --source=elastic_class test/unit/elastic_class/ElasticStatus_chk_nodes.py
coverage run -a --source=elastic_class test/unit/elastic_class/ElasticStatus_chk_server.py
coverage run -a --source=elastic_class test/unit/elastic_class/ElasticStatus_chk_shards.py
coverage run -a --source=elastic_class test/unit/elastic_class/ElasticStatus_chk_status.py
coverage run -a --source=elastic_class test/unit/elastic_class/ElasticStatus_get_all.py
coverage run -a --source=elastic_class test/unit/elastic_class/ElasticStatus_get_cluster.py
coverage run -a --source=elastic_class test/unit/elastic_class/ElasticStatus_get_disk_status.py
coverage run -a --source=elastic_class test/unit/elastic_class/ElasticStatus_get_dump_disk_status.py
coverage run -a --source=elastic_class test/unit/elastic_class/ElasticStatus_get_gen_status.py
coverage run -a --source=elastic_class test/unit/elastic_class/ElasticStatus_get_mem_status.py
coverage run -a --source=elastic_class test/unit/elastic_class/ElasticStatus_get_nodes.py
coverage run -a --source=elastic_class test/unit/elastic_class/ElasticStatus_get_node_status.py
coverage run -a --source=elastic_class test/unit/elastic_class/ElasticStatus_get_shrd_status.py
coverage run -a --source=elastic_class test/unit/elastic_class/ElasticStatus_get_svr_status.py
coverage run -a --source=elastic_class test/unit/elastic_class/ElasticStatus_init.py
coverage run -a --source=elastic_libs test/unit/elastic_libs/list_repos2.py
coverage run -a --source=elastic_libs test/unit/elastic_libs/list_dumps.py
coverage run -a --source=elastic_libs test/unit/elastic_libs/get_latest_dump.py

echo ""
echo "Producing code coverage report"
coverage combine
coverage report -m
coverage xml -i

