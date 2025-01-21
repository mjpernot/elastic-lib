# Changelog
All notable changes to this project will be documented in this file.

The format is based on "Keep a Changelog".  This project adheres to Semantic Versioning.


## [4.0.8] - 2025-01-21
- Updated certifi==2024.12.14
- Updated urllib3==1.26.20
- Downgraded elasticsearch==7.17.9
- Updated python-lib==4.0.0

### Fixed
- Downgraded elasticsearch library from 8.11.1 to 7.17.19

### Changed
- Documentation changes.

### Deprecated
- Support for Elasticsearch v7.4, v7.12 and v7.17


## [4.0.7] - 2024-11-18
- Updated python-lib to v3.0.8

### Fixed
- Set chardet==3.0.4 for Python 3.

### Deprecated
- Support for Python 2.7


## [4.0.6] - 2024-11-05
- Updated certifi==2024.6.2 for Python 3.
- Updated chardet==4.0.0 for Python 3.
- Updated distro==1.9.0 for Python 3.
- Updated idna==2.10 for Python 3.
- Updated urllib3==1.26.19 for Python 3.
- Updated requests==2.25.0 for Python 3.
- Added elastic-transport==8.10.0 for Python 3.
- Updated elasticsearch==8.11.1 for Python 3.
- Updated python-lib to v3.0.7


## [4.0.5] - 2024-09-27
- Updated simplejson==3.13.2 for Python 3
- Updated python-lib to v3.0.5


## [4.0.4] - 2024-08-07
- Updated simplejson==3.13.2
- Updated requests==2.25.0
- Added idna==2.10
- Removed email==4.0.3

### Changed
- Updates to requirements.txt.


## [4.0.3] - 2024-07-30
- Set urllib3 to 1.26.19 for Python 2 for security reasons.

### Added
- elastic.py - Template Elasticsearch configuration file.


## [4.0.2] - 2024-02-29
- Updated to work in Red Hat 8
- Updated python-lib to v3.0.3

### Changed
- set elasticsearch to 7.17.9 for Python.
- Set simplejson to 3.12.0 for Python 3.
- Set chardet to 3.0.4 for Python 2.
- Documentation updates.


## [4.0.1] - 2022-12-21
- Updated to work in Python 3 too
- Upgraded python-lib to v2.9.4

### Changed
- requirements.txt: Added requests==2.6.0 and certifi==2019.11.28.
- Converted imports to use Python 2.7 or Python 3.
- elastic_class.ElasticSearchDump.update_dump_status: Converted dictionary keys() call to list.


## [4.0.0] - 2022-02-17
Breaking Change
- Updated to work in Elasticsearch 7.17.0

### Fixed
- elastic_class.ElasticSearchStatus.chk_disk: Ignore UNASSIGNED disk and check for cutoff disk argument if set to zero.
- elastic_class.get_shards: Changed the output format of cat.shards from string to JSON.
- elastic_class.get_master_name: Changed the output format of cat.master from string to JSON.
- elastic_class.get_disks:  Changed the output format of cat.allocation from string to JSON.
- elastic_class.get_dump_list:  Changed cat.snapshot to snapshot.get call.  Returns a list of dumps, but each dump is in JSON format instead of a string.

### Changed
- elastic_libs.list_dumps:  Changed to handle dictionary format, added raw data print option, and changed formating of print.
- elastic_class.ElasticDumpStatus.get_disk_status, elastic_class.ElasticDumpStatus.chk_disk, elastic_class.ElasticDumpStatus.chk_shards:  Changed processing from a list to a dictionary format.
- elastic_libs.get_latest_dump, elastic_class.ElasticSearchDump.\_chk_status:  Changed the processing of dumps from lists to dictionaries.
- elastic_class.ElasticSearchDump.update_dump_status, elastic_class.ElasticSearchDump.delete_dump_all, elastic_class.ElasticSearchDump.delete_dump, elastic_class.ElasticSearchDump.dump_db:  Handle multiple returned datatypes from get_dump_list call.
- elastic_class.get_dump_list:  Added return status and error message to method.
- Documentation updates.

### Removed
- elastic_class.ElasticSearchDump.\_parse method


## [3.0.1] - 2021-11-24
### Fixed
- elastic_class.ElasticSearchStatus.chk_all:  Set cutoff values to the current instance settings if None is passed for any of them.
- elastic_class.ElasticSearch.\_\_init\_\_:  Allow the "scheme" attribute to be set from passed in arguments.

