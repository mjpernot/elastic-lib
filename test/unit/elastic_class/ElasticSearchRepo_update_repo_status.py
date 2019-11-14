#!/usr/bin/python
# Classification (U)

"""Program:  ElasticSearchRepo_update_repo_status.py

    Description:  Unit testing of update_repo_status in
        elastic_class.ElasticSearchDump.

    Usage:
        test/unit/elastic_class/ElasticSearchRepo_update_repo_status.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os

if sys.version_info < (2, 7):
    import unittest2 as unittest
else:
    import unittest

# Third-party
import mock

# Local
sys.path.append(os.getcwd())
import elastic_class
import lib.gen_libs as gen_libs
import version

__version__ = version.__version__


class Repo2(object):

    """Class:  Repo2

    Description:  Class representation of the snapshot class.

    Methods:
        get_repository -> Stub holder for snapshot.get_repository method.

    """

    def get_repository(self):

        """Method:  get_repository

        Description:  Stub holder for snapshot.get_repository method.

        Arguments:

        """

        return {"reponame": {"type": "dbdump", "settings":
                             {"location": "/dir/path/dump"}},
                "reponame2": {"type": "dbdump2", "settings":
                             {"location": "/dir/path/dump2"}}}


class Repo(object):

    """Class:  Repo

    Description:  Class representation of the snapshot class.

    Methods:
        get_repository -> Stub holder for snapshot.get_repository method.

    """

    def get_repository(self):

        """Method:  get_repository

        Description:  Stub holder for snapshot.get_repository method.

        Arguments:

        """

        return {"reponame": {"type": "dbdump", "settings":
                             {"location": "/dir/path/dump"}}}


class Elasticsearch(object):

    """Class:  ElasticSearch

    Description:  Class representation of the Elasticsearch class.

    Methods:
        __init__ -> Initialize configuration environment.
        ping -> Stub holder for Elasticsearch.ping method.
        info -> Stub holder for Elasticsearch.info method.

    """

    def __init__(self, host_list, port=9200):

        """Method:  __init__

        Description:  Initialization instance of the class.

        Arguments:

        """

        self.hosts = host_list
        self.port = port
        self.ping_status = True
        self.info_status = {"cluster_name": "ClusterName",
                            "name": "servername"}
        self.snapshot = Repo()

    def ping(self):

        """Method:  ping

        Description:  Stub holder for Elasticsearch.ping method.

        Arguments:

        """

        return self.ping_status

    def info(self):

        """Method:  info

        Description:  Stub holder for Elasticsearch.info method.

        Arguments:

        """

        return self.info_status


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Initialization for unit testing.
        test_repo_not_present -> Test with repo not present.
        test_default -> Test with default settings.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.host_list = ["host1", "host2"]
        self.host_str = "host1, host2"
        self.repo = "reponame"
        self.repo2 = "reponame2"
        self.es = Elasticsearch(self.host_list)
        self.dump_list = ["dump1", "dump2"]
        self.nodes_data = {"serverid1": {"name": "hostname1", "settings":
            {"path": {"data": ["/dir/data1"], "logs": ["/dir/logs1"]}}},
            "serverid2": {"name": "hostname2", "settings":
            {"path": {"data": ["/dir/data2"], "logs": ["/dir/logs2"]}}}}
        self.health_data = {"status": "green", "cluster_name": "ClusterName"}
        self.last_dump = "dump2"

    @mock.patch("elastic_class.get_cluster_nodes",
                mock.Mock(return_value={"_nodes": {"total": 3}}))
    @mock.patch("elastic_class.get_master_name",
                mock.Mock(return_value="MasterName"))
    @mock.patch("elastic_class.get_info",
                mock.Mock(return_value={"name": "localservername"}))
    @mock.patch("elastic_class.elastic_libs.get_latest_dump",
                mock.Mock(return_value= "dump2"))
    @mock.patch("elastic_class.is_active", mock.Mock(return_value=True))
    @mock.patch("elastic_class.get_cluster_health")
    @mock.patch("elastic_class.get_nodes")
    @mock.patch("elastic_class.get_dump_list")
    @mock.patch("elastic_class.elasticsearch.Elasticsearch")
    def test_repo_not_present(self, mock_es, mock_list, mock_nodes,
                              mock_health):

        """Function:  test_repo_not_present

        Description:  Test with repo not present.

        Arguments:

        """

        mock_es.return_value = self.es
        mock_list.return_value = self.dump_list
        mock_nodes.return_value = self.nodes_data
        mock_health.return_value = self.health_data

        es = elastic_class.ElasticSearchRepo(self.host_list, repo=self.repo2)
        self.assertEqual((es.hosts, es.dump_list, es.repo_name,
                          es.last_dump_name), (self.host_list, [], None, None))

    @mock.patch("elastic_class.get_master_name",
                mock.Mock(return_value="MasterName"))
    @mock.patch("elastic_class.get_cluster_nodes",
                mock.Mock(return_value={"_nodes": {"total": 3}}))
    @mock.patch("elastic_class.get_info",
                mock.Mock(return_value={"name": "localservername"}))
    @mock.patch("elastic_class.is_active", mock.Mock(return_value=True))
    @mock.patch("elastic_class.get_cluster_health")
    @mock.patch("elastic_class.get_nodes")
    @mock.patch("elastic_class.get_dump_list")
    @mock.patch("elastic_class.elasticsearch.Elasticsearch")
    def test_default(self, mock_es, mock_list, mock_nodes, mock_health):

        """Function:  test_default

        Description:  Test with default settings.

        Arguments:

        """

        mock_es.return_value = self.es
        mock_list.return_value = self.dump_list
        mock_nodes.return_value = self.nodes_data
        mock_health.return_value = self.health_data

        es = elastic_class.ElasticSearchRepo(self.host_list, repo=self.repo)
        self.assertEqual((es.hosts, es.dump_list, es.repo_name),
                         (self.host_list, self.dump_list, self.repo))


if __name__ == "__main__":
    unittest.main()
