# Python project that contains common libraries and classes for Elasticsearch database/cluster.
# Classification (U)

# Description:
  Consists of a number of Python files that are common function libraries and classes for connecting to and operating in a Elasticsearch database/cluster system.  These programs are not standalone programs, but are installed in another project to support those programs.


### This README file is broken down into the following sections:
  *  Installation
     - Pip Installation
  *  Testing
     - Git Installation
     - Unit
     - Integration


# Installation
  * From here on out, any reference to **{Python_Project}** or **PYTHON_PROJECT** replace with the baseline path of the python program.

### Pip Installation:

###### Create requirements file in another program's project to install elastic-lib as a library module.

  * Create requirements-elastic-lib.txt and requirements-elastic-python-lib.txt files.  Replace N.N.N with the version of the library needed.

```
echo 'git+ssh://git@sc.appdev.proj.coe.ic.gov/JAC-DSXD/elastic-lib.git@N.N.N#egg=mysql-lib' > requirements-elastic-lib.txt
echo 'git+ssh://git@sc.appdev.proj.coe.ic.gov/JAC-DSXD/python-lib.git@N.N.N#egg=python-lib' > requirements-elastic-python-lib.txt
```

##### Modify the other program's README.md file to add the pip commands under the "Install supporting classes and libraries" section.

Centos 7 (Running Python 2.7):
Modify the README.md file and the following lines to install the library modules:

```
pip install -r requirements-elastic-lib.txt --target elastic_lib --trusted-host pypi.appdev.proj.coe.ic.gov
pip install -r requirements-elastic-python-lib.txt --target elastic_lib/lib --trusted-host pypi.appdev.proj.coe.ic.gov
```

Redhat 8 (Running Python 3.6):
Modify the README.md file and the following lines to install the library modules:

```
python -m pip install -r requirements-elastic-lib.txt --target elastic_lib --trusted-host pypi.appdev.proj.coe.ic.gov
python -m pip install -r requirements-elastic-python-lib.txt --target elastic_lib/lib --trusted-host pypi.appdev.proj.coe.ic.gov
```

##### Add the general elastic-lib requirements to the other program's requirements.txt file.  Remove any duplicates.

Centos 7 (Running Python 2.7):
requirements.txt

Redhat 8 (Running Python 3.6):
requirements3.txt

# Testing

### Git Installation:

Install general Elastic libraries and classes using git.

```
git clone git@sc.appdev.proj.coe.ic.gov:JAC-DSXD/elastic-lib.git
cd elastic-lib
```

Install/upgrade system modules.

Centos 7 (Running Python 2.7):
```
sudo pip install -r requirements.txt --upgrade --trusted-host pypi.appdev.proj.coe.ic.gov
```

Redhat 8 (Running Python 3.6):
NOTE: Install as the user that will use the package.

```
python -m pip install --user -r requirements.txt --upgrade --trusted-host pypi.appdev.proj.coe.ic.gov
```


Install supporting classes and libraries

Centos 7 (Running Python 2.7):
```
pip install -r requirements-python-lib.txt --target lib --trusted-host pypi.appdev.proj.coe.ic.gov
```

Redhat 8 (Running Python 3.6):

```
python -m pip install -r requirements-python-lib.txt --target lib --trusted-host pypi.appdev.proj.coe.ic.gov
```

# Unit Testing:

### Installation:

Install the project using the procedures in the Git Installation section.

### Testing:

```
test/unit/elastic_libs/unit_test_run3.sh
test/unit/elastic_class/unit_test_run3.sh
```

### Code coverage:

```
test/unit/elastic_libs/code_coverage.sh
test/unit/elastic_class/code_coverage.sh
```


# Integration Testing:

NOTES:
  * For several of the tests to work the Elasticsearch needs to have xpack.security.enabled set to true.
  * These tests need to run as the same user who is running the elasticsearch database, normally the elasticsearch user.
  * These tests require that the Elasticsearch database/cluster do not have any created repositories, otherwise the tests will be skipped.  
  * The path.repo needs to be set in the elasticsearch.yml file to register a path for any repositories to be created.

### Installation:

Install the project using the procedures in the Git Installation section.

### Configuration:

Create Elasticsearch configuration file.

```
cp elastic.py test/integration/elastic_class/config/elastic.py
vim test/integration/elastic_class/config/elastic.py
chmod 600 test/integration/elastic_class/config/elastic.py
```

Add the following lines to the end of the file:
```
# Name of the test repository directory path
# Must be a shared mount between all Elasticsearch databases in the cluster.
# NOTE:  If running ElasticSearch as Docker setup, then these paths will be different.  If running as a standard setup, they will be the same.
# Logical base repository directory.
log_repo_dir = "LOGICAL_DIR_PATH"
# Physical base repository directory.
phy_repo_dir = "PHYSICAL_DIR_PATH"
```

Make the appropriate changes to the Elasticsearch environment.
  * Change these entries in the elastic.py file:
    - host = ["https://HOST_NAME1:9200", "https://HOST_NAME2:9200"]
    - log_repo_dir = "LOGICAL_DIR_PATH"
    - phy_repo_dir = "PHYSICAL_DIR_PATH"
  * **LOGICAL_DIR_PATH** is the logical directory path to the share file system.
  * **phy_repo_dir** is the physical directory path to the share file system.
    - See the path.repo entry in the elasticsearch.yml for log_repo_dir and phy_repo_dir values.


### Testing:

```
test/integration/elastic_class/integration_test_run3.sh
```

### Code coverage:

```
test/integration/elastic_class/code_coverage.sh
```

