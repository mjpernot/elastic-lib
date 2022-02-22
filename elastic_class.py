# Classification (U)

"""Program:  elastic_class.py

    Description:  Class definitions and methods for an Elasticsearch cluster,
        Elasticsearch cluster dump, Elasticsearch cluster repository, and
        Elasticsearch cluster status.  Includes supporting functions for the
        classes.

    Functions:
        create_snapshot
        create_snapshot_repo
        delete_snapshot
        delete_snapshot_repo
        get_cluster_health
        get_cluster_nodes
        get_cluster_stats
        get_disks
        get_dump_list
        get_info
        get_master_name
        get_nodes
        get_repo_list
        get_shards
        is_active

    Classes:
        ElasticSearch
            ElasticSearchDump
            ElasticSearchRepo
            ElasticSearchStatus

"""

# Libraries and Global Variables

# Standard
import datetime
import time

# Third-party
import elasticsearch

# Local
import elastic_libs
import lib.gen_libs as gen_libs
import version

__version__ = version.__version__


def create_snapshot(els, reponame, body, dumpname):

    """Function:  create_snapshot

    Description:  Runs a dump of a named repository.

    Arguments:
        (input) els -> ElasticSearch instance
        (input) reponame -> Name of repository
        (input) body -> Contains arguments for the dump command
        (input) dumpname -> Dump name which it will be dumped too

    """

    body = dict(body)
    els.snapshot.create(repository=reponame, body=body, snapshot=dumpname)


def create_snapshot_repo(els, reponame, body, verify=True):

    """Function:  create_snapshot_repo

    Description:  Creates a repository in Elasticsearch cluster.

    Arguments:
        (input) els -> ElasticSearch instance
        (input) reponame -> Name of repository
        (input) body -> Contains arguments for the dump command
        (input) verify -> True|False - Validate the repository
        (output) Return exit status of create_repository command

    """

    body = dict(body)
    return els.snapshot.create_repository(repository=reponame, body=body,
                                          verify=verify)


def delete_snapshot(els, reponame, dumpname):

    """Function:  delete_snapshot

    Description:  Deltes a dump in a named repository.

    Arguments:
        (input) els -> ElasticSearch instance
        (input) reponame -> Name of repository
        (input) dumpname -> Dump name to be deleted
        (output) Return exit status of delete_repository command

    """

    return els.snapshot.delete(repository=reponame, snapshot=dumpname)


def delete_snapshot_repo(els, reponame):

    """Function:  delete_snapshot_repo

    Description:  Deletes named repository in Elasticsearch cluster.

    Arguments:
        (input) els -> ElasticSearch instance
        (input) reponame -> Name of repository
        (output) Return exit status of delete_repository command

    """

    return els.snapshot.delete_repository(repository=reponame)


def get_cluster_health(els):

    """Function:  get_cluster_health

    Description:  Return a dict of information on Elasticsearch cluster health.

    Arguments:
        (input) els -> ElasticSearch instance
        (output) Dictionary of information on Elasticsearch cluster health

    """

    return els.cluster.health()


def get_cluster_nodes(els):

    """Function:  get_cluster_nodes

    Description:  Return a dict of information on Elasticsearch cluster nodes.

    Arguments:
        (input) els -> ElasticSearch instance
        (output) Dictionary of information on Elasticsearch cluster nodes

    """

    return els.nodes.info()


def get_cluster_stats(els):

    """Function:  get_cluster_stats

    Description:  Return a dict of information on Elasticsearch cluster stats.

    Arguments:
        (input) els -> ElasticSearch instance
        (output) Dictionary of information on Elasticsearch cluster stats

    """

    return els.cluster.stats()


def get_cluster_status(els):

    """Function:  get_cluster_status

    Description:  Return status of the Elasticsearch cluster.

    Arguments:
        (input) els -> ElasticSearch instance
        (output) Status of the Elasticsearch cluster

    """

    return els.cluster.health()["status"]


def get_disks(els):

    """Function:  get_disks

    Description:  Return a list of disks within the Elasticsearch cluster.

    Arguments:
        (input) els -> ElasticSearch instance
        (output) List of ElasticSearch disks

    """

    return els.cat.allocation(format="json")


