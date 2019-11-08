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

        Elastic (deprecated)
            ElasticCluster (deprecated)
                ElasticDump (deprecated)
                ElasticStatus (deprecated)

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
import requests_lib.requests_libs as requests_libs
import version

__version__ = version.__version__


def create_snapshot(es, reponame, body, dumpname, **kwargs):

    """Function:  create_snapshot

    Description:  Runs a dump of a named repository.

    Arguments:
        (input) es -> ElasticSearch instance.
        (input) reponame -> Name of repository.
        (input) body -> Contains arguments for the dump command.
        (input) dumpname -> Dump name which it will be dumped too.

    """

    body = dict(body)
    es.snapshot.create(repository=reponame, body=body, snapshot=dumpname)


def create_snapshot_repo(es, reponame, body, verify=True, **kwargs):

    """Function:  create_snapshot_repo

    Description:  Creates a repository in Elasticsearch cluster.

    Arguments:
        (input) es -> ElasticSearch instance.
        (input) reponame -> Name of repository.
        (input) body -> Contains arguments for the dump command.
        (input) verify -> True|False - Validate the repository.
        (output) Return exit status of create_repository command.

    """

    body = dict(body)
    return es.snapshot.create_repository(repository=reponame, body=body,
                                         verify=verify)


def delete_snapshot(es, reponame, dumpname, **kwargs):

    """Function:  delete_snapshot

    Description:  Deltes a dump in a named repository.

    Arguments:
        (input) es -> ElasticSearch instance.
        (input) reponame -> Name of repository.
        (input) dumpname -> Dump name to be deleted.

    """

    es.snapshot.delete(repository=reponame, snapshot=dumpname)


def delete_snapshot_repo(es, reponame, **kwargs):

    """Function:  delete_snapshot_repo

    Description:  Deletes named repository in Elasticsearch cluster.

    Arguments:
        (input) es -> ElasticSearch instance.
        (input) reponame -> Name of repository.

    """

    es.snapshot.delete(repository=reponame)


def get_cluster_health(es, **kwargs):

    """Function:  get_cluster_health

    Description:  Return a dict of information on Elasticsearch cluster health.

    Arguments:
        (input) es -> ElasticSearch instance.
        (output) Dictionary of information on Elasticsearch cluster health.

    """

    return es.cluster.health()


def get_cluster_nodes(es, **kwargs):

    """Function:  get_cluster_nodes

    Description:  Return a dict of information on Elasticsearch cluster nodes.

    Arguments:
        (input) es -> ElasticSearch instance.
        (output) Dictionary of information on Elasticsearch cluster nodes.

    """

    return es.nodes.info()


def get_cluster_stats(es, **kwargs):

    """Function:  get_cluster_stats

    Description:  Return a dict of information on Elasticsearch cluster stats.

    Arguments:
        (input) es -> ElasticSearch instance.
        (output) Dictionary of information on Elasticsearch cluster stats.

    """

    return es.cluster.stats()


def get_cluster_status(es, **kwargs):

    """Function:  get_cluster_status

    Description:  Return status of the Elasticsearch cluster.

    Arguments:
        (input) es -> ElasticSearch instance.
        (output) Status of the Elasticsearch cluster.

    """

    return es.cluster.health()["status"]


def get_disks(es, **kwargs):

    """Function:  get_disks

    Description:  Return a list of disks within the Elasticsearch cluster.

    Arguments:
        (input) es -> ElasticSearch instance.
        (output) List of ElasticSearch disks.

    """

    return [x.split() for x in es.cat.allocation().splitlines()]


def get_dump_list(es, repo, **kwargs):

    """Function:  get_dump_list

    Description:  Return a list of dumps within a named repository.

    Arguments:
        (input) es -> ElasticSearch instance.
        (input) repo -> Name of repository.
        (output) List of ElasticSearch dumps.

    """

    return [x.split() for x in es.cat.snapshots(repository=repo).splitlines()]


def get_info(es, **kwargs):

    """Function:  get_info

    Description:  Return a dictionary of a basic Elasticsearch info command.

    Arguments:
        (input) es -> ElasticSearch instance.
        (output) Dictionary of basic Elasticsearch info command.

    """

    return es.info()


def get_master_name(es, **kwargs):

    """Function:  get_master_name

    Description:  Return name of the master node in a Elasticsearch cluster.

    Arguments:
        (input) es -> ElasticSearch instance.
        (output) Name of master node in ElasticSearch cluster.

    """

    return es.cat.master().strip().split(" ")[-1]


def get_nodes(es, **kwargs):

    """Function:  get_nodes

    Description:  Return a dictionary of information on Elasticsearch nodes.

    Arguments:
        (input) es -> ElasticSearch instance.
        (output) Dictionary of information on Elasticsearch nodes.

    """

    return es.nodes.info()["nodes"]


def get_repo_list(es, **kwargs):

    """Function:  get_repo_list

    Description:  Return a dictionary of a list of Elasticsearch repositories.

    Arguments:
        (input) es -> ElasticSearch instance.
        (output) Dictionary of a list of Elasticsearch repositories.

    """

    return es.snapshot.get_repository()


def get_shards(es, **kwargs):

    """Function:  get_shards

    Description:  Return a list of shards within the Elasticsearch cluster.

    Arguments:
        (input) es -> ElasticSearch instance.
        (output) List of ElasticSearch shards.

    """

    return [x.split() for x in es.cat.shards().splitlines()]


def is_active(es, **kwargs):

    """Function:  is_active

    Description:  Returns True or False if the Elasticsearch cluster is up.

    Arguments:
        (input) es -> ElasticSearch instance.
        (output) True|False - Elasticsearch cluster is up.

    """

    return es.ping()


