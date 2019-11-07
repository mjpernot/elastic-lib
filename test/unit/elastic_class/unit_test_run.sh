#!/bin/bash
# Unit testing program for the elastic_class module.
# This will run all the units tests for this program.
# Will need to run this from the base directory where the module file
#   is located at.

echo ""
echo "Unit test:  elastic_class"
test/unit/elastic_class/create_snapshot.py
test/unit/elastic_class/create_snapshot_repo.py
test/unit/elastic_class/delete_snapshot.py
test/unit/elastic_class/delete_snapshot_repo.py
test/unit/elastic_class/get_cluster_health.py
test/unit/elastic_class/get_cluster_nodes.py
test/unit/elastic_class/get_cluster_stats.py
test/unit/elastic_class/get_cluster_status.py
test/unit/elastic_class/get_disks.py
test/unit/elastic_class/get_dump_list.py
test/unit/elastic_class/get_info.py
test/unit/elastic_class/get_master_name.py
test/unit/elastic_class/get_nodes.py
test/unit/elastic_class/get_repo_list.py
test/unit/elastic_class/get_shards.py
test/unit/elastic_class/is_active.py
test/unit/elastic_class/Elastic_init.py
test/unit/elastic_class/ElasticCluster_init.py
test/unit/elastic_class/ElasticSearch_init.py
test/unit/elastic_class/ElasticSearch_update_status.py
test/unit/elastic_class/ElasticSearchDump_chk_status.py
test/unit/elastic_class/ElasticSearchDump_init.py
test/unit/elastic_class/ElasticSearchDump_dump_db.py
test/unit/elastic_class/ElasticSearchRepo_create_repo.py
test/unit/elastic_class/ElasticSearchRepo_delete_dump.py
test/unit/elastic_class/ElasticSearchRepo_delete_dump_all.py
test/unit/elastic_class/ElasticSearchRepo_delete_repo.py
test/unit/elastic_class/ElasticSearchRepo_init.py
test/unit/elastic_class/ElasticSearchStatus_chk_all.py
test/unit/elastic_class/ElasticSearchStatus_chk_disk.py
test/unit/elastic_class/ElasticSearchStatus_chk_mem.py
test/unit/elastic_class/ElasticSearchStatus_chk_nodes.py
test/unit/elastic_class/ElasticSearchStatus_chk_server.py
test/unit/elastic_class/ElasticSearchStatus_chk_shards.py
test/unit/elastic_class/ElasticSearchStatus_chk_status.py
test/unit/elastic_class/ElasticSearchStatus_get_cluster.py
test/unit/elastic_class/ElasticSearchStatus_get_disk_status.py
test/unit/elastic_class/ElasticSearchStatus_get_dump_disk_status.py
test/unit/elastic_class/ElasticSearchStatus_get_gen_status.py
test/unit/elastic_class/ElasticSearchStatus_get_mem_status.py
test/unit/elastic_class/ElasticSearchStatus_get_node_status.py
test/unit/elastic_class/ElasticSearchStatus_get_nodes.py
test/unit/elastic_class/ElasticSearchStatus_get_shrd_status.py
test/unit/elastic_class/ElasticSearchStatus_get_svr_status.py
test/unit/elastic_class/ElasticSearchStatus_init.py
test/unit/elastic_class/ElasticSearchStatus_update_status.py
test/unit/elastic_class/ElasticStatus_chk_all.py
test/unit/elastic_class/ElasticStatus_chk_disk.py
test/unit/elastic_class/ElasticStatus_chk_mem.py
test/unit/elastic_class/ElasticStatus_chk_nodes.py
test/unit/elastic_class/ElasticStatus_chk_server.py
test/unit/elastic_class/ElasticStatus_chk_shards.py
test/unit/elastic_class/ElasticStatus_chk_status.py
test/unit/elastic_class/ElasticStatus_get_all.py
test/unit/elastic_class/ElasticStatus_get_cluster.py
test/unit/elastic_class/ElasticStatus_get_disk_status.py
test/unit/elastic_class/ElasticStatus_get_dump_disk_status.py
test/unit/elastic_class/ElasticStatus_get_gen_status.py
test/unit/elastic_class/ElasticStatus_get_mem_status.py
test/unit/elastic_class/ElasticStatus_get_nodes.py
test/unit/elastic_class/ElasticStatus_get_node_status.py
test/unit/elastic_class/ElasticStatus_get_shrd_status.py
test/unit/elastic_class/ElasticStatus_get_svr_status.py
test/unit/elastic_class/ElasticStatus_init.py
