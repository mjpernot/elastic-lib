# Python project that contains common libraries and classes for Elasticsearch database/cluster.
# Classification (U)

# Description:
  This project consists of a number of Python files that are common function libraries and classes for connecting to and operating in a Elasticsearch database/cluster system.  These programs are not standalone programs, but are installed in another project to support those programs.


### This README file is broken down into the following sections:
  *  Prerequisites
  *  Installation
  *  Program Descriptions
  *  Testing
     - Unit
     - Integration


# Prerequisites:
  * List of Linux packages that need to be installed on the server.
    - python-libs
    - python-devel
    - git
    - python-pip

  * Local class/library dependencies within the program structure.
    - requests_lib/requests_libs
    - elastic_libs
    - lib/gen_libs


# Installation
  There are two types of installs: pip and git.  Pip will only install the program modules and classes, whereas git will install all modules and classes including testing programs along with README and CHANGELOG files.  The Pip installation will be modifying another program's project to install these supporting librarues via pip.

### Pip Installation:
  * Replace **{Python_Project}** with the baseline path of the python program.
  * Replace **{Other_Python_Project}** with the baseline path of another python program.

Create requirement files for the supporting library in another program's project.

```
cd {Python_Project}
cat requirements-elastic-lib.txt >> {Other_Python_Project}/requirements-elastic-lib.txt
cat requirements-requests-lib.txt >> {Other_Python_Project}/requirements-requests-lib.txt
cat requirements-python-lib.txt >> {Other_Python_Project}/requirements-python-lib.txt
```

Place the following commands into the another program's README.md file under the "Install supporting classes and libraries" section.
   pip install -r requirements-elastic-lib.txt --target elastic_lib --trusted-host pypi.appdev.proj.coe.ic.gov
   pip install -r requirements-requests-lib.txt --target elastic_lib/requests_lib --trusted-host pypi.appdev.proj.coe.ic.gov
   pip install -r requirements-python-lib.txt --target elastic_lib/lib --trusted-host pypi.appdev.proj.coe.ic.gov

```
vim {Other_Python_Project}/README.md
```

Add the system module requirements to the another program's requirements.txt file and remove any duplicates.

