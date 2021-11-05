#!/bin/bash
# Unit test code coverage for elastic_class.py module.
# This will run the Python code coverage module against all integration test modules.
# This will show the amount of code that was tested and which lines of code
#	that was skipped during the test.

coverage erase

echo ""
echo "Running unit test modules in conjunction with coverage"
coverage run -a --source=elastic_class test/integration/elastic_class/elasticsearch_init.py
coverage run -a --source=elastic_class test/integration/elastic_class/elasticsearch_connect.py
coverage run -a --source=elastic_class test/integration/elastic_class/elasticsearch_update.py
coverage run -a --source=elastic_class test/integration/elastic_class/elasticsearchdump.py
coverage run -a --source=elastic_class test/integration/elastic_class/elasticsearchdump_connect.py
coverage run -a --source=elastic_class test/integration/elastic_class/elasticsearchdump_dumpdb.py
coverage run -a --source=elastic_class test/integration/elastic_class/elasticsearchdump_update_dump_status.py
coverage run -a --source=elastic_class test/integration/elastic_class/elasticsearchrepo.py
coverage run -a --source=elastic_class test/integration/elastic_class/elasticsearchrepo_connect.py
coverage run -a --source=elastic_class test/integration/elastic_class/elasticsearchrepo_createrepo.py
coverage run -a --source=elastic_class test/integration/elastic_class/elasticsearchrepo_deleterepo.py
coverage run -a --source=elastic_class test/integration/elastic_class/elasticsearchrepo_deletedump.py
coverage run -a --source=elastic_class test/integration/elastic_class/elasticsearchrepo_deletedumpall.py
coverage run -a --source=elastic_class test/integration/elastic_class/elasticsearchrepo_update_repo_status.py
coverage run -a --source=elastic_class test/integration/elastic_class/elasticsearchstatus.py
coverage run -a --source=elastic_class test/integration/elastic_class/elasticsearchstatus_connect.py

echo ""
echo "Producing code coverage report"
coverage combine
coverage report -m
