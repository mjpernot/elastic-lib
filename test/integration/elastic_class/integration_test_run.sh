#!/bin/bash
# Integration testing program for the elastic_class.py class file.
# This will run all the integrations tests for this program.
# Will need to run this from the base directory where the program file
#   is located at.

echo ""
echo "Integration test:  elastic_class"
/usr/bin/python test/integration/elastic_class/elasticsearch_init.py
/usr/bin/python test/integration/elastic_class/elasticsearch_connect.py
/usr/bin/python test/integration/elastic_class/elasticsearch_update.py
/usr/bin/python test/integration/elastic_class/elasticsearchdump.py
/usr/bin/python test/integration/elastic_class/elasticsearchdump_connect.py
/usr/bin/python test/integration/elastic_class/elasticsearchdump_dumpdb.py
/usr/bin/python test/integration/elastic_class/elasticsearchdump_update_dump_status.py
/usr/bin/python test/integration/elastic_class/elasticsearchrepo.py
/usr/bin/python test/integration/elastic_class/elasticsearchrepo_connect.py
/usr/bin/python test/integration/elastic_class/elasticsearchrepo_createrepo.py
/usr/bin/python test/integration/elastic_class/elasticsearchrepo_deleterepo.py
/usr/bin/python test/integration/elastic_class/elasticsearchrepo_deletedump.py
/usr/bin/python test/integration/elastic_class/elasticsearchrepo_deletedumpall.py
/usr/bin/python test/integration/elastic_class/elasticsearchrepo_update_repo_status.py
/usr/bin/python test/integration/elastic_class/elasticsearchstatus.py
/usr/bin/python test/integration/elastic_class/elasticsearchstatus_chk_all.py
/usr/bin/python test/integration/elastic_class/elasticsearchstatus_chk_disk.py
/usr/bin/python test/integration/elastic_class/elasticsearchstatus_chk_mem.py
/usr/bin/python test/integration/elastic_class/elasticsearchstatus_chk_nodes.py
/usr/bin/python test/integration/elastic_class/elasticsearchstatus_chk_server.py
/usr/bin/python test/integration/elastic_class/elasticsearchstatus_chk_shards.py
/usr/bin/python test/integration/elastic_class/elasticsearchstatus_chk_status.py
/usr/bin/python test/integration/elastic_class/elasticsearchstatus_connect.py
/usr/bin/python test/integration/elastic_class/elasticsearchstatus_get_all.py
/usr/bin/python test/integration/elastic_class/elasticsearchstatus_get_cluster.py
/usr/bin/python test/integration/elastic_class/elasticsearchstatus_get_disk_status.py
/usr/bin/python test/integration/elastic_class/elasticsearchstatus_get_dump_disk_status.py
/usr/bin/python test/integration/elastic_class/elasticsearchstatus_get_gen_status.py
/usr/bin/python test/integration/elastic_class/elasticsearchstatus_get_mem_status.py
/usr/bin/python test/integration/elastic_class/elasticsearchstatus_get_nodes.py
/usr/bin/python test/integration/elastic_class/elasticsearchstatus_get_node_status.py
/usr/bin/python test/integration/elastic_class/elasticsearchstatus_get_shrd_status.py
/usr/bin/python test/integration/elastic_class/elasticsearchstatus_get_svr_status.py
/usr/bin/python test/integration/elastic_class/elasticsearchstatus_update_status2.py

