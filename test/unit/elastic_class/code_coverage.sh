#!/bin/bash
# Unit test code coverage for elastic_class module.
# This will run the Python code coverage module against all unit test modules.
# This will show the amount of code that was tested and which lines of code
#   that was skipped during the test.

coverage erase

echo ""
echo "Running unit test modules in conjunction with coverage"
coverage run -a --source=elastic_class test/unit/elastic_class/create_snapshot.py
coverage run -a --source=elastic_class test/unit/elastic_class/create_snapshot_repo.py
coverage run -a --source=elastic_class test/unit/elastic_class/delete_snapshot.py
coverage run -a --source=elastic_class test/unit/elastic_class/delete_snapshot_repo.py
coverage run -a --source=elastic_class test/unit/elastic_class/get_cluster_health.py
coverage run -a --source=elastic_class test/unit/elastic_class/get_cluster_nodes.py
coverage run -a --source=elastic_class test/unit/elastic_class/get_cluster_stats.py
coverage run -a --source=elastic_class test/unit/elastic_class/get_cluster_status.py
coverage run -a --source=elastic_class test/unit/elastic_class/get_disks.py
coverage run -a --source=elastic_class test/unit/elastic_class/get_dump_list.py
coverage run -a --source=elastic_class test/unit/elastic_class/get_info.py
coverage run -a --source=elastic_class test/unit/elastic_class/get_master_name.py
coverage run -a --source=elastic_class test/unit/elastic_class/get_nodes.py
coverage run -a --source=elastic_class test/unit/elastic_class/get_repo_list.py
coverage run -a --source=elastic_class test/unit/elastic_class/get_shards.py
coverage run -a --source=elastic_class test/unit/elastic_class/is_active.py
coverage run -a --source=elastic_class test/unit/elastic_class/elasticsearch_init.py
coverage run -a --source=elastic_class test/unit/elastic_class/elasticsearch_connect.py
coverage run -a --source=elastic_class test/unit/elastic_class/elasticsearch_is_active.py
coverage run -a --source=elastic_class test/unit/elastic_class/elasticsearch_get_info.py
coverage run -a --source=elastic_class test/unit/elastic_class/elasticsearch_get_master_name.py
coverage run -a --source=elastic_class test/unit/elastic_class/elasticsearch_get_nodes.py
coverage run -a --source=elastic_class test/unit/elastic_class/elasticsearch_get_repo_list.py
coverage run -a --source=elastic_class test/unit/elastic_class/elasticsearch_get_shards.py
coverage run -a --source=elastic_class test/unit/elastic_class/elasticsearch_set_login_config.py
coverage run -a --source=elastic_class test/unit/elastic_class/elasticsearch_set_ssl_config.py
coverage run -a --source=elastic_class test/unit/elastic_class/elasticsearch_update_status.py
coverage run -a --source=elastic_class test/unit/elastic_class/elasticsearchdump_chk_status.py
coverage run -a --source=elastic_class test/unit/elastic_class/elasticsearchdump_connect.py
coverage run -a --source=elastic_class test/unit/elastic_class/elasticsearchdump_dump_db.py
coverage run -a --source=elastic_class test/unit/elastic_class/elasticsearchdump_init.py
coverage run -a --source=elastic_class test/unit/elastic_class/elasticsearchdump_update_dump_status.py
coverage run -a --source=elastic_class test/unit/elastic_class/elasticsearchrepo_connect.py
coverage run -a --source=elastic_class test/unit/elastic_class/elasticsearchrepo_create_repo.py
coverage run -a --source=elastic_class test/unit/elastic_class/elasticsearchrepo_delete_dump.py
coverage run -a --source=elastic_class test/unit/elastic_class/elasticsearchrepo_delete_dump_all.py
coverage run -a --source=elastic_class test/unit/elastic_class/elasticsearchrepo_delete_repo.py
coverage run -a --source=elastic_class test/unit/elastic_class/elasticsearchrepo_init.py
coverage run -a --source=elastic_class test/unit/elastic_class/elasticsearchrepo_update_repo_status.py
coverage run -a --source=elastic_class test/unit/elastic_class/elasticsearchstatus_chk_all.py
coverage run -a --source=elastic_class test/unit/elastic_class/elasticsearchstatus_chk_disk.py
coverage run -a --source=elastic_class test/unit/elastic_class/elasticsearchstatus_chk_mem.py
coverage run -a --source=elastic_class test/unit/elastic_class/elasticsearchstatus_chk_nodes.py
coverage run -a --source=elastic_class test/unit/elastic_class/elasticsearchstatus_chk_server.py
coverage run -a --source=elastic_class test/unit/elastic_class/elasticsearchstatus_chk_shards.py
coverage run -a --source=elastic_class test/unit/elastic_class/elasticsearchstatus_chk_status.py
coverage run -a --source=elastic_class test/unit/elastic_class/elasticsearchstatus_connect.py
coverage run -a --source=elastic_class test/unit/elastic_class/elasticsearchstatus_get_all.py
coverage run -a --source=elastic_class test/unit/elastic_class/elasticsearchstatus_get_cluster.py
coverage run -a --source=elastic_class test/unit/elastic_class/elasticsearchstatus_get_disk_status.py
coverage run -a --source=elastic_class test/unit/elastic_class/elasticsearchstatus_get_dump_disk_status.py
coverage run -a --source=elastic_class test/unit/elastic_class/elasticsearchstatus_get_gen_status.py
coverage run -a --source=elastic_class test/unit/elastic_class/elasticsearchstatus_get_mem_status.py
coverage run -a --source=elastic_class test/unit/elastic_class/elasticsearchstatus_get_node_status.py
coverage run -a --source=elastic_class test/unit/elastic_class/elasticsearchstatus_get_nodes.py
coverage run -a --source=elastic_class test/unit/elastic_class/elasticsearchstatus_get_shrd_status.py
coverage run -a --source=elastic_class test/unit/elastic_class/elasticsearchstatus_get_svr_status.py
coverage run -a --source=elastic_class test/unit/elastic_class/elasticsearchstatus_init.py
coverage run -a --source=elastic_class test/unit/elastic_class/elasticsearchstatus_update_status2.py

echo ""
echo "Producing code coverage report"
coverage combine
coverage report -m

