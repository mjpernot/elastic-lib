#!/bin/bash
# Integration testing program for the elastic_class.py class file.
# This will run all the integrations tests for this program.
# Will need to run this from the base directory where the program file
#   is located at.

echo ""
echo "Integration test:  ElasticSearch"
test/integration/elastic_class/elastic_search.py

echo ""
echo "Integration test:  ElasticSearchDump"
test/integration/elastic_class/elasticsearchdump.py

echo ""
echo "Integration test:  ElasticSearchDump.dump_db"
test/integration/elastic_class/elasticsearchdump_dumpdb.py

echo ""
echo "Integration test:  ElasticSearchRepo"
test/integration/elastic_class/elasticsearchrepo.py

echo ""
echo "Integration test:  ElasticSearchRepo.create_repo"
test/integration/elastic_class/elasticsearchrepo_createrepo.py

echo ""
echo "Integration test:  ElasticSearchRepo.delete_repo"
test/integration/elastic_class/elasticsearchrepo_deleterepo.py

echo ""
echo "Integration test:  ElasticSearchRepo.delete_dump"
test/integration/elastic_class/elasticsearchrepo_deletedump.py

echo ""
echo "Integration test:  ElasticSearchRepo.delete_dump_all"
test/integration/elastic_class/elasticsearchrepo_deletedumpall.py

