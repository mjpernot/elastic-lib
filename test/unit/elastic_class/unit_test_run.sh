#!/bin/bash
# Unit testing program for the elastic_class module.
# This will run all the units tests for this program.
# Will need to run this from the base directory where the module file
#   is located at.

echo ""
echo "Unit test:  elastic_class"
/usr/bin/python ./test/unit/elastic_class/create_snapshot.py
/usr/bin/python ./test/unit/elastic_class/create_snapshot_repo.py
/usr/bin/python ./test/unit/elastic_class/delete_snapshot.py
/usr/bin/python ./test/unit/elastic_class/delete_snapshot_repo.py
/usr/bin/python ./test/unit/elastic_class/get_cluster_health.py
/usr/bin/python ./test/unit/elastic_class/get_cluster_nodes.py
/usr/bin/python ./test/unit/elastic_class/get_cluster_stats.py
/usr/bin/python ./test/unit/elastic_class/get_cluster_status.py
/usr/bin/python ./test/unit/elastic_class/get_disks.py
/usr/bin/python ./test/unit/elastic_class/get_dump_list.py
/usr/bin/python ./test/unit/elastic_class/get_info.py
/usr/bin/python ./test/unit/elastic_class/get_master_name.py
/usr/bin/python ./test/unit/elastic_class/get_nodes.py
/usr/bin/python ./test/unit/elastic_class/get_repo_list.py
/usr/bin/python ./test/unit/elastic_class/get_shards.py
/usr/bin/python ./test/unit/elastic_class/is_active.py
/usr/bin/python ./test/unit/elastic_class/elasticsearch_connect.py
/usr/bin/python ./test/unit/elastic_class/elasticsearch_get_disks.py
/usr/bin/python ./test/unit/elastic_class/elasticsearch_get_dump_list.py
/usr/bin/python ./test/unit/elastic_class/elasticsearch_get_info.py
/usr/bin/python ./test/unit/elastic_class/elasticsearch_get_master_name.py
/usr/bin/python ./test/unit/elastic_class/elasticsearch_get_nodes.py
/usr/bin/python ./test/unit/elastic_class/elasticsearch_get_repo_list.py
/usr/bin/python ./test/unit/elastic_class/elasticsearch_get_shards.py
/usr/bin/python ./test/unit/elastic_class/elasticsearch_init.py
/usr/bin/python ./test/unit/elastic_class/elasticsearch_is_active.py
/usr/bin/python ./test/unit/elastic_class/elasticsearch_set_login_config.py
/usr/bin/python ./test/unit/elastic_class/elasticsearch_set_ssl_config.py
/usr/bin/python ./test/unit/elastic_class/elasticsearch_update_status.py
/usr/bin/python ./test/unit/elastic_class/elasticsearchdump_chk_status.py
/usr/bin/python ./test/unit/elastic_class/elasticsearchdump_connect.py
/usr/bin/python ./test/unit/elastic_class/elasticsearchdump_dump_db.py
/usr/bin/python ./test/unit/elastic_class/elasticsearchdump_init.py
/usr/bin/python ./test/unit/elastic_class/elasticsearchdump_update_dump_status.py
/usr/bin/python ./test/unit/elastic_class/elasticsearchrepo_connect.py
/usr/bin/python ./test/unit/elastic_class/elasticsearchrepo_create_repo.py
/usr/bin/python ./test/unit/elastic_class/elasticsearchrepo_delete_dump.py
/usr/bin/python ./test/unit/elastic_class/elasticsearchrepo_delete_dump_all.py
/usr/bin/python ./test/unit/elastic_class/elasticsearchrepo_delete_repo.py
/usr/bin/python ./test/unit/elastic_class/elasticsearchrepo_init.py
/usr/bin/python ./test/unit/elastic_class/elasticsearchrepo_update_repo_status.py
/usr/bin/python ./test/unit/elastic_class/elasticsearchstatus_chk_all.py
/usr/bin/python ./test/unit/elastic_class/elasticsearchstatus_chk_disk.py
/usr/bin/python ./test/unit/elastic_class/elasticsearchstatus_chk_mem.py
/usr/bin/python ./test/unit/elastic_class/elasticsearchstatus_chk_nodes.py
/usr/bin/python ./test/unit/elastic_class/elasticsearchstatus_chk_server.py
/usr/bin/python ./test/unit/elastic_class/elasticsearchstatus_chk_shards.py
/usr/bin/python ./test/unit/elastic_class/elasticsearchstatus_chk_status.py
/usr/bin/python ./test/unit/elastic_class/elasticsearchstatus_connect.py
/usr/bin/python ./test/unit/elastic_class/elasticsearchstatus_get_all.py
/usr/bin/python ./test/unit/elastic_class/elasticsearchstatus_get_cluster.py
/usr/bin/python ./test/unit/elastic_class/elasticsearchstatus_get_disk_status.py
/usr/bin/python ./test/unit/elastic_class/elasticsearchstatus_get_dump_disk_status.py
/usr/bin/python ./test/unit/elastic_class/elasticsearchstatus_get_gen_status.py
/usr/bin/python ./test/unit/elastic_class/elasticsearchstatus_get_mem_status.py
/usr/bin/python ./test/unit/elastic_class/elasticsearchstatus_get_node_status.py
/usr/bin/python ./test/unit/elastic_class/elasticsearchstatus_get_nodes.py
/usr/bin/python ./test/unit/elastic_class/elasticsearchstatus_get_shrd_status.py
/usr/bin/python ./test/unit/elastic_class/elasticsearchstatus_get_svr_status.py
/usr/bin/python ./test/unit/elastic_class/elasticsearchstatus_init.py
/usr/bin/python ./test/unit/elastic_class/elasticsearchstatus_update_status2.py