### Changed
- elastic_class.ElasticSearchStatus.chk_all: Refactored method.
- Documentation updates.


## [3.0.0] - 2021-10-18
Breaking Change

### Added
- elastic_class.ElasticSearch.set_ssl_config:  Set the SSL config attributes.
- elastic_class.ElasticSearch.set_login_config:  Set the login config attributes.
- elastic_class.ElasticSearchStatus.connect:  Connection method for ElasticSearchStatus class.
- elastic_class.ElasticSearchRepo.connect:  Connection method for ElasticSearchRepo class.
- elastic_class.ElasticSearchDump.connect:  Connection method for ElasticSearchDump class.
- elastic_class.ElasticSearch.connect:  Connection method to ElasticSearch server/cluster.

### Changed
- elastic_class.ElasticSearch.connect:  Added config to the connection call.
- elastic_class.ElasticSearch.\_\_init\_\_:  Added SSL and login attributes and set up of SSL and login in config and removed connection and update_status calls.
- elastic_class.ElasticSearchStatus.\_\_init\_\_:  Removed update_status2 call.
- elastic_class.ElasticSearchRepo.\_\_init\_\_:  Removed update_repo_status call.
- elastic_class.ElasticSearchDump.\_\_init\_\_:  Removed update_dump_status call.
- elastic_class.ElasticSearchStatus.update_status2, elastic_class.ElasticSearchRepo.update_repo_status, elastic_class.ElasticSearch.update_status, elastic_class.ElasticSearchDump.update_dump_status:  Removed is_active check and setting of is_connected attribute.
- elastic_libs, elastc_class:  Removed non-required \*\*kwargs entries.
- Documentation updates


## [2.0.3] - 2020-07-10
### Fixed
- elastic_libs.list_dumps:  Fixed formatting error.

### Changed
- elastic_libs.get_latest_dump:  Refactored function and removed multiple returns and else clause.


## [2.0.2] - 2020-06-12
### Fixed
- elastic_class.ElasticSearchStatus.get_disk_status:  Skips any disks that are listed as UNASSIGNED.
- elastic_class.ElasticSearchStatus.chk_disk:  Does not check any disk listed as UNASSIGNED.

### Changed
- elastic_class.ElasticSearch.\_\_init\_\_:  Removed duplication code of setting self.els attribute.
- Changed variable to standard naming convention in many methods.
- elastic_class.ElasticSearchStatus.chk_disk:  Added UsedPercent and Available and clarified four other components.
- elastic_class.ElasticSearchStatus.chk_mem:  Added MemoryUsed to output and clarified two other components.
- elastic_libs, elastic_class:  Removed unused external library module.


## [2.0.1] - 2020-02-07
### Changed
- elastic_class.ElasticSearchStatus.chk_server, elastic_class.ElasticSearchStatus.chk_nodes, elastic_class.ElasticSearchStatus.chk_mem:  Refactored method to have only one return.
- requirements.txt:  Set elasticsearch between 7.0.0 and 8.0.0.

### Fixed
- requirements.txt:  Changed urllib3 to be 1.24.3 to work with curator.
- elastic_class.ElasticSearchStatus.update_status2:  Fixed incorrect method call.

### Removed
- elastic_class.Elastic class
- elastic_class.ElasticCluster class
- elastic_class.ElasticDump class
- elastic_class.ElasticStatus class


## [2.0.0] - 2019-10-31
Breaking Change

### Changed
- elastic_class.ElasticSearchRepo.\_\_init\_\_:  Changed self.repo_dict default setting from "None" to "{}".
- elastic_class.ElasticSearchRepo.\_\_init\_\_:  Replaced attribute updates with call to update_repo_status().
- elastic_class.ElasticSearchDump.\_\_init\_\_:  Replaced attribute updates with call to update_dump_status().
- elastic_class.ElasticSearchRepo.delete_dump:  Replaced snapshot.delete with call to delete_snapshot().
- elastic_class.ElasticSearchRepo.delete_repo, elastic_class.ElasticSearchRepo.create_repo:  Replaced es.snapshot.get_repository with call to get_repo_list().
- elastic_class.ElasticSearchRepo.delete_repo:  Replaced snapshot.delete_repository with call to delete_snapshot_repo().
- elastic_class.ElasticSearchDump.dump_db:  Replaced snapshot.create with call to create_snapshot().
- elastic_class.ElasticSearchRepo.create_repo:  Replaced snapshot.create_repository with call to create_snapshot_repo().
- elastic_class.ElasticSearch.update_status:  Replaced call to ping with call to is_active().
- elastic_class.ElasticSearch.\_\_init\_\_:  Integrated ElasticCluster class into ElasticSearch class.
- elastic_class.ElasticSearch.\_\_init\_\_:  Integrated Elastic class into ElasticSearch class.
- elastic_class.ElasticSearch.\_\_init\_\_:  Replaced attribute updates with call to update_status().

