# Python project that contains common libraries and classes for Elasticsearch database/cluster.
# Classification (U)

# Description:
  Consists of a number of Python files that are common function libraries and classes for connecting to and operating in a Elasticsearch database/cluster system.  These programs are not standalone programs, but are installed in another project to support those programs.


### This README file is broken down into the following sections:
  *  Prerequisites
  *  Installation
  *  Testing
     - Unit
     - Integration


# Prerequisites:
  * List of Linux packages that need to be installed on the server.
    - git
    - python-pip

  * Local class/library dependencies within the program structure.
    - elastic-lib
    - python-lib


# Installation
  * From here on out, any reference to **{Python_Project}** or **PYTHON_PROJECT** replace with the baseline path of the python program.
  * Replace any reference to **{Other_Python_Project}** with the baseline path of another python program.
  * There are two types of installs: pip and git.

### Pip Installation:

###### Create requirements file in another program's project to install elastic-lib as a library module.

Create requirements-elastic-lib.txt and requirements-python-lib.txt files:

```
cd {Python_Project}
cp requirements-elastic-lib.txt {Other_Python_Project}/requirements-elastic-lib.txt
cp requirements-python-lib.txt {Other_Python_Project}/requirements-python-lib.txt
```

##### Modify the other program's README.md file to add the pip commands under the "Install supporting classes and libraries" section.

Modify the {Other_Python_Project}/README.md file and add the following line:

```
pip install -r requirements-elastic-lib.txt --target elastic_lib --trusted-host pypi.appdev.proj.coe.ic.gov
pip install -r requirements-python-lib.txt --target elastic_lib/lib --trusted-host pypi.appdev.proj.coe.ic.gov
```

##### Add the general elastic-lib requirements to the other program's requirements.txt file.  Remove any duplicates.

Modify the {Other_Python_Project}/requirements.txt file and add the following line:

```
elasticsearch>=7.0.0,<8.0.0
urllib3==1.24.3
```

### Git Installation:

Install general Elastic libraries and classes using git.

```
cd {Python_Project}
git clone git@sc.appdev.proj.coe.ic.gov:JAC-DSXD/elastic-lib.git
```

Install/upgrade system modules.

```
sudo bash
umask 022
pip install -r requirements.txt --upgrade --trusted-host pypi.appdev.proj.coe.ic.gov
exit
```

Install supporting classes and libraries

```
cd elastic-lib
pip install -r requirements-python-lib.txt --target lib --trusted-host pypi.appdev.proj.coe.ic.gov
```


# Testing

# Unit Testing:

### Installation:

Install the project using the procedures in the Git Installation section.

### Testing:

```
cd {Python_Project}/elastic-lib
test/unit/elastic_libs/unit_test_run.sh
test/unit/elastic_class/unit_test_run.sh
```

### Code coverage:

```
cd {Python_Project}/elastic-lib
test/unit/elastic_libs/code_coverage.sh
test/unit/elastic_class/code_coverage.sh
```


# Integration Testing:

NOTES:
  * These tests need to run as the same user who is running the elasticsearch database, normally the elasticsearch user.
  * These tests require that the Elasticsearch database/cluster do not have any created repositories, otherwise the tests will be skipped.  
  * The path.repo needs to be set in the elasticsearch.yml file to register a path for any repositories to be created.

### Installation:

Install the project using the procedures in the Git Installation section.

### Configuration:

Create Elasticsearch configuration file.

```
cd test/integration/elastic_class/config
cp elastic.py.TEMPLATE elastic.py
```

Make the appropriate changes to the Elasticsearch environment.
  * Change these entries in the elastic.py file:
    - host = ["HOST_NAME1", "HOST_NAME2"]
    - log_repo_dir = "LOGICAL_DIR_PATH"
    - phy_repo_dir = "PHYSICAL_DIR_PATH"
  * **LOGICAL_DIR_PATH** is the logical directory path to the share file system.
  * **phy_repo_dir** is the physical directory path to the share file system.
    - See the path.repo entry in the elasticsearch.yml for log_repo_dir and phy_repo_dir values.

```
vim elastic.py
chmod 600 elastic.py
sudo chown elasticsearch:elasticsearch elastic.py
```

### Testing:

```
cd {Python_Project}/elastic_lib
test/integration/elastic_class/integration_test_run.sh
```

### Code coverage:

```
cd {Python_Project}/elastic_lib
test/integration/elastic_class/code_coverage.sh
```