class ElasticSearch(object):

    """Class:  ElasticSearch

    Description:  Class which is a representation of an ElasticSearch
        database/cluster.  An ElasticSearch object is used as proxy to
        implement the connecting to an execute commands in an ElasticSearch
        database/cluster.

    Methods:
        __init__ -> Class instance initialization.
        update_status -> Update class attributes by querying Elasticsearch.

    """

    def __init__(self, host_list, port=9200, **kwargs):

        """Method:  __init__

        Description:  Initialization of an instance of the ElasticSearch class.

        Arguments:
            (input) host_list -> List of host(s) within ElasticSearch cluster.
            (input) port -> ElasticSearch port to connect to.

        """

        self.port = port
        self.hosts = list(host_list)
        self.cluster_name = None
        self.node_connected_to = None
        self.es = None
        self.is_connected = False
        self.data = {}
        self.logs = {}
        self.nodes = []
        self.total_nodes = None
        self.cluster_status = None
        self.master = None
        self.es = elasticsearch.Elasticsearch(self.hosts, port=self.port)

        self.update_status()

    def update_status(self, **kwargs):

        """Method:  update_status

        Description:  Update class attributes by querying Elasticsearch.

        Arguments:

        """

        if is_active(self.es):
            self.is_connected = True

            # Basic information
            info = get_info(self.es)

            self.node_connected_to = info["name"]

            # Node information
            data = get_nodes(self.es)

            for x in data:
                self.data[data[x]["name"]] = \
                    data[x]["settings"]["path"]["data"]
                self.logs[data[x]["name"]] = \
                    data[x]["settings"]["path"]["logs"]

            self.nodes = [data[x]["name"] for x in data]

            # Cluster node information
            cluster = get_cluster_nodes(self.es)

            self.total_nodes = cluster["_nodes"]["total"]

            # Cluster health information
            health = get_cluster_health(self.es)

            self.cluster_status = health["status"]
            self.cluster_name = health["cluster_name"]

            # Master information
            self.master = get_master_name(self.es)

        else:
            self.is_connected = False


class ElasticSearchDump(ElasticSearch):

    """Class:  ElasticSearchDump

    Description:  Class which is a representation of ElasticSearch database
        dump.  An ElasticSearchDump object is used as proxy to implement a
        database dump of an ElasticSearch database/cluster.

    Methods:
        __init__ -> Class instance initilization.
        dump_db -> Executes a dump of an ElasticSearch database.

    """

    def __init__(self, host_list, port=9200, repo=None, **kwargs):

        """Method:  __init__

        Description:  Initialization of an instance of the ElasticSearchDump
            class.

        Arguments:
            (input) host_list -> List of host(s) within ElasticSearch cluster.
            (input) port -> ElasticSearch database port.
            (input) repo -> Name of repository.  Required if multiple
                repositories are present in the cluster.

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

        if self.es:
            self.dump_name = self.cluster_name.lower() + "_bkp_" + \
                datetime.datetime.strftime(datetime.datetime.now(),
                                           "%Y%m%d-%H%M%S")

            # Query dump repository
            repo_dict = self.es.snapshot.get_repository()

            # Repo does not exist in repository.
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
                self.dump_loc = \
                    repo_dict[self.repo_name]["settings"]["location"]
                self.dump_list = get_dump_list(self.es, self.repo_name)

            if self.dump_list:
                self.last_dump_name = \
                    elastic_libs.get_latest_dump(self.dump_list)

            # Make sure new dump name is unique.
            if self.dump_name == self.last_dump_name:
                time.sleep(1)
                self.dump_name = self.cluster_name.lower() + "_bkp_" + \
                    datetime.datetime.strftime(datetime.datetime.now(),
                                               "%Y%m%d-%H%M%s")

    def dump_db(self, dbs=None, **kwargs):

        """Method:  dump_db

        Description:  Executes a dump of an ElasticSearch database.

        Arguments:
            (input) dbs -> String of database(s) to dump, comma delimited.
            (output) err_flag True|False -> Were errors detected during dump.
            (output) status_msg -> Dump error message.

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
            self.es.snapshot.create(repository=self.repo_name, body=body,
                                    snapshot=self.dump_name)

            while not break_flag and not err_flag:

                err_flag, status_msg, break_flag = self._chk_status(break_flag)

            self.dump_list = get_dump_list(self.es, self.repo_name)
            self.last_dump_name = elastic_libs.get_latest_dump(self.dump_list)

        elif not err_flag:
            err_flag = True
            status_msg = "ERROR:  Repository name not set."

        return err_flag, status_msg

    def _chk_status(self, break_flag):

        """Function:  _chk_status

        Description:  Check status of database dump.

        Arguments:
            (input) break_flag True|False -> Break out of loop for check.
            (output) err_flag True|False -> Were errors detected during dump.
            (output) status_msg -> Dump error message.
            (output) break_flag True|False -> Break out of loop for check.

        """

        err_flag = False
        status_msg = None

        for dump in get_dump_list(self.es, self.repo_name):

            if self.dump_name == dump[0]:

                self.dump_status, self.failed_shards = self._parse(dump)

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
                    status_msg = "Unknown error detected on %s" \
                                 % (self.repo_name)
                    err_flag = True

        return err_flag, status_msg, break_flag

    def _parse(self, dump, **kwargs):

        """Function:  _parse

        Description:  Parse the dump entry for status and shard.

        Arguments:
            (input)  dump -> Dump entry.
            (output) Return dump status.
            (output) Return shard failures.

        """

        return dump[1], dump[9]


