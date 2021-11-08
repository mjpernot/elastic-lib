#!/bin/bash
# Integration testing program for the elastic_class.py class file.
# This will run all the integrations tests for this program.
# Will need to run this from the base directory where the program file
#   is located at.

echo ""
echo "Integration test:  elastic_class"
test/integration/elastic_class/elasticsearch_init.py
test/integration/elastic_class/elasticsearch_connect.py
test/integration/elastic_class/elasticsearch_update.py
test/integration/elastic_class/elasticsearchdump.py
test/integration/elastic_class/elasticsearchdump_connect.py
test/integration/elastic_class/elasticsearchdump_dumpdb.py
test/integration/elastic_class/elasticsearchdump_update_dump_status.py
test/integration/elastic_class/elasticsearchrepo.py
test/integration/elastic_class/elasticsearchrepo_connect.py
test/integration/elastic_class/elasticsearchrepo_createrepo.py
test/integration/elastic_class/elasticsearchrepo_deleterepo.py
test/integration/elastic_class/elasticsearchrepo_deletedump.py
test/integration/elastic_class/elasticsearchrepo_deletedumpall.py
test/integration/elastic_class/elasticsearchrepo_update_repo_status.py
test/integration/elastic_class/elasticsearchstatus.py
test/integration/elastic_class/elasticsearchstatus_connect.py
test/integration/elastic_class/elasticsearchstatus_get_cluster.py
test/integration/elastic_class/elasticsearchstatus_get_gen_status.py
test/integration/elastic_class/elasticsearchstatus_get_mem_status.py
test/integration/elastic_class/elasticsearchstatus_get_nodes.py
test/integration/elastic_class/elasticsearchstatus_get_node_status.py
test/integration/elastic_class/elasticsearchstatus_get_shrd_status.py
test/integration/elastic_class/elasticsearchstatus_get_svr_status.py
test/integration/elastic_class/elasticsearchstatus_update_status2.py

