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
    - elastic_libs
    - lib/gen_libs


# Installation
  There are two types of installs: pip and git.

### Pip Installation:
  * Replace **{Other_Python_Project}** with the baseline path of another python program.

###### Create requirements file in another program's project to install elastic-lib as a library module.

Create requirements-elastic-lib.txt file:
```
vim {Other_Python_Project}/requirements-elastic-lib.txt
```

Add the following lines to the requirements-elastic-lib.txt file:
```
git+ssh://git@sc.appdev.proj.coe.ic.gov/JAC-DSXD/elastic-lib.git#egg=elastic-lib
```

Create requirements-python-lib.txt file:
```
vim {Other_Python_Project}/requirements-python-lib.txt
```

Add the following lines to the requirements-python-lib.txt file:
```
git+ssh://git@sc.appdev.proj.coe.ic.gov/JAC-DSXD/python-lib.git#egg=python-lib
```

##### Modify the other program's README.md file to add the pip commands under the "Install supporting classes and libraries" section.

Modify the README.md file:
```
vim {Other_Python_Project}/README.md
```

Add the following lines under the "Install supporting classes and libraries" section.
```
pip install -r requirements-elastic-lib.txt --target elastic_lib --trusted-host pypi.appdev.proj.coe.ic.gov
pip install -r requirements-python-lib.txt --target elastic_lib/lib --trusted-host pypi.appdev.proj.coe.ic.gov
```

##### Add the general elastic-lib requirements to the other program's requirements.txt file.  Remove any duplicates.

Modify the requirements.txt file:
```
vim {Other_Python_Project}/requirements.txt
```

Add the following lines to the requirements.txt file:
```
elasticsearch>=7.0.0,<8.0.0
urllib3==1.24.3
```

### Git Installation:

Install general Elastic libraries and classes using git.
  * Replace **{Python_Project}** with the baseline path of the python program.

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

Install general Elastic libraries and classes using git.
  * Replace **{Python_Project}** with the baseline path of the python program.
  * Replace **{Branch_Name}** with the name of the Git branch being tested.  See Git Merge Request.

```
cd {Python_Project}
git clone --branch {Branch_Name} git@sc.appdev.proj.coe.ic.gov:JAC-DSXD/elastic-lib.git
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
  * NOTE:  **BASE_REPO_DIRECTORY** is a directory path to a shared file system by all Elasticsearch databases in the cluster.

```
vim elastic.py
chmod 600 elastic.py
sudo chown elasticsearch:elasticsearch elastic.py
```

### Testing:
  * These tests must be run as the elasticsearch account:
  * Replace **{Python_Project}** with the baseline path of the python program.

```
cd {Python_Project}/elastic_lib
test/integration/elastic_class/integration_test_run.sh
```

### Code coverage:

```
cd {Python_Project}/elastic_lib
test/integration/elastic_class/code_coverage.sh
```