### Added
- elastic_class.ElasticSearchRepo.update_repo_status:  Update class attributes by querying Elasticsearch.
- elastic_class.ElasticSearchDump.update_dump_status:  Update class attributes by querying Elasticsearch.
- elastic_class.ElasticSearchStatus:  Added class and associated methods.
- elastic_class.ElasticSearch.update_status:  Update class attributes by querying Elasticsearch.
- elastic_class.create_snapshot:  Runs a dump of a repository.
- elastic_class.create_snapshot_repo:  Creates a repository in Elasticsearch cluster.
- elastic_class.delete_snapshot:  Deletes a dump in a repository.
- elastic_class.delete_snapshot_repo:  Deletes a repository in Elasticsearch cluster.
- elastic_class.get_cluster_health:  Dictionary of information on Elasticsearch cluster health.
- elastic_class.get_cluster_nodes:  Dictionary of information on Elasticsearch cluster nodes.
- elastic_class.get_cluster_stats:  Dictionary of information on Elasticsearch cluster stats.
- elastic_class.get_cluster_status:  Status of the Elasticsearch cluster.
- elastic_class.get_disks:  List of disks in Elasticsearch cluser.
- elastic_class.get_info:  Dictionary of basic Elasticsearch info command.
- elastic_class.get_master_name:  Name of the master node in Elasticsearch cluster.
- elastic_class.get_nodes:  Dictionary of information on Elasticsearch nodes.
- elastic_class.get_repo_list:  Dictionary of a list of Elasticsearch repositories.
- elastic_class.get_shards:  List of shards in Elasticsearch cluser.
- elastic_class.is_active:  True or False if the Elasticsearch cluster is up.

### Deprecated
- elastic_class.ElasticCluster:  Integrated into the ElasticSearch class.
- elastic_class.ElasticStatus:  Replaced by the ElasticSearchAdmin class.


## [1.0.4] - 2019-09-02
### Fixed
- elastic_class.chk_all, elastic_class.get_all:  Added return parameters for gen_libs.merge_two_dicts.
- elastic_class.ElasticStatus.chk_disk:  Corrected formatting error.
- elastic_class.ElasticSearch.\_\_init\_\_: Created is_connected attr to maintain connection status.
- elastic_class.ElasticSearchRepo.\_\_init\_\_, elastic_class.ElasticSearchDump.\_\_init\_\_, elastic_class.ElasticSearch.\_\_init\_\_, elastic_libs.get_latest_dump, elastic_libs.list_dumps, elastic_libs.list_repos2:  Fixed problem with mutable default arguments issue.
- elastic_class.ElasticStatus.chk_shards:  Corrected string concentation error.
- elastic_class.ElasticSearchDump.dump_db:  Corrected call syntax to \_chk_status method.
- elastic_class.ElasticSearchDump.\_chk_status:  Corrected call syntax to \_parse method.
- elastic_class.ElasticSearchDump.\_parse:  Corrected incorrect argument list.


## [1.0.3] - 2019-03-12
### Changed
- elastic_class.ElasticStatus.chk_disk:  Updated warning message.
- elastic_class.ElasticSearch.\_\_init\_\_:  Removed check on host_list being a list.
- elastic_class.ElasticSearch.\_\_init\_\_:  Replaced host_list with self.hosts attribute.
- elastic_class.get_dump_list:  Changed ES to es for standard convention.
- elastic_class.ElasticSearchDump.dump_db:  Changed parse() to \_parse.
- elastic_class.ElasticSearchDump.dump_db:  Reduced Cognitive Complexity to accepted standard level - moved section of code to private method: \_chk_status.
- elastic_class.ElasticDump.\_\_init\_\_:  Reduced Cognitive Complexity to accepted standard level - initialized attributes in one area.
- elastic_class.ElasticStatus.\_\_init\_\_:  Reduced Cognitive Complexity to accepted standard level - initalized data variable.
- elastic_class.ElasticSearchDump.\_\_init\_\_:  Reduced Cognitive Complexity to accepted standard level - flatten if statements.