``
cat requirements.txt >> {Other_Python_Project}/requirements.txt
vim {Other_Python_Project}/requirements.txt
```

### Git Installation:

Install general Elastic libraries and classes using git.
  * Replace **{Python_Project}** with the baseline path of the python program.

```
cd {Python_Project}
git clone git@sc.appdev.proj.coe.ic.gov:JAC-DSXD/elastic-lib.git
```

Install supporting classes and libraries

```
cd elastic-lib
pip install -r requirements-python-lib.txt --target lib --trusted-host pypi.appdev.proj.coe.ic.gov
pip install -r requirements-requests-lib.txt --target requests_lib --trusted-host pypi.appdev.proj.coe.ic.gov
```

Install/upgrade system modules.

```
sudo bash
umask 022
pip install -r requirements.txt --upgrade --trusted-host pypi.appdev.proj.coe.ic.gov
exit
```


# Program Descriptions:
### Program:  elastic_class.py
##### Description:   Class definitions and methods for connecting to Elasticsearch database system.
##### Classes:
  * ElasticSearch => Class which is a representation of an ElasticSearch database/cluster.  An ElasticSearch object is used as proxy to implement the connecting to an execute commands in an ElasticSearch database/cluster.
  * ElasticSearchDump => Class which is a representation of ElasticSearch database dump.  An ElasticSearchDump object is used as proxy to implement a database dump of an ElasticSearch database/cluster.
  * ElasticSearchRepo => Class which is a representation of ElasticSearchRepo repositories.  An ElasticSearchRepo object is used as proxy to implement respositories within an Elasticsearch cluster.
  * (Deprecated)  Elastic => Class which is a representation of an Elasticsearch database node.  An Elastic object is used as proxy to implement the connecting to an execute commands in an Elasticsearch database node.
  * ElasticCluster => Class which is a representation of a cluster of Elasticsearch database nodes.  An ElasticCluster object is used as a proxy to implement connecting to an Elasticsearch database cluster.
  * (Deprecated)  ElasticDump => Class which is a representation of Elasticsearch database dump.  An ElasticDump object is used as proxy to implement a database dump of an Elasticsearch database node.
  * ElasticStatus => Class which is a representation of an Elasticsearch cluster status which contains attributes to show the general health of the Elasticsearch cluster.  An ElasticStatus is used as a proxy to implement connecting to an Elasticsearch database cluster and executing status commands.

### Program: elastic_lib.py
##### Description: Library of function calls for a Elasticsearch database/cluster system.


# Testing

# Unit Testing:

### Description: Testing consists of unit testing for the functions in the library modules and methods in the classes.

### Installation:

Install general Elastic libraries and classes using git.
  * Replace **{Python_Project}** with the baseline path of the python program.
  * Replace **{Branch_Name}** with the name of the Git branch being tested.  See Git Merge Request.

```
cd {Python_Project}
git clone --branch {Branch_Name} git@sc.appdev.proj.coe.ic.gov:JAC-DSXD/elastic-lib.git
```

Install supporting classes and libraries

```
cd elastic-lib
pip install -r requirements-python-lib.txt --target lib --trusted-host pypi.appdev.proj.coe.ic.gov
pip install -r requirements-requests-lib.txt --target requests_lib --trusted-host pypi.appdev.proj.coe.ic.gov
```

Install/upgrade system modules.

```
sudo bash
umask 022
pip install -r requirements.txt --upgrade --trusted-host pypi.appdev.proj.coe.ic.gov
exit
```

# Unit test runs for elastic_libs.py:

```
test/unit/elastic_libs/get_latest_dump.py
test/unit/elastic_libs/list_dumps.py
test/unit/elastic_libs/list_repos2.py
```

### All unit testing for elastic_lib.py

```
test/unit/elastic_libs/unit_test_run.sh
```

### Code coverage program

```
test/unit/elastic_libs/code_coverage.sh
```

# Unit test runs for elastic_libs.py:

```
test/unit/elastic_class/ElasticSearch_init.py
test/unit/elastic_class/ElasticSearchDump_init.py
test/unit/elastic_class/ElasticSearchDump_dump_db.py
test/unit/elastic_class/ElasticSearchRepo_create_repo.py
test/unit/elastic_class/ElasticSearchRepo_delete_repo.py
test/unit/elastic_class/ElasticSearchRepo_init.py
```

### All unit testing for elastic_class.py

```
test/unit/elastic_class/unit_test_run.sh
```

### Code coverage program

```
test/unit/elastic_class/code_coverage.sh
```


# Unit tests runs for elastic_class.py:
### NOTE:  Due to the inability to mock Elasticsearch connections in Python 2.6, there are no unit tests for this class.  All unit tests for elastic_class.py will be conducted in the Integration test section.


# Integration Testing:

### Description: Testing consists of integration testing of methods in elastic_class.py.

NOTE:  These tests require that the Elasticsearch database/cluster do not have any repositories setup, otherwise the tests will be skipped.

### Installation:
  * Replace **{Python_Project}** with the baseline path of the python program.
  * Replace **{Branch_Name}** with the name of the Git branch being tested.  See Git Merge Request.

Install these programs using git.

```
umask 022
cd {Python_Project}
git clone --branch {Branch_Name} git@sc.appdev.proj.coe.ic.gov:JAC-DSXD/elastic-lib.git
```

Install supporting classes and libraries

```
cd elastic-lib
pip install -r requirements-python-lib.txt --target lib --trusted-host pypi.appdev.proj.coe.ic.gov
pip install -r requirements-requests-lib.txt --target requests_lib --trusted-host pypi.appdev.proj.coe.ic.gov
```

Install/upgrade system modules.

```
sudo bash
umask 022
pip install -r requirements.txt --upgrade --trusted-host pypi.appdev.proj.coe.ic.gov
exit
```

### Configuration:

Create Elasticsearch configuration file.

```
cd test/integration/elastic_class/config
cp elastic.py.TEMPLATE elastic.py
```

Make the appropriate changes to the Elasticsearch environment.
  * Change these entries in the elastic.py file:
    - host = ["HOST_NAME1", "HOST_NAME2"]
    - repo_dir = "BASE_REPO_DIRECTORY/"
  * NOTE:  **REPO_DIRECTORY_PATH** is a directory path to a shared file system by all Elasticsearch databases in the cluster.

```
vim elastic.py
chmod 600 elastic.py
sudo chown elasticsearch:elasticsearch elastic.py
```

# Integration test runs for elastic_class.py:
  * These tests must be run as the elasticsearch account:
  * Replace **{Python_Project}** with the baseline path of the python program.

```
sudo bash
su - elasticsearch
cd {Python_Project}/elastic_lib
```

### Integration:  ElasticSearch class

```
test/integration/elastic_class/elastic_search.py
```

### Integration:  ElasticSearchDump class

```
test/integration/elastic_class/elasticsearchdump.py
```

### Integration:  ElasticSearchDump.dump_db method

```
test/integration/elastic_class/elasticsearchdump_dumpdb.py
```

### Integration:  ElasticSearchRepo class

```
test/integration/elastic_class/elasticsearchrepo.py
```

### Integration:  ElasticSearchRepo.create_repo method

```
test/integration/elastic_class/elasticsearchrepo_createrepo.py
```

### Integration:  ElasticSearchRepo.delete_repo method

```
test/integration/elastic_class/elasticsearchrepo_deleterepo.py
```

### Integration:  ElasticSearchRepo.delete_dump method

```
test/integration/elastic_class/elasticsearchrepo_deletedump.py
```

### Integration:  ElasticSearchRepo.delete_dump_all method

```
test/integration/elastic_class/elasticsearchrepo_deletedumpall.py
```

### All integration testing

```
test/integration/elastic_class/integration_test_run.sh
```

### Code coverage program

```
test/integration/elastic_class/code_coverage.sh
```

