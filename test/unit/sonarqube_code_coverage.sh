#!/bin/bash
# Unit test code coverage for SonarQube to cover all modules.
# This will run the Python code coverage module against all unit test modules.
# This will show the amount of code that was tested and which lines of code
#	that was skipped during the test.

coverage erase

echo ""
echo "Running unit test modules in conjunction with coverage"
coverage run -a --source=elastic_class test/unit/elastic_class/ElasticSearch_init.py
coverage run -a --source=elastic_class test/unit/elastic_class/ElasticSearchDump_init.py
coverage run -a --source=elastic_class test/unit/elastic_class/ElasticSearchDump_dump_db.py
coverage run -a --source=elastic_class test/unit/elastic_class/ElasticSearchRepo_create_repo.py
coverage run -a --source=elastic_class test/unit/elastic_class/ElasticSearchRepo_delete_dump.py
coverage run -a --source=elastic_class test/unit/elastic_class/ElasticSearchRepo_delete_dump_all.py
coverage run -a --source=elastic_class test/unit/elastic_class/ElasticSearchRepo_delete_repo.py
coverage run -a --source=elastic_class test/unit/elastic_class/ElasticSearchRepo_init.py
coverage run -a --source=elastic_libs test/unit/elastic_libs/list_repos2.py
coverage run -a --source=elastic_libs test/unit/elastic_libs/list_dumps.py
coverage run -a --source=elastic_libs test/unit/elastic_libs/get_latest_dump.py

echo ""
echo "Producing code coverage report"
coverage combine
coverage report -m
coverage xml -i