### Added
- elastic_class.ElasticSearchDump.\_parse:  Replaces parse() in dump_db() function.
- elastic_class.ElasticSearchDump.\_chk_status:  Check status of database dump.

### Removed
- elastic_class.ElasticSearchDump.dump_db.parse:  Replaced by \_parse() function.


## [1.0.2] - 2018-11-22
### Changed
- Documentation updates.


## [1.0.1] - 2018-11-19
### Changed
- elastic_libs.list_repos2:  Changed length of repo name field from 25 to 30.

### Removed
- elastic_libs.list_repos function
- elastic_libs.list_dump_format function


## [1.0.0] - 2018-11-02
- General Release

### Changed
- Documentation updates.


## [0.3.15] - 2018-08-12
### Removed
- elastic_libs.delete_repo function
- elastic_libs.create_repo function


## [0.3.14] - 2018-08-06
### Changed
- elastic_class.ElasticSearchDump.dump_db:  Added "body" option to dump command.


## [0.3.13] - 2018-07-23
### Added
- elastic_class.ElasticSearchRepo.delete_dump_all:  Delete all dumps in a repository.
- elastic_class.ElasticSearchRepo.delete_dump:  Delete dump from a repository.

### Changed
- elastic_class.ElasticSearchRepo.delete_repo:  Added check to see if repository exist.


## [0.3.12] - 2018-06-27
### Changed
- Documentation updates.


## [0.3.11] - 2018-06-25
### Changed
- elastic_class.ElasticSearchDump.dump_db:  Update last_dump_name with latest dump name.
- elastic_class.ElasticSearchDump.\_\_init\_\_:  Added seconds to dump_name attribute value.
- elastic_class.ElasticSearchDump.\_\_init\_\_:  Added check to make sure new dump name is unique.


## [0.3.10] - 2018-06-20
### Changed
- Documentation updates.


## [0.3.9] - 2018-06-19
### Fixed
- elastic_class.ElasticSearchDump.\_\_init\_\_:  Added check for repo_name not being set.


## [0.3.8] - 2018-06-18
### Changed
- elastic_class.ElasticSearchDump.dump_db:  Update self.dump_list after dump has completed.
- elastic_class.ElasticSearch.\_\_init\_\_:  Initialize all attributes at the very least.
- elastic_class.ElasticSearchDump.\_\_init\_\_:  Refactored check on repository name argument.
- elastic_class.ElasticSearchRepo.\_\_init\_\_, elastic_class.ElasticSearchDump.\_\_init\_\_:  Initialize all attributes at the very least.


## [0.3.7] - 2018-06-17
### Added
- elastic_class.ElasticSearchDump.dump_db:  Created inner function "parse".
- elastic_class.ElasticSearchRepo class.
- elastic_libs.get_latest_dump:  Function to get latest dump from a list of dumps.
- elastic_class.get_dump_list:  Function to return list of Elasticsearch dumps.
- elastic_class.ElasticSearchDump class
- elastic_class.ElasticSearch class
- elastic_libs.list_repos2:  Lists the repositories in the Elasticsearch cluster.

### Changed
- elastic_libs.list_dumps:  Merged list_dump_format function into this function.

### Deprecated
- elastic_libs.list_repos:  Replaced by elastic_libs.elastic_libs.list_repos2 function.
- elastic_libs.list_dump_format:  Replaced by elastic_libs.list_dumps function.
- elastic_libs.create_repo:  Replaced by ElasticSearchRepo.create_repo method.
- elastic_libs.delete_repo:  Replaced by ElasticSearchRepo.delete_repo method.
- elastic_class.Elastic:  Replaced by ElasticRearch class.
- elastic_class.ElasticDump:  Replaced by ElasticRearchDump class.


## [0.3.6] - 2018-06-06
### Removed
- elastic_libs.List_Dump_Format function
- elastic_libs.List_Dumps function
- elastic_libs.List_Repos function
- elastic_class.Elastic_Cluster class
- elastic_class.Elastic_Dump class
- elastic_class.Elastic_Status ckass


## [0.3.5] - 2018-04-16
### Added
- elastic_libs.delete_repo function:  Replaces "elastic_db_repo.Repo_Deletion" function.