class ElasticSearchRepo(ElasticSearch):

    """Class:  ElasticSearchRepo

    Description:  Class which is a representation of ElasticSearchRepo
        repositories.  An ElasticSearchRepo object is used as proxy to
        implement respositories within an Elasticsearch cluster.

    Methods:
        __init__ -> Class instance initilization.
        create_repo -> Create an elasticsearch dump repository.
        delete_repo -> Delete an elasticsearch dump repository.
        delete_dump -> Delete a database dump in an Elasticsearch repository.
        delete_dump_all -> Delete all dumps in a repository.

    """

    def __init__(self, host_list, port=9200, repo=None, repo_dir=None,
                 **kwargs):

        """Method:  __init__

        Description:  Initialization of an instance of the ElasticSearchRepo
            class.

        Arguments:
            (input) host_list -> List of host(s) within ElasticSearch cluster.
            (input) port -> ElasticSearch database port.
            (input) repo -> Name of repository.
            (input) repo_dir -> Directory path to respository.

        """

        host_list = list(host_list)
        super(ElasticSearchRepo, self).__init__(host_list, port, **kwargs)

        self.repo = repo
        self.repo_dir = repo_dir
        self.repo_dict = None

        if self.es:

            # Query dump repository
            self.repo_dict = self.es.snapshot.get_repository()

    def create_repo(self, repo_name=None, repo_dir=None, **kwargs):

        """Method:  create_repo

        Description:  Create an elasticsearch dump repository.

        Arguments:
            (input) repo_name -> Name of repository.
            (input) repo_dir -> Directory path to respository.
            (output) err_flag -> True|False - Error status for repo creation.
            (output) err_msg -> Status error message or None.

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

            status = create_snapshot_repo(self.es, repo_name, data_dict, True)

            if not status["acknowledged"]:
                err_flag = True
                err_msg = "ERROR:  Repository creation failure:  %s, %s" \
                          % (repo_name, repo_dir)

            else:
                # Update repo dictionary.
                self.repo_dict = self.es.snapshot.get_repository()

                if repo_name not in self.repo_dict:
                    err_flag = True
                    err_msg = "ERROR:  Repository not detected:  %s, %s" \
                              % (repo_name, repo_dir)

        else:
            err_flag = True
            err_msg = "ERROR: Missing repo name or directory: '%s', '%s'" \
                      % (repo_name, repo_dir)

        return err_flag, err_msg

    def delete_repo(self, repo_name=None, **kwargs):

        """Method:  delete_repo

        Description:  Delete an elasticsearch dump repository.

        Arguments:
            (input) repo -> Name of repository.
            (output) err_flag -> True|False - Error status for repo deletion.
            (output) err_msg -> Status error message or None.

        """

        err_flag = False
        err_msg = None

        if not repo_name:
            repo_name = self.repo

        if repo_name and repo_name in self.repo_dict:

            status = self.es.snapshot.delete_repository(
                repository=repo_name)

            if not status["acknowledged"]:
                err_flag = True
                err_msg = "ERROR:  Repository deletion failed:  %s" \
                          % (repo_name)

            else:
                # Update repo dictionary.
                self.repo_dict = self.es.snapshot.get_repository()

                if repo_name in self.repo_dict:
                    err_flag = True
                    err_msg = "ERROR:  Repository still detected:  %s" \
                              % (repo_name)

        else:
            err_flag = True
            err_msg = "ERROR: Missing repo or does not exist: %s" % (repo_name)

        return err_flag, err_msg

    def delete_dump(self, repo_name=None, dump_name=None, **kwargs):

        """Method:  delete_dump

        Description:  Delete a database dump in an Elasticsearch repository.

        Arguments:
            (input) repo_name -> Name of repository.
            (input) dump_name -> Name of dump.
            (output) err_flag -> True|False - Error status for deletion.
            (output) err_msg -> Status error message or None.

        """

        err_flag = False
        err_msg = None

        if not repo_name:
            repo_name = self.repo

        if repo_name and dump_name and repo_name in self.repo_dict:

            # See if the dump exists.
            if dump_name in [x[0] for x in get_dump_list(self.es, repo_name)]:

                status = self.es.snapshot.delete(repository=repo_name,
                                                 snapshot=dump_name)

                if not status["acknowledged"]:
                    err_flag = True
                    err_msg = "ERROR:  Dump deletion failed:  %s, %s" \
                              % (repo_name, dump_name)

                else:
                    # See if the dump still exists.
                    if dump_name in [x[0] for x in get_dump_list(self.es,
                                                                 repo_name)]:

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

    def delete_dump_all(self, repo_name=None, **kwargs):

        """Method:  delete_dump_all

        Description:  Delete all dumps in a repository.

        Arguments:
            (input)  repo_name -> Name of repository.
            (output) err_flag -> True|False - Error status for deletion.
            (output) err_msg -> Status error message or None.

        """

        err_flag = False
        err_msg = None

        if not repo_name:
            repo_name = self.repo

        if repo_name and repo_name in self.repo_dict:

            for dump in [x[0] for x in get_dump_list(self.es, repo_name)]:

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
        __init__ -> Class instance initilization.
        update_status -> Update class attributes by querying Elasticsearch.
        get_cluster -> Return formatted cluster name.
        get_nodes -> Return formatted list of node names.
        get_node_status -> Return status of nodes.
        get_svr_status -> Return status of server.
        get_mem_status -> Return status of memory on the server.
        get_shrd_status -> Return status of shards in the cluster.
        get_gen_status -> Return general status in the cluster.
        get_disk_status -> Return status of disk usage for each node.
        get_dump_disk_status -> Return status of dump disk usage for each repo.
        get_all -> Call get_ functions and return as single result set.
        chk_mem -> Checks the memory percentage used against a cutoff value.
        chk_nodes -> Check status of nodes in cluster.
        chk_shards -> Check status of shards in cluster.
        chk_server -> Check status of the server.
        chk_status -> Check status of the cluster.
        chk_disk -> Check status of disk usage on each node.
        chk_all - Calls all chk_ functions and return as a single result set.

    """

    def __init__(self, hostname, port=9200, cutoff_mem=90, cutoff_cpu=75,
                 cutoff_disk=85, **kwargs):

        """Method:  __init__

        Description:  Initialization of an instance of ElasticSearchStatus
            class.

        Arguments:
            (input) hostname -> Hostname of Elasticsearch database node.
            (input) port -> Elasticsearch database port.  Default = 9200.
            (input) cutoff_mem -> Threshold cutoff for memory check.
            (input) cutoff_cpu -> Threshold cutoff for cpu usage check.
            (input) cutoff_disk -> Threshold cutoff for disk usage check.

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

        self.update_status()

    def update_status(self, **kwargs):

        """Method:  update_status

        Description:  Update class attributes by querying Elasticsearch.

        Arguments:

        """

        if is_active(self.es):
            self.is_connected = True

            # Get cluster health
            health = get_cluster_health(self.es)

            self.unassigned_shards = health["unassigned_shards"]
            self.active_shards_percent = \
                health["active_shards_percent_as_number"]
            self.pending_tasks = health["number_of_pending_tasks"]
            self.num_shards = health["active_shards"]
            self.num_primary = health["active_primary_shards"]

            # Get cluster shards
            self.shard_list = get_shards(self.es)

            # Get cluster status
            status = get_cluster_status(self.es)

            self.failed_nodes = status["_nodes"]["failed"]
            self.mem_per_used = status["nodes"]["os"]["mem"]["used_percent"]
            self.mem_total = status["nodes"]["os"]["mem"]["total_in_bytes"]
            self.mem_used = status["nodes"]["os"]["mem"]["used_in_bytes"]
            self.mem_free = status["nodes"]["os"]["mem"]["free_in_bytes"]
            self.uptime = status["nodes"]["jvm"]["max_uptime_in_millis"]
            self.alloc_cpu = status["nodes"]["os"]["allocated_processors"]
            self.cpu_active = status["nodes"]["process"]["cpu"]["percent"]

            # Get disks usage
            self.disk_list = get_disks(self.es)

            # Get repository list
            self.repo_dict = get_repo_list(self.es)

        else:
            self.is_connected = False

    def get_cluster(self, **kwargs):

        """Method:  get_cluster

        Description:  Return dictionary format of cluster name.

        Arguments:
            (output) Dictionary of cluster name

        """

        return {"Cluster": self.cluster_name}

    def get_nodes(self, **kwargs):

        """Method:  get_nodes

        Description:  Return dictionary format of a list of node names.

        Arguments:
            (output) Dictionary list of node names

        """

        return {"Nodes": [str(x) for x in self.nodes]}

    def get_node_status(self, **kwargs):

        """Method:  get_node_status

        Description:  Return dictionary format of status of nodes.

        Arguments:
            (output) Return dictionary format of status of nodes in cluster.

        """

        return {"NodeStatus": {"TotalNodes": self.total_nodes,
                               "FailedNodes": self.failed_nodes}}

    def get_svr_status(self, **kwargs):

        """Method:  get_svr_status

        Description:  Return dictionary format of status of server.

        Arguments:
            (output) Return dictionary dictionary format of status of server.

        """

        return {"Server": {"Uptime": gen_libs.milli_2_readadble(self.uptime),
                           "AllocatedCPU": self.alloc_cpu,
                           "CPUActive": self.cpu_active}}

    def get_mem_status(self, **kwargs):

        """Method:  get_mem_status

        Description:  Return dictionary format of status of memory on server.

        Arguments:
            (output) Return dictionary format of status of memory.

        """

        return {"Memory": {"Percent": self.mem_per_used,
                           "Total": gen_libs.bytes_2_readable(self.mem_total),
                           "Used": gen_libs.bytes_2_readable(self.mem_used),
                           "Free": gen_libs.bytes_2_readable(self.mem_free)}}

    def get_shrd_status(self, **kwargs):

        """Method:  get_shrd_status

        Description:  Return dictionary format of status of shards in cluster.

        Arguments:
            (output) Return dictionary format of status of shards in cluster.

        """

        return {"Shards": {"Percent": self.active_shards_percent,
                           "Unassigned": self.unassigned_shards,
                           "Total": self.num_shards,
                           "Primary": self.num_primary}}

    def get_gen_status(self, **kwargs):

        """Method:  get_shard_status

        Description:  Return dictionary format of general status in cluster.

        Arguments:
            (output) Return dictionary format of general status of cluster.

        """

        return {"ClusterStatus": {"Master": self.master,
                                  "Status": self.cluster_status,
                                  "PendingTasks": self.pending_tasks}}

    def get_disk_status(self, **kwargs):

        """Method:  get_disk_status

        Description:  Return dictionary format of status of disk usage for each
            node.

        Arguments:
            (output) data -> Dictionary format of disk usage status by node.

        """

        data = {"DiskUsage": {}}

        for node in self.disk_list:
            data["DiskUsage"][node[8]] = {
                "Total": node[4], "Available": node[3],
                "TotalUsed": node[2], "ESUsed": node[1], "Percent": node[5]}

        return data

    def get_dump_disk_status(self, **kwargs):

        """Method:  get_dump_disk_status

        Description:  Return dictionary format of status of dump disk usage for
            each repository.

        Arguments:
            (output) data -> Dictionary format of dump disk usage by repo.

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

    def get_all(self, **kwargs):

        """Method:  get_all

        Description:  Return dictionary format of  status of all elements.

        Arguments:
            (output) data -> Dictionary format of status of all elements.

        """

        # List of checks to be called
        func_list = [self.get_nodes, self.get_node_status,
                     self.get_svr_status, self.get_mem_status,
                     self.get_shrd_status, self.get_gen_status,
                     self.get_disk_status]
        data = self.get_cluster()

        for func in func_list:
            results = func()
            data, status, msg = gen_libs.merge_two_dicts(data, results)

        return data

    def chk_mem(self, cutoff_mem=None, **kwargs):

        """Method:  chk_mem

        Description:  Checks the memory percentage used against a cutoff value.

        Arguments:
            (input) cutoff_mem -> Percentage threshold on memory used.
            (output) Return warning message on memory usage.

        """

        if cutoff_mem:
            self.cutoff_mem = cutoff_mem

        if self.mem_per_used >= self.cutoff_mem:
            return {"MemoryWarning":
                    {"Reason": "Have reach memory threshold",
                     "Threshold": self.cutoff_mem,
                     "TotalMemory":
                         gen_libs.bytes_2_readable(self.mem_total),
                     "MemoryUsage": self.mem_per_used}}

        else:
            return {}

    def chk_nodes(self, **kwargs):

        """Method:  chk_nodes

        Description:  Check for failed nodes in a cluster.

        Arguments:
            (output) Return warning message on failed nodes.

        """

        if self.failed_nodes > 0:
            return {"NodeFailure":
                    {"Reason": "Detected failure on one or more nodes",
                     "FailedNodes": self.failed_nodes,
                     "TotalNodes": self.total_nodes}}

        else:
            return {}

    def chk_shards(self, **kwargs):

        """Method:  chk_shards

        Description:  Check on status of shards in cluster.

        Arguments:
            (output) Return warning message on shard problems.

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
            (input) cutoff_cpu -> Percentage threshold on cpu usage.
            (output) Return warning message on server status.

        """

        if cutoff_cpu:
            self.cutoff_cpu = cutoff_cpu

        if self.cpu_active >= self.cutoff_cpu:
            return {"ServerWarning":
                    {"Reason": "Have reach cpu threshold",
                     "Threshold": self.cutoff_cpu,
                     "TotalCPUs": self.alloc_cpu,
                     "CPUUsage": self.cpu_active}}

        else:
            return {}

    def chk_status(self, **kwargs):

        """Method:  chk_status

        Description:  Checks the cluster status.

        Arguments:
            (output) Return warning message on cluster status.

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
            (input) cutoff_disk -> Percentage threshold on disk usage.
            (output) data -> Warning messages on disk usage status.

        """

        err_flag = False

        data = {"DiskWarning": {}}

        if cutoff_disk:
            self.cutoff_disk = cutoff_disk

        for node in self.disk_list:

            if int(node[5]) >= self.cutoff_disk:
                err_flag = True

                data["DiskWarning"][node[8]] = {
                    "Reason": "Have reached disk usage threshold",
                    "Threshold": self.cutoff_disk,
                    "Total": node[4],
                    "Used": node[2],
                    "ESUsed": node[1]}

        return data if err_flag else {}

    def chk_all(self, cutoff_cpu=None, cutoff_mem=None, cutoff_disk=None,
                **kwargs):

        """Method:  chk_all

        Description:  Check status of all elements.

        Arguments:
            (input) cutoff_cpu -> Percentage threshold on cpu usage.
            (input) cutoff_mem -> Percentage threshold on memory used.
            (input) cutoff_disk -> Percentage threshold on disk usage.
            (output) Return any messages from all element check.

        """

        # List of checks to be called
        func_list = [self.chk_mem, self.chk_nodes, self.chk_shards,
                     self.chk_server, self.chk_status, self.chk_disk]
        err_flag = False

        data = self.get_cluster()

        for func in func_list:
            results = func(cutoff_cpu=cutoff_cpu, cutoff_mem=cutoff_mem,
                           cutoff_disk=cutoff_disk)

            if results:
                err_flag = True

                data, status, msg = gen_libs.merge_two_dicts(data, results)

        return data if err_flag else {}