def get_dump_list(els, repo, **kwargs):

    """Function:  get_dump_list

    Description:  Return a list of dumps within a named repository.

    Note:  The "ignore" option will determine whether to ignore the exception
        or capture the exception and process it.

    Future mods:  If want to capture the exception codes then will need to add
        the following to the end of the exception: as (err_num, err_code, msg) 

    Arguments:
        (input) els -> ElasticSearch instance
        (input) repo -> Name of repository
        (input) kwargs:
            snapshot -> A list of snapshot names, defaults to all snapshots
            ignore -> True|False - Ignore if snapshot name is not found
        (output) dump_list -> List of ElasticSearch dumps
        (output) status -> True|False - If found snapshot successfully
        (output) err_msg -> Error message if snapshot not found

    """

    snapshot = kwargs.get("snapshot", "_all")
    ignore = kwargs.get("ignore", True)
    err_msg = None

    try:
        data = els.snapshot.get(
            repository=repo, snapshot=snapshot, ignore_unavailable=ignore)
        dump_list = data["snapshots"]
        status = True

    except elasticsearch.exceptions.NotFoundError:
        err_msg = "Failed to find snapshot: '%s' in repository: '%s'" % (
            snapshot, repo)
        dump_list = []
        status = False

    return dump_list, status, err_msg


def get_info(els):

    """Function:  get_info

    Description:  Return a dictionary of a basic Elasticsearch info command.

    Arguments:
        (input) els -> ElasticSearch instance
        (output) Dictionary of basic Elasticsearch info command

    """

    return els.info()


def get_master_name(els):

    """Function:  get_master_name

    Description:  Return name of the master node in a Elasticsearch cluster.

    Arguments:
        (input) els -> ElasticSearch instance
        (output) Name of master node in ElasticSearch cluster

    """

    return els.cat.master(format="json")[0]["node"]
    #return els.cat.master().strip().split(" ")[-1]


def get_nodes(els):

    """Function:  get_nodes

    Description:  Return a dictionary of information on Elasticsearch nodes.

    Arguments:
        (input) els -> ElasticSearch instance
        (output) Dictionary of information on Elasticsearch nodes

    """

    return els.nodes.info()["nodes"]


def get_repo_list(els):

    """Function:  get_repo_list

    Description:  Return a dictionary of a list of Elasticsearch repositories.

    Arguments:
        (input) els -> ElasticSearch instance
        (output) Dictionary of a list of Elasticsearch repositories

    """

    return els.snapshot.get_repository()


def get_shards(els):

    """Function:  get_shards

    Description:  Return a list of shards within the Elasticsearch cluster.

    Arguments:
        (input) els -> ElasticSearch instance
        (output) List of ElasticSearch shards

    """

    return els.cat.shards(format="json")
    #return [item.split() for item in els.cat.shards().splitlines()]


def is_active(els):

    """Function:  is_active

    Description:  Returns True or False if the Elasticsearch cluster is up.

    Arguments:
        (input) els -> ElasticSearch instance
        (output) True|False - Elasticsearch cluster is up

    """

    return els.ping()


class ElasticSearch(object):

    """Class:  ElasticSearch

    Description:  Class which is a representation of an ElasticSearch
        database/cluster.  An ElasticSearch object is used as proxy to
        implement the connecting to an execute commands in an ElasticSearch
        database/cluster.

    Methods:
        __init__
        connect
        set_login_config
        set_ssl_config
        update_status

    """

    def __init__(self, host_list, port=9200, **kwargs):

        """Method:  __init__

        Description:  Initialization of an instance of the ElasticSearch class.

        Arguments:
            (input) host_list -> List of host(s) within ElasticSearch cluster
            (input) port -> ElasticSearch port to connect to
            (input) kwargs:
                user -> User login name
                japd -> User pswd
                ca_cert -> CA Certificate
                scheme -> Type of connection

        """

        self.port = port
        self.hosts = list(host_list)
        self.cluster_name = None
        self.node_connected_to = None
        self.is_connected = False
        self.data = {}
        self.logs = {}
        self.nodes = []
        self.total_nodes = None
        self.cluster_status = None
        self.master = None
        self.els = None

        # Login configuration setup
        self.config = {}
        self.user = kwargs.get("user", None)
        self.japd = kwargs.get("japd", None)
        self.set_login_config()

        # SSL configuration setup
        self.ca_cert = kwargs.get("ca_cert", None)
        self.scheme = kwargs.get("scheme", "https")
        self.set_ssl_config()

    def connect(self):

        """Method:  connect

        Description:  Connection to ElasticSearch server/cluster.

        Arguments:

        """

        self.els = elasticsearch.Elasticsearch(
            self.hosts, port=self.port, **self.config)

        if is_active(self.els):
            self.is_connected = True
            self.update_status()

        else:
            self.is_connected = False

    def set_login_config(self):

        """Method:  set_login_config

        Description:  Set the login config attributes.

        Arguments:

        """

        if self.user and self.japd:
            self.config["http_auth"] = (self.user, self.japd)

    def set_ssl_config(self):

        """Method:  set_ssl_config

        Description:  Set the SSL config attributes.

        Arguments:

        """

        if self.ca_cert:
            self.config["use_ssl"] = True
            self.config["ca_certs"] = self.ca_cert
            self.config["scheme"] = self.scheme

    def update_status(self):

        """Method:  update_status

        Description:  Update class attributes by querying Elasticsearch.

        Arguments:

        """

        # Basic information
        info = get_info(self.els)

        self.node_connected_to = info["name"]

        # Node information
        data = get_nodes(self.els)

        for item in data:
            self.data[data[item]["name"]] = \
                data[item]["settings"]["path"]["data"]
            self.logs[data[item]["name"]] = \
                data[item]["settings"]["path"]["logs"]

        self.nodes = [data[item]["name"] for item in data]

        # Cluster node information
        cluster = get_cluster_nodes(self.els)

        self.total_nodes = cluster["_nodes"]["total"]

        # Cluster health information
        health = get_cluster_health(self.els)

        self.cluster_status = health["status"]
        self.cluster_name = health["cluster_name"]

        # Master information
        self.master = get_master_name(self.els)