## [0.3.4] - 2018-04-12
### Added
- elastic_libs.create_repo function:  Replaces "elastic_db_repo.Repo_Creation" function.


## [0.3.3] - 2018-04-09
### Added
- elastic_libs.list_repos function:  Replaces "List_Repos".
- elastic_libs.list_dumps function:  Replaces "List_Dumps".
- elastic_libs.list_dump_format:  Replaces "List_Dump_Format".
- elastic_class.ElasticCluster class:  Replaces "Elastic_Cluster".
- elastic_class.ElasticDump class:  Replaces "Elastic_Dump".
- elastic_class.ElasticStatus class:  Replaces "Elastic_Status".

### Changed
- elastic_class.ElasticStatus.chk_all:  Changed "Merge_2_Dicts" to "merge_two_dicts".
- elastic_class.ElasticStatus.chk_mem:  Changed "Bytes_2_Readable" to "bytes_2_readable".
- elastic_class.ElasticStatus.get_all:  Changed "Merge_2_Dicts" to "merge_two_dicts".
- elastic_class.ElasticStatus.get_dump_disk_status:  Changed "Bytes_2_Readable" to "bytes_2_readable" and "Disk_Usage" to "disk_usage".
- elastic_class.ElasticStatus.get_mem_status:  Changed "Bytes_2_Readable" to "bytes_2_readable".
- elastic_class.ElasticStatus.get_svr_status:  Changed "Milli_2_Readadble" to "milli_2_readadble".
- elastic_class.ElasticDump.dump_db: Changed "Put_Cmd" to "put_cmd".
- elastic_class.ElasticDump.\_\_init\_\_, elastic_class.ElasticCluster.\_\_init\_\_, elastic_class.Elastic.\_\_init\_\_, elastic_class.ElasticStatus.\_\_init\_\_: Changed "Get_Query" to "get_query".
- elastic_class.py, elastic_libs.py:  Setup single source version control.

### Fixed
- elastic_libs.py:  Corrected library module pointing to requests_lib/requests_libs.

### Deprecated
- elastic_libs.List_Dump_Format function:  Replace by "list_dump_format".
- elastic_libs.List_Repos function:  Replace by "list_repos".
- elastic_libs.List_Dumps function:  Replace by "list_dumps".
- elastic_class.Elastic_Cluster class:  Replace by "ElasticCluster".
- elastic_class.Elastic_Dump class:  Replace by "ElasticDump".
- elastic_class.Elastic_Status class:  Replace by "ElasticStatus".


## [0.3.2] - 2018-04-05
### Changed
- elastic_class.py:  Moved requests_libs module into requests_lib directory.


## [0.3.1] - 2017-10-12
### Added
- elastic_class.Elastic_Status.get_dump_disk_status:  Display dump partition status.

### Changed
- elastic_class.Elastic_Status.get_all:  Add get_dump_disk_status to method.
- elastic_class.Elastic_Status.get_disk_status:  Change formatting of standard output.
- elastic_class.Elastic_Status.get_disk_status:  Refactor code to reduce levels of code.


## [0.3.0] - 2017-10-11
- Field release.


## [0.2.1] - 2017-10-10
### Changed
- elastic_libs.List_Dumps:  Change in argument to accept a dump list.

### Removed
- elastic_class.Elastic_Replica class.


## [0.2.0] - 2017-10-09
- Beta release.


## [0.1.11] - 2017-10-04
### Fixed
- elastic_class.py:  Error: Unable to dump to new repository as no last dump is is listed.
- elastic_class.Elastic_Dump.\_\_init\_\_:  Set last_dump_name to None if new or empty repository.


## [0.1.10] - 2017-10-02
### Changed
- elastic_class.Elastic_Status.chk_all:  Add cutoff_disk argument to function.
- elastic_class.Elastic_Status.get_disk_status:  Add percentage used value to output.
- elastic_class.Elastic_Status.chk_disk_status:  Change format of output.
- elastic_class.Elastic_Status.get_disk_status:  Refactored method.
- elastic_class.Elastic_Status.chk_mem:  Change total_memory to readable format.
- elastic_class.Elastic_Status:  Change method name from chk_disk_status to chk_disk.


## [0.1.9] - 2017-09-29
### Added
- elastic_class.Elastic_Status.get_disk_status method.
- elastic_class.Elastic_Status.chk_disk_status method.