class Elastic(object):

    """Class:  Elastic (deprecated:  Replaced by Elasticsearch class)

    Description:  Class which is a representation of an Elasticsearch database
        node.  An Elastic object is used as proxy to implement the connecting
        to an execute commands in an Elasticsearch database node.
    Methods:
        __init__ -> Class instance initilization.

    """

    def __init__(self, hostname, port=9200, **kwargs):

        """Method:  __init__

        Description:  Initialization of an instance of the Elastic class.

        Arguments:
            (input) hostname -> Hostname of Elasticsearch database node.
            (input) port -> Elasticsearch database port.  Default = 9200.

        """

        self.node = hostname
        self.port = port

        # Query single node
        data = requests_libs.get_query(self.node, self.port,
                                       "/_nodes/" + self.node, "json")["nodes"]

        # Get the Elastic server's node key to acces the settings dictionary.
        self.data = data[next(iter(data))]["settings"]["path"]["data"]
        self.logs = data[next(iter(data))]["settings"]["path"]["logs"]


class ElasticCluster(Elastic):

    """Class:  ElasticCluster (deprecated:  Integrated into ElasticSearch)

    Description:  Class which is a representation of a cluster of
        Elasticsearch database nodes.  An ElasticCluster object is used as a
        proxy to implement connecting to an Elasticsearch database cluster.

    Methods:
        __init__ -> Class instance initilization.

    """

    def __init__(self, hostname, port=9200, **kwargs):

        """Method:  __init__

        Description:  Initialization of an instance of ElasticCluster class.

        Arguments:
            (input) hostname -> Hostname of Elasticsearch database node.
            (input) port -> Elasticsearch database port.  Default = 9200.

        """

        super(ElasticCluster, self).__init__(hostname, port, **kwargs)

        # Query cluster nodes
        data = requests_libs.get_query(self.node, self.port, "/_nodes", "json")

        self.cluster = data["cluster_name"]
        self.nodes = [data["nodes"][x]["name"] for x in data["nodes"]]
        self.total_nodes = data["_nodes"]["total"]

        # Query cluster health
        self.cluster_status = requests_libs.get_query(self.node, self.port,
                                                      "/_cluster/health",
                                                      "json")["status"]

        # Query cluster master
        self.master = [x for x in requests_libs.get_query(self.node,
                                                          self.port,
                                                          "/_cat/master",
                                                          "text")
                       .strip().split(" ")][-1]

        # Query for repositories
        self.repo_list = requests_libs.get_query(self.node, self.port,
                                                 "/_snapshot", "json")


