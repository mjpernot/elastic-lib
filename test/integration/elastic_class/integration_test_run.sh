#!/bin/bash
# Integration testing program for the elastic_class.py class file.
# This will run all the integrations tests for this program.
# Will need to run this from the base directory where the program file
#   is located at.

echo ""
echo "Integration test:  elastic_class"
test/integration/elastic_class/elastic_search.py
test/integration/elastic_class/elasticsearchdump.py
test/integration/elastic_class/elasticsearchdump_dumpdb.py
test/integration/elastic_class/elasticsearchrepo.py
test/integration/elastic_class/elasticsearchrepo_createrepo.py
test/integration/elastic_class/elasticsearchrepo_deleterepo.py
test/integration/elastic_class/elasticsearchrepo_deletedump.py
test/integration/elastic_class/elasticsearchrepo_deletedumpall.py