class ElasticSearchDump(ElasticSearch):

    """Class:  ElasticSearchDump

    Description:  Class which is a representation of ElasticSearch database
        dump.  An ElasticSearchDump object is used as proxy to implement a
        database dump of an ElasticSearch database/cluster.

    Methods:
        __init__
        connect
        update_dump_status
        dump_db
        _chk_status
        _parse

    """

    def __init__(self, host_list, port=9200, repo=None, **kwargs):

        """Method:  __init__

        Description:  Initialization of an instance of the ElasticSearchDump
            class.

        Arguments:
            (input) host_list -> List of host(s) within ElasticSearch cluster
            (input) port -> ElasticSearch database port
            (input) repo -> Name of repository, required if multiple
                repositories are present in the cluster
            (input) kwargs:
                user -> User login name
                japd -> User pswd
                ca_cert -> CA Certificate
                scheme -> Type of connection

        """

        host_list = list(host_list)
        super(ElasticSearchDump, self).__init__(host_list, port, **kwargs)

        self.dump_status = None
        self.failed_shards = 0
        self.type = None
        self.dump_loc = None
        self.dump_list = []
        self.last_dump_name = None
        self.dump_name = None
        self.repo_name = repo

    def connect(self):

        """Method:  connect

        Description:  Connection to ElasticSearch server/cluster.

        Arguments:

        """

        super(ElasticSearchDump, self).connect()

        if self.is_connected:
            self.update_dump_status()

    def update_dump_status(self):

        """Method:  update_dump_status

        Description:  Update class attributes by querying Elasticsearch.

        Arguments:

        """

        self.dump_name = self.cluster_name.lower() + "_bkp_" + \
            datetime.datetime.strftime(
                datetime.datetime.now(), "%Y%m%d-%H%M%S")
        repo_dict = get_repo_list(self.els)

        if self.repo_name and self.repo_name not in repo_dict:
            self.repo_name = None

        elif not self.repo_name:

            # Use if only one repository exists.
            if len(repo_dict.keys()) == 1:
                self.repo_name = next(iter(repo_dict))

            # Cannot set if multiple repositories exist.
            elif len(repo_dict.keys()) >= 1:
                self.repo_name = None

        if self.repo_name:
            self.type = repo_dict[self.repo_name]["type"]
            self.dump_loc = repo_dict[self.repo_name]["settings"]["location"]
            self.dump_list, _, _ = get_dump_list(self.els, self.repo_name)

        if self.dump_list:
            self.last_dump_name = elastic_libs.get_latest_dump(self.dump_list)

        # Make sure new dump name is unique.
        if self.dump_name == self.last_dump_name:
            time.sleep(1)
            self.dump_name = self.cluster_name.lower() + "_bkp_" + \
                datetime.datetime.strftime(
                    datetime.datetime.now(), "%Y%m%d-%H%M%s")

    def dump_db(self, dbs=None):

        """Method:  dump_db

        Description:  Executes a dump of an ElasticSearch database.

        Arguments:
            (input) dbs -> String of database(s) to dump, comma delimited
            (output) err_flag True|False -> Were errors detected during dump
            (output) status_msg -> Dump error message

        """

        err_flag = False
        status_msg = None
        break_flag = False
        body = {}

        if dbs and isinstance(dbs, str):
            body = {"indices": dbs, "ignore_unavailable": True}

        elif dbs and not isinstance(dbs, str):
            err_flag = True
            status_msg = "ERROR:  Database name(s) is not a string: %s" % dbs

        if self.repo_name and not err_flag:
            create_snapshot(self.els, self.repo_name, body, self.dump_name)

            while not break_flag and not err_flag:

                err_flag, status_msg, break_flag = self._chk_status(break_flag)

            self.dump_list, _, _ = get_dump_list(self.els, self.repo_name)
            self.last_dump_name = elastic_libs.get_latest_dump(self.dump_list)

        elif not err_flag:
            err_flag = True
            status_msg = "ERROR:  Repository name not set."

        return err_flag, status_msg

    def _chk_status(self, break_flag):

        """Function:  _chk_status

        Description:  Check status of database dump.

        Arguments:
            (input) break_flag True|False -> Break out of loop for check
            (output) err_flag True|False -> Were errors detected during dump
            (output) status_msg -> Dump error message
            (output) break_flag True|False -> Break out of loop for check

        """

        err_flag = False
        status_msg = None

        for dump in get_dump_list(self.els, self.repo_name)[0]:

            if self.dump_name == dump["snapshot"]:

# Remove _parse method
#                self.dump_status, self.failed_shards = self._parse(dump)
                self.dump_status = dump["state"]
                self.failed_shards = dump["shards"]["failed"]

                if self.dump_status == "IN_PROGRESS":
                    time.sleep(5)

                elif self.dump_status == "SUCCESS":
                    break_flag = True

                elif self.dump_status == "INCOMPATIBLE":
                    status_msg = "Older version of ES detected: %s" \
                                 % (self.repo_name)
                    err_flag = True

                elif self.dump_status == "PARTIAL":
                    status_msg = "Partial dump completed on %s" \
                                 % (self.repo_name)
                    err_flag = True

                elif self.dump_status == "FAILED":
                    status_msg = "Dump failed to finish on %s" \
                                 % (self.repo_name)
                    err_flag = True

                else:
                    status_msg = "Unknown error '%s' detected on %s" \
                                 % (self.dump_status, self.repo_name)
                    err_flag = True

        return err_flag, status_msg, break_flag

    def _parse(self, dump):

        """Function:  _parse

        Description:  Parse the dump entry for status and shard.

        Arguments:
            (input)  dump -> Dump entry
            (output) Return dump status
            (output) Return shard failures

        """

        return dump[1], dump[9]


class ElasticSearchRepo(ElasticSearch):

    """Class:  ElasticSearchRepo

    Description:  Class which is a representation of ElasticSearchRepo
        repositories.  An ElasticSearchRepo object is used as proxy to
        implement respositories within an Elasticsearch cluster.

    Methods:
        __init__
        connect
        update_repo_status
        create_repo
        delete_repo
        delete_dump
        delete_dump_all

    """

    def __init__(self, host_list, port=9200, repo=None, repo_dir=None,
                 **kwargs):

        """Method:  __init__

        Description:  Initialization of an instance of the ElasticSearchRepo
            class.

        Arguments:
            (input) host_list -> List of host(s) within ElasticSearch cluster
            (input) port -> ElasticSearch database port
            (input) repo -> Name of repository
            (input) repo_dir -> Directory path to respository
            (input) kwargs:
                user -> User login name
                japd -> User pswd
                ca_cert -> CA Certificate
                scheme -> Type of connection

        """

        host_list = list(host_list)
        super(ElasticSearchRepo, self).__init__(host_list, port, **kwargs)

        self.repo = repo
        self.repo_dir = repo_dir
        self.repo_dict = {}

    def connect(self):

        """Method:  connect

        Description:  Connection to ElasticSearch server/cluster.

        Arguments:

        """

        super(ElasticSearchRepo, self).connect()

        if self.is_connected:
            self.update_repo_status()

    def update_repo_status(self):

        """Method:  update_repo_status

        Description:  Query dump repository and update class attributes.

        Arguments:

        """

        self.repo_dict = get_repo_list(self.els)

    def create_repo(self, repo_name=None, repo_dir=None):

        """Method:  create_repo

        Description:  Create an elasticsearch dump repository.

        Arguments:
            (input) repo_name -> Name of repository
            (input) repo_dir -> Directory path to respository
            (output) err_flag -> True|False - Error status for repo creation
            (output) err_msg -> Status error message or None

        """

        err_flag = False
        err_msg = None

        if not repo_name:
            repo_name = self.repo

        if not repo_dir:
            repo_dir = self.repo_dir

        if repo_name and repo_dir:

            data_dict = {"type": "fs", "settings": {"location": repo_dir,
                                                    "compress": True}}

            status = create_snapshot_repo(self.els, repo_name, data_dict, True)

            if not status["acknowledged"]:
                err_flag = True
                err_msg = "ERROR:  Repository creation failure:  %s, %s" \
                          % (repo_name, repo_dir)

            else:
                # Update repo dictionary.
                self.repo_dict = get_repo_list(self.els)

                if repo_name not in self.repo_dict:
                    err_flag = True
                    err_msg = "ERROR:  Repository not detected:  %s, %s" \
                              % (repo_name, repo_dir)

        else:
            err_flag = True
            err_msg = "ERROR: Missing repo name or directory: '%s', '%s'" \
                      % (repo_name, repo_dir)

        return err_flag, err_msg

    def delete_repo(self, repo_name=None):

        """Method:  delete_repo

        Description:  Delete an elasticsearch dump repository.

        Arguments:
            (input) repo -> Name of repository
            (output) err_flag -> True|False - Error status for repo deletion
            (output) err_msg -> Status error message or None

        """

        err_flag = False
        err_msg = None

        if not repo_name:
            repo_name = self.repo

        if repo_name and repo_name in self.repo_dict:

            status = delete_snapshot_repo(self.els, repo_name)

            if not status["acknowledged"]:
                err_flag = True
                err_msg = "ERROR:  Repository deletion failed:  %s" \
                          % (repo_name)

            else:
                # Update repo dictionary.
                self.repo_dict = get_repo_list(self.els)

                if repo_name in self.repo_dict:
                    err_flag = True
                    err_msg = "ERROR:  Repository still detected:  %s" \
                              % (repo_name)

        else:
            err_flag = True
            err_msg = "ERROR: Missing repo or does not exist: %s" % (repo_name)

        return err_flag, err_msg

    def delete_dump(self, repo_name=None, dump_name=None):

        """Method:  delete_dump

        Description:  Delete a database dump in an Elasticsearch repository.

        Arguments:
            (input) repo_name -> Name of repository
            (input) dump_name -> Name of dump
            (output) err_flag -> True|False - Error status for deletion
            (output) err_msg -> Error message, if any

        """

        err_flag = False
        err_msg = None

        if not repo_name:
            repo_name = self.repo

        if repo_name and dump_name and repo_name in self.repo_dict:

            # See if the dump exists.
            if dump_name in \
               [item["snapshot"] for item in get_dump_list(
                   self.els, repo_name)[0]]:

                status = delete_snapshot(self.els, repo_name, dump_name)

                if not status["acknowledged"]:
                    err_flag = True
                    err_msg = "ERROR:  Dump deletion failed:  %s, %s" \
                              % (repo_name, dump_name)

                else:
                    # Does the dump still exists
                    if dump_name in \
                       [item["snapshot"] for item in get_dump_list(
                           self.els, repo_name)[0]]:

                        err_flag = True
                        err_msg = "ERROR: Dump still detected: %s, %s" \
                                  % (repo_name, dump_name)

            else:
                err_flag = True
                err_msg = "ERROR: Dump: %s not in Repository: %s" \
                          % (dump_name, repo_name)

        else:
            err_flag = True
            err_msg = "ERROR: Missing arg/repo not exist, Repo: %s, Dump: %s" \
                      % (repo_name, dump_name)

        return err_flag, err_msg

    def delete_dump_all(self, repo_name=None):

        """Method:  delete_dump_all

        Description:  Delete all dumps in a repository.

        Arguments:
            (input)  repo_name -> Name of repository
            (output) err_flag -> True|False - Error status for deletion
            (output) err_msg -> Status error message or None

        """

        err_flag = False
        err_msg = None

        if not repo_name:
            repo_name = self.repo

        if repo_name and repo_name in self.repo_dict:

            for dump in \
               [item["snapshot"] for item in get_dump_list(
                   self.els, repo_name)[0]]:

                err_flag, err_msg = self.delete_dump(repo_name=repo_name,
                                                     dump_name=dump)

                # Stop deleting if error
                if err_flag:
                    break

        else:
            err_flag = True
            err_msg = "ERROR:  Repo:  %s is not present or missing argument." \
                      % (repo_name)

        return err_flag, err_msg