class ElasticDump(ElasticCluster):

    """Class:  ElasticDump (deprecated:  Replaced by ElasticsearchDump class)

    Description:  Class which is a representation of Elasticsearch database
        dump.  An ElasticDump object is used as proxy to implement a database
        dump of an Elasticsearch database node.

    Methods:
        __init__ -> Class instance initilization.
        dump_db -> Dump Elasticsearch database.

    """

    def __init__(self, hostname, repo=None, port=9200, **kwargs):

        """Method:  __init__

        Description:  Initialization of an instance of the ElasticDump class.

        Arguments:
            (input) hostname -> Hostname of Elasticsearch database node.
            (input) repo -> Name of repository.  Required if multiple repos.
            (input) port -> Elasticsearch database port.  Default = 9200.

        """

        super(ElasticDump, self).__init__(hostname, port, **kwargs)

        # Query dump repository
        data = requests_libs.get_query(self.node, self.port, "/_snapshot",
                                       "json")

        self.type = None
        self.dump_loc = None
        self.dump_list = []
        self.last_dump_name = None

        # Passed repo matches existing repo entry
        if repo and repo in data:
            self.repo_name = repo

        # Passed repo name doesn't exist
        elif repo:
            pass

        # If only one entry, then use it
        elif len(data.keys()) == 1:
            self.repo_name = next(iter(data))

        if self.repo_name:
            self.type = data[self.repo_name]["type"]
            self.dump_loc = data[self.repo_name]["settings"]["location"]

            self.dump_list = [x.split() for x in
                              requests_libs.get_query(self.node, self.port,
                                                      "/_cat/snapshots/" +
                                                      self.repo_name,
                                                      "text").splitlines()]

            if self.dump_list:
                # Get latest dump name
                search = max([x[4] for x in self.dump_list])
                for x in self.dump_list:
                    if x[4] == search:
                        self.last_dump_name = x[0]
                        break

        # Pre-dump settings
        self.dump_name = self.cluster.lower() + "_bkp_" \
            + datetime.datetime.strftime(datetime.datetime.now(),
                                         "%Y%m%d-%H%M")

        # Post-dump status
        self.dump_status = None
        self.failed_shards = 0
        self.failures = []

    def dump_db(self, **kwargs):

        """Method:  dump_db

        Description:  Creates and executes a dump of a database, updates the
            status of the dump attributes.

        Arguments:
            (output) err_flag True|False -> Has errors been detected.
            (output) status_msg -> Return dump status or error message.

        """

        err_flag = False
        status_msg = None

        if self.repo_name:
            cmd = "/_snapshot/" + self.repo_name + "/" + self.dump_name \
                  + "?wait_for_completion=true"

            status = requests_libs.put_cmd(self.node, self.port, cmd)

            # Good dump
            if "snapshot" in status.keys():
                status_msg = status["snapshot"]
                self.dump_status = status_msg["state"]
                self.failed_shards = status_msg["shards"]["failed"]
                self.failures = status_msg["failures"]

            # Dump failure for a reason
            elif "status" in status.keys():
                self.dump_status = "FAILURE"
                err_flag = True

                if "error" in status.keys():
                    status_msg = status["error"]["root_cause"][0]["reason"]

                else:
                    status_msg = status

            # Dump failure for unknown reason
            else:
                self.dump_status = "FAILURE"
                err_flag = True
                status_msg = status

        else:
            err_flag = True
            status_msg = "ERROR:  Repository name not set."

        return err_flag, status_msg


