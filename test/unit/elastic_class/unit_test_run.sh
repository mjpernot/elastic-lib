#!/bin/bash
# Unit testing program for the elastic_class module.
# This will run all the units tests for this program.
# Will need to run this from the base directory where the module file
#   is located at.

echo ""
echo "Unit test:  elastic_class"
test/unit/elastic_class/Elastic_init.py
test/unit/elastic_class/ElasticCluster_init.py
test/unit/elastic_class/ElasticSearch_init.py
test/unit/elastic_class/ElasticSearchDump_chk_status.py
test/unit/elastic_class/ElasticSearchDump_init.py
test/unit/elastic_class/ElasticSearchDump_dump_db.py
test/unit/elastic_class/ElasticSearchRepo_create_repo.py
test/unit/elastic_class/ElasticSearchRepo_delete_dump.py
test/unit/elastic_class/ElasticSearchRepo_delete_dump_all.py
test/unit/elastic_class/ElasticSearchRepo_delete_repo.py
test/unit/elastic_class/ElasticSearchRepo_init.py
test/unit/elastic_class/ElasticStatus_get_cluster.py
test/unit/elastic_class/ElasticStatus_get_disk_status.py
test/unit/elastic_class/ElasticStatus_get_dump_disk_status.py
test/unit/elastic_class/ElasticStatus_get_gen_status.py
test/unit/elastic_class/ElasticStatus_init.py