### Changed
- elastic_class.Elastic_Status.\_\_init\_\_:  Add attributes for disk space usage and cutoffs.
- elastic_class.Elastic_Status.get_all:  Refactored method.
- elastic_class.Elastic_Status.get_all:  Added get_disk_status to method.


## [0.1.8] - 2017-09-28
### Changed
- elastic_class.Elastic_Status.\_\_init\_\_:  Add new attributes for cpu and memory threshold cutoffs.
- elastic_class.Elastic_Status.chk_mem, elastic_class.Elastic_Status.chk_server:  Use class attribute as the default setting for threshold.


## [0.1.7] - 2017-09-25
### Added
- elastic_class.Elastic_Status.chk_all emthod.

### Changed
- elastic_class.Elastic_Status:  Add returns on all output functions.
- elastic_class.Elastic_Status:  Refactor "if" statements.
- elastic_class.Elastic_Status.get_svr_status:  Change uptime milliseconds to human-readable format.
- elastic_class.Elastic_Status.get_mem_status:  Change memory values to human-readable format.


## [0.1.6] - 2017-09-22
### Added
- elastic_class.Elastic_Status.chk_status method.
- elastic_class.Elastic_Status.get_all method.

### Changed
- elastic_class.Elastic_Status.chk_shards method.


## [0.1.5] - 2017-09-21
### Added
- elastic_class.Elastic_Status.chk_mem method.
- elastic_class.Elastic_Status.chk_nodes method.
- elastic_class.Elastic_Status.chk_shards method.
- elastic_class.Elastic_Status.chk_server method.
- elastic_class.Elastic_Status.get_gen_status method.


## [0.1.4] - 2017-09-20
### Added
- elastic_class.Elastic_Status.get_cluster method.
- elastic_class.Elastic_Status.get_nodes method.
- elastic_class.Elastic_Status.get_node_status method.
- elastic_class.Elastic_Status.get_svr_status method.
- elastic_class.Elastic_Status.get_mem_status method.
- elastic_class.Elastic_Status.get_shrd_status method.

### Changed
- elastic_class.Elastic_Status:  Add attributes alloc_cpu and cpu_active to class.
- elastic_class.Elastic_Cluster:  Move num_shards and num_primary to Elastic_Status class.
- elastic_class.Elastic_Cluster:  Combine data2 and cluster_status into single command.
- elastic_class.Elastic_Cluster:  Combine data3 and master into single command.


## [0.1.3] - 2017-09-19
### Added
- elastic_class.Elastic_Status class.

### Changed
- elastic_libs.List_Dumps:  Replace print header with call to "List_Dump_Format".


## [0.1.2] - 2017-09-18
### Added
- elastic_libs.List_Dump_Format function.

### Changed
- elastic_class.Elastic_Cluster.\_\_init\_\_: Add attribute repo_list.


## [0.1.1] - 2017-09-15
### Fixed
- elastic_class.Elastic_Dump.\_\_init\_\_:  Modify code to deal with multiple repositories.
- elastic_class.Elastic_Dump.\_\_init\_\_:  Accept new argument into class:  repo

### Changed
- elastic_class.Elastic_Dump.dump_db:  Add additional checks to ensure dump will be successful.
- elastic_class.Elastic_Dump.\_\_init\_\_:  Change self.dump_list to an empty list.


## [0.1.0] - 2017-09-13
- Alpha release.


## [0.0.5] - 2017-09-12
### Fixed
- elastic_class.Elastic_Dump.\_\_init\_\_:  Database dump list being incorrectly parsed on white spaces.

### Changed
- elastic_class.py:  Change all requests_libs.Get_Query calls to add leading slash.
- elastic_class.Elastic_Dump.\_\_init\_\_:  Add new attribute to hold list of database dumps.


## [0.0.4] - 2017-09-11
### Added
- elastic_class.Elastic_Dump.dump_db method.

### Changed
- elastic_class.Elastic_Dump.\_\_init\_\_:  Changed attribute setting for dump name.


## [0.0.3] - 2017-09-07
### Changed
- elastic_class.py:  Initialize attributes in Elastic_Cluster class.
- elastic_class.py:  Initialize attributes in Elastic class.
- elastic_class.py:  Initialize attributes in Elastic_Dump class.
- elastic_class.py:  Initialize attributes in Elastic_Replica class.


## [0.0.2] - 2017-09-05
### Changed
- elastic_class.py:  Moved Elastic_Dump class to under Elastic_Cluster class.


## [0.0.1] - 2017-09-01
- Initial Pre-Alpha release.