class ElasticStatus(ElasticCluster):

    """Class:  ElasticStatus (deprecated:  Replaced by ElasticSearchStatus)

    Description:  Class which is a representation of an Elasticsearch
        cluster status which contains attributes to show the general health of
        the Elasticsearch cluster.  An ElasticStatus is used as a proxy to
        implement connecting to an Elasticsearch database cluster and executing
        status commands.

    Methods:
        __init__ -> Class instance initilization.
        get_cluster -> Return formatted cluster name.
        get_nodes -> Return formatted list of node names.
        get_node_status -> Return status of nodes.
        get_svr_status -> Return status of server.
        get_mem_status -> Return status of memory on the server.
        get_shrd_status -> Return status of shards in the cluster.
        get_gen_status -> Return general status in the cluster.
        get_disk_status -> Return status of disk usage for each node.
        get_dump_disk_status -> Return status of dump disk usage for each repo.
        get_all -> Call get_ functions and return as single result set.
        chk_mem -> Checks the memory percentage used against a cutoff value.
        chk_nodes -> Check status of nodes in cluster.
        chk_shards -> Check status of shards in cluster.
        chk_server -> Check status of the server.
        chk_status -> Check status of the cluster.
        chk_disk -> Check status of disk usage on each node.
        chk_all - Calls all chk_ functions and return as a single result set.

    """

    def __init__(self, hostname, port=9200, cutoff_mem=None, cutoff_cpu=None,
                 cutoff_disk=None, **kwargs):

        """Method:  __init__

        Description:  Initialization of an instance of ElasticStatus class.

        Arguments:
            (input) hostname -> Hostname of Elasticsearch database node.
            (input) port -> Elasticsearch database port.  Default = 9200.
            (input) cutoff_mem -> Threshold cutoff for memory check.
            (input) cutoff_cpu -> Threshold cutoff for cpu usage check.
            (input) cutoff_disk -> Threshold cutoff for disk usage check.

        """

        super(ElasticStatus, self).__init__(hostname, port, **kwargs)

        # Set threshold cutoff attributes
        if cutoff_mem:
            self.cutoff_mem = cutoff_mem

        else:
            self.cutoff_mem = 90

        if cutoff_cpu:
            self.cutoff_cpu = cutoff_cpu

        else:
            self.cutoff_cpu = 75

        if cutoff_disk:
            self.cutoff_disk = cutoff_disk

        else:
            self.cutoff_disk = 85

        # Query cluster health
        data = requests_libs.get_query(self.node, self.port,
                                       "/_cluster/health", "json")

        self.unassigned_shards = data["unassigned_shards"]
        self.active_shards_percent = data["active_shards_percent_as_number"]
        self.pending_tasks = data["number_of_pending_tasks"]
        self.num_shards = data["active_shards"]
        self.num_primary = data["active_primary_shards"]

        # Query cluster shards
        self.shard_list = [x.split() for x in
                           requests_libs.get_query(self.node, self.port,
                                                   "/_cat/shards",
                                                   "text").splitlines()]

        # Query cluster status
        data2 = requests_libs.get_query(self.node, self.port,
                                        "/_cluster/stats", "json")

        self.failed_nodes = data2["_nodes"]["failed"]
        self.mem_per_used = data2["nodes"]["os"]["mem"]["used_percent"]
        self.mem_total = data2["nodes"]["os"]["mem"]["total_in_bytes"]
        self.mem_used = data2["nodes"]["os"]["mem"]["used_in_bytes"]
        self.mem_free = data2["nodes"]["os"]["mem"]["free_in_bytes"]
        self.uptime = data2["nodes"]["jvm"]["max_uptime_in_millis"]
        self.alloc_cpu = data2["nodes"]["os"]["allocated_processors"]
        self.cpu_active = data2["nodes"]["process"]["cpu"]["percent"]

        # Query disk space usage
        self.disk_list = [x.split() for x in
                          requests_libs.get_query(self.node, self.port,
                                                  "/_cat/allocation",
                                                  "text").splitlines()]

    def get_cluster(self, json=False, **kwargs):

        """Method:  get_cluster

        Description:  Return formatted cluster name.

        Arguments:
            (input) json -> True|False - Return output in JSON format.
            (output) Cluster name

        """

        if json:
            return {"Cluster": self.cluster}

        else:
            return "Cluster: %s" % (self.cluster)

    def get_nodes(self, json=False, **kwargs):

        """Method:  get_nodes

        Description:  Return formatted list of node names.

        Arguments:
            (input) json -> True|False - Return output in JSON format.
            (output) List of node names

        """

        if json:
            return {"Nodes": [str(x) for x in self.nodes]}

        else:
            return "Nodes:  %s" % ([str(x) for x in self.nodes])

    def get_node_status(self, json=False, **kwargs):

        """Method:  get_node_status

        Description:  Return status of nodes.

        Arguments:
            (input) json -> True|False - Return output in JSON format.
            (output) Return status of nodes in cluster

        """

        if json:
            return {"Node_Status":
                    {"Total_Nodes": self.total_nodes,
                     "Failed_Nodes": self.failed_nodes}}

        else:
            return "Node_Status\n\tTotal Nodes:  %s\n\tFailed Nodes:  %s" \
                   % (self.total_nodes, self.failed_nodes)

    def get_svr_status(self, json=False, **kwargs):

        """Method:  get_svr_status

        Description:  Return status of server.

        Arguments:
            (input) json -> True|False - Return output in JSON format.
            (output) Return status of server

        """

        if json:
            return {"Server":
                    {"Uptime": gen_libs.milli_2_readadble(self.uptime),
                     "Allocated_CPU": self.alloc_cpu,
                     "CPU_Active": self.cpu_active}}

        else:
            return "Server\n\tUptime: %s\n\tAlloc CPU: %s\n\tCPU Active: %s" \
                   % (gen_libs.milli_2_readadble(self.uptime), self.alloc_cpu,
                      self.cpu_active)

    def get_mem_status(self, json=False, **kwargs):

        """Method:  get_mem_status

        Description:  Return status of memory on the server.

        Arguments:
            (input) json -> True|False - Return output in JSON format.
            (output) Return status of memory

        """

        if json:
            return {"Memory":
                    {"Percent": self.mem_per_used,
                     "Total": gen_libs.bytes_2_readable(self.mem_total),
                     "Used": gen_libs.bytes_2_readable(self.mem_used),
                     "Free": gen_libs.bytes_2_readable(self.mem_free)}}

        else:
            return "Memory\n\tPer: %s\n\tTotal: %s\n\tUsed: %s\n\tFree: %s"\
                   % (self.mem_per_used,
                      gen_libs.bytes_2_readable(self.mem_total),
                      gen_libs.bytes_2_readable(self.mem_used),
                      gen_libs.bytes_2_readable(self.mem_free))

    def get_shrd_status(self, json=False, **kwargs):

        """Method:  get_shrd_status

        Description:  Return status of shards in the cluster.

        Arguments:
            (input) json -> True|False - Return output in JSON format.
            (output) Return status of shards in Elasticsearch cluster

        """

        if json:
            return {"Shards":
                    {"Percent": self.active_shards_percent,
                     "Unassigned": self.unassigned_shards,
                     "Total": self.num_shards, "Primary": self.num_primary}}

        else:
            return "Shards\n\tPercent: %s\n\t" % (self.active_shards_percent) \
                   + "Unassigned: %s\n\tTotal: %s\n\tPrimary: %s" \
                   % (self.unassigned_shards, self.num_shards,
                      self.num_primary)

    def get_gen_status(self, json=False, **kwargs):

        """Method:  get_shard_status

        Description:  Return general status in the cluster.

        Arguments:
            (input) json -> True|False - Return output in JSON format.
            (output) Return general status of Elasticsearch cluster

        """

        if json:
            return {"Cluster_Status":
                    {"Master": self.master, "Status": self.cluster_status,
                     "Pending_Tasks": self.pending_tasks}}

        else:
            return "Cluster\n\tMaster: %s\n\tStatus: %s\n\tPending Tasks: %s" \
                   % (self.master, self.cluster_status, self.pending_tasks)

    def get_disk_status(self, json=False, **kwargs):

        """Method:  get_disk_status

        Description:  Return status of disk usage for each node.

        Arguments:
            (input) json -> True|False - Return output in JSON format.
            (output) data -> Disk usage status by node.

        """

        data = {"Disk_Usage": {}} if json else "Disk Usage"

        for node in self.disk_list:
            if json:
                data["Disk_Usage"][node[8]] = {
                    "Total": node[4], "Available": node[3],
                    "Total_Used": node[2], "ES_Used": node[1],
                    "Percent": node[5]}

            else:
                data = data \
                    + "\n\tNode: %s\n\t\tTotal: %s\n\t\tAvailable: %s\n" \
                    % (node[8], node[4], node[3]) \
                    + "\t\tTotal Used: %s\n\t\tES Used: %s\n" \
                    % (node[2], node[1]) \
                    + "\t\tPercent: %s" % (node[5])

        return data

    def get_dump_disk_status(self, json=False, **kwargs):

        """Method:  get_dump_disk_status

        Description:  Return status of dump disk usage for each repository.

        Arguments:
            (input) json -> True|False - Return output in JSON format.
            (output) data -> Dump disk usage by repository.

        """

        data = {"Dump_Usage": {}} if json else "Dump Usage"

        for repo in self.repo_list:
            partition = self.repo_list[repo]["settings"]["location"]
            usage = gen_libs.disk_usage(partition)

            if json:
                data["Dump_Usage"][repo] = {
                    "Partition": partition,
                    "Total": gen_libs.bytes_2_readable(usage.total),
                    "Used": gen_libs.bytes_2_readable(usage.used),
                    "Free": gen_libs.bytes_2_readable(usage.free),
                    "Percent": (float(usage.used) / usage.total) * 100}

            else:
                data = data + "\n\tRepo: %s\n\t\tPartition: %s\n" \
                    % (repo, partition) \
                    + "\t\tTotal: %s\n\t\tUsed: %s\n\t\tFree: %s\n" \
                    % (gen_libs.bytes_2_readable(usage.total),
                       gen_libs.bytes_2_readable(usage.used),
                       gen_libs.bytes_2_readable(usage.free)) \
                    + "\t\tPercent: %.2f%%" \
                    % ((float(usage.used) / usage.total) * 100)

        return data

    def get_all(self, json=False, **kwargs):

        """Method:  get_all

        Description:  Return status of all elements.

        Arguments:
            (input) json -> True|False - Return output in JSON format.
            (output) data -> Status of all elements.

        """

        # List of checks to be called
        func_list = [self.get_nodes, self.get_node_status,
                     self.get_svr_status, self.get_mem_status,
                     self.get_shrd_status, self.get_gen_status,
                     self.get_disk_status, self.get_dump_disk_status]

        data = self.get_cluster(json)

        for func in func_list:
            results = func(json)

            if json:
                data, status, msg = gen_libs.merge_two_dicts(data, results)

            else:
                data = data + "\n" + results

        return data

    def chk_mem(self, json=False, cutoff_mem=None, **kwargs):

        """Method:  chk_mem

        Description:  Checks the memory percentage used against a cutoff value.

        Arguments:
            (input) json -> True|False - Return output in JSON format.
            (input) cutoff_mem -> Percentage threshold on memory used.
            (output) Return warning message on memory usage

        """

        if cutoff_mem:
            self.cutoff_mem = cutoff_mem

        if self.mem_per_used >= self.cutoff_mem:
            if json:
                return {"Memory_Warning":
                        {"Reason": "Have reach memory threshold",
                         "Threshold": self.cutoff_mem,
                         "Total_Memory":
                             gen_libs.bytes_2_readable(self.mem_total),
                         "Memory_Usage": self.mem_per_used}}

            else:
                return "WARNING:  Have reach %s%% threshold.  " \
                       % (self.cutoff_mem) \
                       + "Currently using %s%% on %s of memory" \
                       % (self.mem_per_used,
                          gen_libs.bytes_2_readable(self.mem_total))

        else:
            return None

    def chk_nodes(self, json=False, **kwargs):

        """Method:  chk_nodes

        Description:  Check for failed nodes in a Elasticsearch cluster.

        Arguments:
            (input) json -> True|False - Return output in JSON format.
            (output) Return warning message on failed nodes

        """

        if self.failed_nodes > 0:
            if json:
                return {"Node_Failure":
                        {"Reason": "Detected failure on one or more nodes",
                         "Failed_Nodes": self.failed_nodes,
                         "Total_Nodes": self.total_nodes}}

            else:
                return "WARNING:  Have detected %s " % (self.failed_nodes) \
                       + "failed nodes out of %s nodes" % (self.total_nodes)

        else:
            return None

    def chk_shards(self, json=False, **kwargs):

        """Method:  chk_shards

        Description:  Check on status of shards in Elasticsearcd cluster.

        Arguments:
            (input) json -> True|False - Return output in JSON format.
            (output) Return warning message on shard problems

        """

        err_flag = False

        data = {"Shard_Warning": {}} if json else "Shard_Warning:"

        # Shards not assigned to a node
        if self.unassigned_shards > 0:
            err_flag = True

            if json:
                data["Shard_Warning"]["Unassigned_Shards"] = \
                    {"Reason": "Detected unassigned shards",
                     "Unassigned": self.unassigned_shards,
                     "Total": self.num_shards}

            else:
                data = data + "\n"
                data = data \
                    + "WARNING: Detected %s " % (self.unassigned_shards) \
                    + "unassigned shards out of %s shards" % (self.num_shards)

        # How much of shards is not active
        if self.active_shards_percent < 100:
            err_flag = True

            if json:
                data["Shard_Warning"]["Active_Shards_Percent"] = \
                    {"Reason": "Detected less than 100% active shards",
                     "Percentage": self.active_shards_percent}

            else:
                data = data + "\n"
                data = data + "WARNING: Currently active shards at %s%%" \
                    % (self.active_shards_percent)

        # List of shards not in running in operations
        shards = [x for x in self.shard_list if x[3] != "STARTED"]

        if shards:
            err_flag = True

            if json:
                data["Shard_Warning"]["Non_Operation_Shards"] = \
                    {"Reason": "Detected shards not in operational mode",
                     "List_Of_Shards": shards}

            else:
                data = data + "\n"
                data = data \
                    + "WARNING: Detected shards in non-operation mode:" \
                    + "\n" + "\n".join(str(x) for x in shards)

        return data if err_flag else None

    def chk_server(self, json=False, cutoff_cpu=None, **kwargs):

        """Method:  chk_server

        Description:  Checks the server status.

        Arguments:
            (input) json -> True|False - Return output in JSON format.
            (input) cutoff_cpu -> Percentage threshold on cpu usage.
            (output) Return warning message on server status

        """

        if cutoff_cpu:
            self.cutoff_cpu = cutoff_cpu

        if self.cpu_active >= self.cutoff_cpu:
            if json:
                return {"Server_Warning":
                        {"Reason": "Have reach cpu threshold",
                         "Threshold": self.cutoff_cpu,
                         "Total_CPUs": self.alloc_cpu,
                         "CPU_Usage": self.cpu_active}}

            else:
                return "WARNING:  Have reach %s%% threshold.  " \
                       % (self.cutoff_cpu) \
                       + "Currently using %s%% on %s CPUs" \
                       % (self.cpu_active, self.alloc_cpu)

        else:
            return None

    def chk_status(self, json=False, **kwargs):

        """Method:  chk_status

        Description:  Checks the cluster status.

        Arguments:
            (input) json -> True|False - Return output in JSON format.
            (output) Return warning message on cluster status

        """

        err_flag = False

        data = {"Cluster_Warning": {}} if json else ""

        # Elasticsearch cluster status
        if self.cluster_status != "green":
            err_flag = True

            if json:
                data["Cluster_Warning"]["Cluster_Status"] = \
                    {"Reason": "Detected the cluster is not green",
                     "Status": self.cluster_status}

            else:
                data = data + "WARNING: Detected Cluster status is %s" \
                    % (self.cluster_status)

        # Cluster's pending tasks
        if self.pending_tasks > 0:
            err_flag = True

            if json:
                data["Cluster_Warning"]["Pending_Tasks"] = \
                    {"Reason": "Detected cluster has pending tasks",
                     "Tasks": self.pending_tasks}

            else:
                if data:
                    data = data + "\n"

                data = data + "WARNING: Detected Cluster has %s " \
                    % (self.pending_tasks) + "pending tasks"

        return data if err_flag else None

    def chk_disk(self, json=False, cutoff_disk=None, **kwargs):

        """Method:  chk_disk

        Description:  Checks the disk usage status.

        Arguments:
            (input) json -> True|False - Return output in JSON format.
            (input) cutoff_disk -> Percentage threshold on disk usage.
            (output) data -> Warning messages on disk usage status

        """

        err_flag = False

        data = {"Disk_Warning": {}} if json else "Disk Warning\n"

        if cutoff_disk:
            self.cutoff_disk = cutoff_disk

        for node in self.disk_list:

            if int(node[5]) >= self.cutoff_disk:
                err_flag = True

                if json:
                    data["Disk_Warning"][node[8]] = {
                        "Reason": "Have reached disk usage threshold",
                        "Threshold": self.cutoff_disk,
                        "Total": node[4],
                        "Used": node[2],
                        "ES_Used": node[1]}

                else:
                    data = data \
                        + "\n\tNode: %s" \
                        % (node[8]) \
                        + "\n\t\tHave reached disk usage threshold" \
                        + "\n\t\tThreshold: %s\n\t\tTotal: %s\n" \
                        % (self.cutoff_disk, node[4]) \
                        + "\t\tUsed: %s\n\t\tES Used: %s\n" \
                        % (node[2], node[1])

        return data if err_flag else None

    def chk_all(self, json=False, cutoff_cpu=None, cutoff_mem=None,
                cutoff_disk=None, **kwargs):

        """Method:  chk_all

        Description:  Check status of all elements.

        Arguments:
            (input) json -> True|False - Return output in JSON format.
            (input) cutoff_cpu -> Percentage threshold on cpu usage.
            (input) cutoff_mem -> Percentage threshold on memory used.
            (input) cutoff_disk -> Percentage threshold on disk usage.
            (output) Return any messages from all element check.

        """

        # List of checks to be called
        func_list = [self.chk_mem, self.chk_nodes, self.chk_shards,
                     self.chk_server, self.chk_status, self.chk_disk]
        err_flag = False

        data = self.get_cluster(json)

        for func in func_list:
            results = func(json, cutoff_cpu=cutoff_cpu, cutoff_mem=cutoff_mem,
                           cutoff_disk=cutoff_disk)

            if results:
                err_flag = True

                if json:
                    data, status, msg = gen_libs.merge_two_dicts(data, results)

                else:
                    data = data + "\n" + results

        return data if err_flag else None