class ElasticSearchStatus(ElasticSearch):

    """Class:  ElasticSearchStatus

    Description:  Class which is a representation of an elasticsearch
        cluster status which contains attributes to show the general health of
        the cluster.  An ElasticSearchStatus is used as a proxy to implment
        connecting to an elasticsearch cluster and executing status commands.

    Methods:
        __init__
        connect
        update_status2
        get_cluster
        get_nodes
        get_node_status
        get_svr_status
        get_mem_status
        get_shrd_status
        get_gen_status
        get_disk_status
        get_dump_disk_status
        get_all
        chk_mem
        chk_nodes
        chk_shards
        chk_server
        chk_status
        chk_disk
        chk_all

    """

    def __init__(self, hostname, port=9200, cutoff_mem=90, cutoff_cpu=75,
                 cutoff_disk=85, **kwargs):

        """Method:  __init__

        Description:  Initialization of an instance of ElasticSearchStatus
            class.

        Arguments:
            (input) hostname -> Hostname of Elasticsearch database node
            (input) port -> Elasticsearch database port.  Default = 9200
            (input) cutoff_mem -> Threshold cutoff for memory check
            (input) cutoff_cpu -> Threshold cutoff for cpu usage check
            (input) cutoff_disk -> Threshold cutoff for disk usage check
            (input) kwargs:
                user -> User login name
                japd -> User pswd
                ca_cert -> CA Certificate
                scheme -> Type of connection

        """

        super(ElasticSearchStatus, self).__init__(hostname, port, **kwargs)

        self.cutoff_mem = cutoff_mem
        self.cutoff_cpu = cutoff_cpu
        self.cutoff_disk = cutoff_disk
        self.unassigned_shards = None
        self.active_shards_percent = None
        self.pending_tasks = None
        self.num_shards = None
        self.num_primary = None
        self.shard_list = []
        self.failed_nodes = None
        self.mem_per_used = None
        self.mem_total = None
        self.mem_used = None
        self.mem_free = None
        self.uptime = None
        self.alloc_cpu = None
        self.cpu_active = None
        self.disk_list = []
        self.repo_dict = {}

    def connect(self):

        """Method:  connect

        Description:  Connection to ElasticSearch server/cluster.

        Arguments:

        """

        super(ElasticSearchStatus, self).connect()

        if self.is_connected:
            self.update_status2()

    def update_status2(self):

        """Method:  update_status2

        Description:  Update class attributes by querying Elasticsearch.

        Arguments:

        """

        # Get cluster health
        health = get_cluster_health(self.els)

        self.unassigned_shards = health["unassigned_shards"]
        self.active_shards_percent = \
            health["active_shards_percent_as_number"]
        self.pending_tasks = health["number_of_pending_tasks"]
        self.num_shards = health["active_shards"]
        self.num_primary = health["active_primary_shards"]

        # Get cluster shards
        self.shard_list = get_shards(self.els)

        # Get cluster status
        status = get_cluster_stats(self.els)

        self.failed_nodes = status["_nodes"]["failed"]
        self.mem_per_used = status["nodes"]["os"]["mem"]["used_percent"]
        self.mem_total = status["nodes"]["os"]["mem"]["total_in_bytes"]
        self.mem_used = status["nodes"]["os"]["mem"]["used_in_bytes"]
        self.mem_free = status["nodes"]["os"]["mem"]["free_in_bytes"]
        self.uptime = status["nodes"]["jvm"]["max_uptime_in_millis"]
        self.alloc_cpu = status["nodes"]["os"]["allocated_processors"]
        self.cpu_active = status["nodes"]["process"]["cpu"]["percent"]

        # Get disks usage
        self.disk_list = get_disks(self.els)

        # Get repository list
        self.repo_dict = get_repo_list(self.els)

    def get_cluster(self):

        """Method:  get_cluster

        Description:  Return dictionary format of cluster name.

        Arguments:
            (output) Dictionary of cluster name

        """

        return {"Cluster": self.cluster_name}

    def get_nodes(self):

        """Method:  get_nodes

        Description:  Return dictionary format of a list of node names.

        Arguments:
            (output) Dictionary list of node names

        """

        return {"Nodes": [str(x) for x in self.nodes]}

    def get_node_status(self):

        """Method:  get_node_status

        Description:  Return dictionary format of status of nodes.

        Arguments:
            (output) Return dictionary format of status of nodes in cluster

        """

        return {"NodeStatus": {"TotalNodes": self.total_nodes,
                               "FailedNodes": self.failed_nodes}}

    def get_svr_status(self):

        """Method:  get_svr_status

        Description:  Return dictionary format of status of server.

        Arguments:
            (output) Return dictionary dictionary format of status of server

        """

        return {"Server": {"Uptime": gen_libs.milli_2_readadble(self.uptime),
                           "AllocatedCPU": self.alloc_cpu,
                           "CPUActive": self.cpu_active}}

    def get_mem_status(self):

        """Method:  get_mem_status

        Description:  Return dictionary format of status of memory on server.

        Arguments:
            (output) Return dictionary format of status of memory

        """

        return {"Memory": {"Percent": self.mem_per_used,
                           "Total": gen_libs.bytes_2_readable(self.mem_total),
                           "Used": gen_libs.bytes_2_readable(self.mem_used),
                           "Free": gen_libs.bytes_2_readable(self.mem_free)}}

    def get_shrd_status(self):

        """Method:  get_shrd_status

        Description:  Return dictionary format of status of shards in cluster.

        Arguments:
            (output) Return dictionary format of status of shards in cluster

        """

        return {"Shards": {"Percent": self.active_shards_percent,
                           "Unassigned": self.unassigned_shards,
                           "Total": self.num_shards,
                           "Primary": self.num_primary}}

    def get_gen_status(self):

        """Method:  get_shard_status

        Description:  Return dictionary format of general status in cluster.

        Arguments:
            (output) Return dictionary format of general status of cluster

        """

        return {"ClusterStatus": {"Master": self.master,
                                  "Status": self.cluster_status,
                                  "PendingTasks": self.pending_tasks}}

    def get_disk_status(self):

        """Method:  get_disk_status

        Description:  Return dictionary format of status of disk usage for each
            node.

        Arguments:
            (output) data -> Dictionary format of disk usage status by node

        """

        data = {"DiskUsage": {}}

        for node in self.disk_list:
            data["DiskUsage"][node["node"]] = {
                "Total": node["disk.total"], "Available": node["disk.avail"],
                "TotalUsed": node["disk.used"], "ESUsed": node["disk.indices"],
                "Percent": node["disk.percent"]}

