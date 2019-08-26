#!/bin/bash
# Unit testing program for the elastic_libs.py module.
# This will run all the units tests for this program.
# Will need to run this from the base directory where the module file
#   is located at.

echo ""
echo "Unit test:  elastic_libs"
test/unit/elastic_libs/get_latest_dump.py
test/unit/elastic_libs/list_dumps.py
test/unit/elastic_libs/list_repos2.py

