#!/bin/bash
# Unit testing program for the elastic_libs.py module.
# This will run all the units tests for this program.
# Will need to run this from the base directory where the module file
#   is located at.

echo ""
echo "Unit test:  get_latest_dump"
test/unit/elastic_libs/get_latest_dump.py

echo ""
echo "Unit test:  list_dumps"
test/unit/elastic_libs/list_dumps.py

echo ""
echo "Unit test:  list_repos2"
test/unit/elastic_libs/list_repos2.py