#        for node in self.disk_list:
#            if node[1] != "UNASSIGNED":
#                data["DiskUsage"][node[8]] = {
#                    "Total": node[4], "Available": node[3],
#                    "TotalUsed": node[2], "ESUsed": node[1],
#                    "Percent": node[5]}

        return data

    def get_dump_disk_status(self):

        """Method:  get_dump_disk_status

        Description:  Return dictionary format of status of dump disk usage for
            each repository.

        Arguments:
            (output) data -> Dictionary format of dump disk usage by repo

        """

        data = {"DumpUsage": {}}

        for repo in self.repo_dict:
            partition = self.repo_dict[repo]["settings"]["location"]
            usage = gen_libs.disk_usage(partition)

            data["DumpUsage"][repo] = {
                "Partition": partition,
                "Total": gen_libs.bytes_2_readable(usage.total),
                "Used": gen_libs.bytes_2_readable(usage.used),
                "Free": gen_libs.bytes_2_readable(usage.free),
                "Percent": (float(usage.used) / usage.total) * 100}

        return data

    def get_all(self):

        """Method:  get_all

        Description:  Return dictionary format of  status of all elements.

        Arguments:
            (output) data -> Dictionary format of status of all elements

        """

        # List of checks to be called
        func_list = [self.get_nodes, self.get_node_status,
                     self.get_svr_status, self.get_mem_status,
                     self.get_shrd_status, self.get_gen_status,
                     self.get_disk_status]
        data = self.get_cluster()

        for func in func_list:
            results = func()
            data, _, _ = gen_libs.merge_two_dicts(data, results)

        return data

    def chk_mem(self, cutoff_mem=None, **kwargs):

        """Method:  chk_mem

        Description:  Checks the memory percentage used against a cutoff value.

        Arguments:
            (input) cutoff_mem -> Percentage threshold on memory used
            (input) kwargs:
                cutoff_cpu -> Percentage threshold on cpu usage
                cutoff_disk -> Percentage threshold on disk usage
            (output) Return warning message on memory usage

        """

        data = {}

        if cutoff_mem:
            self.cutoff_mem = cutoff_mem

        if self.mem_per_used >= self.cutoff_mem:
            data = {"MemoryWarning":
                    {"Reason": "Have reach memory threshold",
                     "ThresholdPercent": self.cutoff_mem,
                     "TotalMemory":
                         gen_libs.bytes_2_readable(self.mem_total),
                     "MemoryPercentUsage": self.mem_per_used,
                     "MemoryUsed": gen_libs.bytes_2_readable(self.mem_used)}}

        return data

    def chk_nodes(self, **kwargs):

        """Method:  chk_nodes

        Description:  Check for failed nodes in a cluster.

        Arguments:
            (input) kwargs:
                cutoff_cpu -> Percentage threshold on cpu usage
                cutoff_mem -> Percentage threshold on memory used
                cutoff_disk -> Percentage threshold on disk usage
            (output) Return warning message on failed nodes

        """

        data = {}

        if self.failed_nodes > 0:
            data = {"NodeFailure":
                    {"Reason": "Detected failure on one or more nodes",
                     "FailedNodes": self.failed_nodes,
                     "TotalNodes": self.total_nodes}}

        return data

    def chk_shards(self, **kwargs):

        """Method:  chk_shards

        Description:  Check on status of shards in cluster.

        Arguments:
            (input) kwargs:
                cutoff_cpu -> Percentage threshold on cpu usage
                cutoff_mem -> Percentage threshold on memory used
                cutoff_disk -> Percentage threshold on disk usage
            (output) Return warning message on shard problems

        """

        err_flag = False

        data = {"ShardWarning": {}}

        # Shards not assigned to a node
        if self.unassigned_shards > 0:
            err_flag = True

            data["ShardWarning"]["UnassignedShards"] = \
                {"Reason": "Detected unassigned shards",
                 "Unassigned": self.unassigned_shards,
                 "Total": self.num_shards}

        # How much of shards is not active
        if self.active_shards_percent < 100:
            err_flag = True

            data["ShardWarning"]["ActiveShardsPercent"] = \
                {"Reason": "Detected less than 100% active shards",
                 "Percentage": self.active_shards_percent}

        # List of shards not in running in operations
        shards = [x for x in self.shard_list if x[3] != "STARTED"]

        if shards:
            err_flag = True

            data["ShardWarning"]["NonOperationShards"] = \
                {"Reason": "Detected shards not in operational mode",
                 "ListofShards": shards}

        return data if err_flag else {}

    def chk_server(self, cutoff_cpu=None, **kwargs):

        """Method:  chk_server

        Description:  Checks the server status.

        Arguments:
            (input) cutoff_cpu -> Percentage threshold on cpu usage
            (input) kwargs:
                cutoff_mem -> Percentage threshold on memory used
                cutoff_disk -> Percentage threshold on disk usage
            (output) Return warning message on server status

        """

        data = {}

        if cutoff_cpu:
            self.cutoff_cpu = cutoff_cpu

        if self.cpu_active >= self.cutoff_cpu:
            data = {"ServerWarning":
                    {"Reason": "Have reach cpu threshold",
                     "Threshold": self.cutoff_cpu,
                     "TotalCPUs": self.alloc_cpu,
                     "CPUUsage": self.cpu_active}}

        return data

    def chk_status(self, **kwargs):

        """Method:  chk_status

        Description:  Checks the cluster status.

        Arguments:
            (input) kwargs:
                cutoff_cpu -> Percentage threshold on cpu usage
                cutoff_mem -> Percentage threshold on memory used
                cutoff_disk -> Percentage threshold on disk usage
            (output) Return warning message on cluster status

        """

        err_flag = False

        data = {"ClusterWarning": {}}

        # Elasticsearch cluster status
        if self.cluster_status != "green":
            err_flag = True

            data["ClusterWarning"]["ClusterStatus"] = \
                {"Reason": "Detected the cluster is not green",
                 "Status": self.cluster_status}

        # Cluster's pending tasks
        if self.pending_tasks > 0:
            err_flag = True

            data["ClusterWarning"]["PendingTasks"] = \
                {"Reason": "Detected cluster has pending tasks",
                 "Tasks": self.pending_tasks}

        return data if err_flag else {}

    def chk_disk(self, cutoff_disk=None, **kwargs):

        """Method:  chk_disk

        Description:  Checks the disk usage status.

        Arguments:
            (input) cutoff_disk -> Percentage threshold on disk usage
            (input) kwargs:
                cutoff_cpu -> Percentage threshold on cpu usage
                cutoff_mem -> Percentage threshold on memory used
            (output) data -> Warning messages on disk usage status

        """

        data = {"DiskWarning": {}}

        if cutoff_disk:
            self.cutoff_disk = cutoff_disk

        for node in self.disk_list:
            if int(node["disk.percent"]) >= self.cutoff_disk:
                data["DiskWarning"][node["node"]] = {
                    "Reason": "Have reached disk usage threshold",
                    "ThresholdPercent": self.cutoff_disk,
                    "UsedPercent": node["disk.percent"],
                    "TotalDisk": node["disk.total"],
                    "TotalUsed": node["disk.used"],
                    "Available": node["disk.avail"],
                    "ElasticSearchUsed": node["disk.indices"]}

#            if node[1] != "UNASSIGNED" and int(node[5]) >= self.cutoff_disk:
#                data["DiskWarning"][node[8]] = {
#                    "Reason": "Have reached disk usage threshold",
#                    "ThresholdPercent": self.cutoff_disk,
#                    "UsedPercent": node[5],
#                    "TotalDisk": node[4],
#                    "TotalUsed": node[2],
#                    "Available": node[3],
#                    "ElasticSearchUsed": node[1]}

        return data if data["DiskWarning"] else {}

    def chk_all(self, cutoff_cpu=None, cutoff_mem=None, cutoff_disk=None):

        """Method:  chk_all

        Description:  Check status of all elements.

        Arguments:
            (input) cutoff_cpu -> Percentage threshold on cpu usage
            (input) cutoff_mem -> Percentage threshold on memory used
            (input) cutoff_disk -> Percentage threshold on disk usage
            (output) Return any messages from all element check

        """

        # List of methods to be called
        func_list = [self.chk_mem, self.chk_nodes, self.chk_shards,
                     self.chk_server, self.chk_status, self.chk_disk]
        data = {}
        cutoff_cpu = cutoff_cpu if cutoff_cpu else self.cutoff_cpu
        cutoff_mem = cutoff_mem if cutoff_mem else self.cutoff_mem
        cutoff_disk = cutoff_disk if cutoff_disk else self.cutoff_disk

        for func in func_list:
            results = func(cutoff_cpu=cutoff_cpu, cutoff_mem=cutoff_mem,
                           cutoff_disk=cutoff_disk)

            if results:
                data, _, _ = gen_libs.merge_two_dicts(data, results)

        if data:
            data, _, _ = gen_libs.merge_two_dicts(data, self.get_cluster())

        return data
