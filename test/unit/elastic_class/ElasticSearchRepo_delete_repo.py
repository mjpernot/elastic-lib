#!/usr/bin/python
# Classification (U)

"""Program:  ElasticSearchRepo_delete_repo.py

    Description:  Unit testing of delete_repo in
        elastic_class.ElasticSearchRepo class.

    Usage:
        test/unit/elastic_class/ElasticSearchRepo_delete_repo.py

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
        self.info_status = {"cluster_name":
                            "ClusterName", "name": "servername"}
        self.snapshot = Repo()

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
        test_repo_name_failed -> Test with repo name failed to delete.
        test_repo_name_none -> Test with repo name set to None.
        test_no_repo_name -> Test with no repo name passed.
        test_not_deleted -> Test with repository not being deleted.
        test_default -> Test with default settings.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.host_list = ["host1", "host2"]
        self.repo = "reponame"
        self.repo2 = "reponame2"
        self.repo3 = "reponame3"
        self.es = Elasticsearch(self.host_list)
        self.err_msg = "ERROR:  Repository still detected:  reponame"
        self.nodes_data = {"serverid1": {"name": "hostname1", "settings":
            {"path": {"data": ["/dir/data1"], "logs": ["/dir/logs1"]}}},
            "serverid2": {"name": "hostname2", "settings":
            {"path": {"data": ["/dir/data2"], "logs": ["/dir/logs2"]}}}}
        self.health_data = {"status": "green", "cluster_name": "ClusterName"}
        self.repo_list = {"reponame": {"type": "dbdump", "settings":
                {"location": "/dir/path/dump"}}}

    @mock.patch("elastic_class.is_active", mock.Mock(return_value=True))
    @mock.patch("elastic_class.delete_snapshot_repo",
                mock.Mock(return_value={"acknowledged": False}))
    @mock.patch("elastic_class.get_cluster_nodes",
                mock.Mock(return_value={"_nodes": {"total": 3}}))
    @mock.patch("elastic_class.get_master_name",
                mock.Mock(return_value="MasterName"))
    @mock.patch("elastic_class.get_info",
                mock.Mock(return_value={"name": "localservername"}))
    @mock.patch("elastic_class.get_repo_list")
    @mock.patch("elastic_class.get_cluster_health")
    @mock.patch("elastic_class.get_nodes")
    @mock.patch("elastic_class.elasticsearch.Elasticsearch")
    def test_repo_name_failed(self, mock_es, mock_nodes, mock_health,
                              mock_list):

        """Function:  test_repo_name_failed

        Description:  Test with repo name failed to delete.

        Arguments:

        """

        mock_es.return_value = self.es
        mock_nodes.return_value = self.nodes_data
        mock_health.return_value = self.health_data
        mock_list.return_value = self.repo_list

        es = elastic_class.ElasticSearchRepo(self.host_list, repo=self.repo)
        es.repo_dict = {"reponame":
                        {"type": "dbdump", "settings":
                         {"location": "/dir/path/dump"}},
                        "reponame2":
                        {"type": "dbdump", "settings":
                         {"location": "/dir/path/dump2"}}}
        es.repo_dict[self.repo3] = True

        self.assertEqual(es.delete_repo(self.repo3),
            (True, "ERROR:  Repository deletion failed:  reponame3"))

    @mock.patch("elastic_class.is_active", mock.Mock(return_value=True))
    @mock.patch("elastic_class.delete_snapshot_repo",
                mock.Mock(return_value={"acknowledged": True}))
    @mock.patch("elastic_class.get_cluster_nodes",
                mock.Mock(return_value={"_nodes": {"total": 3}}))
    @mock.patch("elastic_class.get_master_name",
                mock.Mock(return_value="MasterName"))
    @mock.patch("elastic_class.get_info",
                mock.Mock(return_value={"name": "localservername"}))
    @mock.patch("elastic_class.get_repo_list")
    @mock.patch("elastic_class.get_cluster_health")
    @mock.patch("elastic_class.get_nodes")
    @mock.patch("elastic_class.elasticsearch.Elasticsearch")
    def test_repo_name_none(self, mock_es, mock_nodes, mock_health, mock_list):

        """Function:  test_repo_name_none

        Description:  Test with repo name set to None.

        Arguments:

        """

        mock_es.return_value = self.es
        mock_nodes.return_value = self.nodes_data
        mock_health.return_value = self.health_data
        mock_list.return_value = self.repo_list

        es = elastic_class.ElasticSearchRepo(self.host_list, repo=self.repo)
        es.repo_dict = {"reponame":
                        {"type": "dbdump", "settings":
                         {"location": "/dir/path/dump"}},
                        "reponame2":
                        {"type": "dbdump", "settings":
                         {"location": "/dir/path/dump2"}}}
        es.repo = None

        self.assertEqual(es.delete_repo(),
            (True, "ERROR: Missing repo or does not exist: None"))

    @mock.patch("elastic_class.is_active", mock.Mock(return_value=True))
    @mock.patch("elastic_class.delete_snapshot_repo",
                mock.Mock(return_value={"acknowledged": True}))
    @mock.patch("elastic_class.get_cluster_nodes",
                mock.Mock(return_value={"_nodes": {"total": 3}}))
    @mock.patch("elastic_class.get_master_name",
                mock.Mock(return_value="MasterName"))
    @mock.patch("elastic_class.get_info",
                mock.Mock(return_value={"name": "localservername"}))
    @mock.patch("elastic_class.get_repo_list")
    @mock.patch("elastic_class.get_cluster_health")
    @mock.patch("elastic_class.get_nodes")
    @mock.patch("elastic_class.elasticsearch.Elasticsearch")
    def test_no_repo_name(self, mock_es, mock_nodes, mock_health, mock_list):

        """Function:  test_no_repo_name

        Description:  Test with no repo name passed.

        Arguments:

        """

        mock_es.return_value = self.es
        mock_nodes.return_value = self.nodes_data
        mock_health.return_value = self.health_data
        mock_list.return_value = self.repo_list

        es = elastic_class.ElasticSearchRepo(self.host_list, repo=self.repo)
        es.repo_dict = {"reponame":
                        {"type": "dbdump", "settings":
                         {"location": "/dir/path/dump"}},
                        "reponame2":
                        {"type": "dbdump", "settings":
                         {"location": "/dir/path/dump2"}}}

        self.assertEqual(es.delete_repo(self.repo2), (False, None))

    @mock.patch("elastic_class.is_active", mock.Mock(return_value=True))
    @mock.patch("elastic_class.delete_snapshot_repo",
                mock.Mock(return_value={"acknowledged": True}))
    @mock.patch("elastic_class.get_cluster_nodes",
                mock.Mock(return_value={"_nodes": {"total": 3}}))
    @mock.patch("elastic_class.get_master_name",
                mock.Mock(return_value="MasterName"))
    @mock.patch("elastic_class.get_info",
                mock.Mock(return_value={"name": "localservername"}))
    @mock.patch("elastic_class.get_repo_list")
    @mock.patch("elastic_class.get_cluster_health")
    @mock.patch("elastic_class.get_nodes")
    @mock.patch("elastic_class.elasticsearch.Elasticsearch")
    def test_not_deleted(self, mock_es, mock_nodes, mock_health, mock_list):

        """Function:  test_not_deleted

        Description:  Test with repository not being deleted.

        Arguments:

        """

        mock_es.return_value = self.es
        mock_nodes.return_value = self.nodes_data
        mock_health.return_value = self.health_data
        mock_list.return_value = self.repo_list

        es = elastic_class.ElasticSearchRepo(self.host_list, repo=self.repo)

        self.assertEqual(es.delete_repo(self.repo), (True, self.err_msg))

    @mock.patch("elastic_class.is_active", mock.Mock(return_value=True))
    @mock.patch("elastic_class.delete_snapshot_repo",
                mock.Mock(return_value={"acknowledged": True}))
    @mock.patch("elastic_class.get_cluster_nodes",
                mock.Mock(return_value={"_nodes": {"total": 3}}))
    @mock.patch("elastic_class.get_master_name",
                mock.Mock(return_value="MasterName"))
    @mock.patch("elastic_class.get_info",
                mock.Mock(return_value={"name": "localservername"}))
    @mock.patch("elastic_class.get_repo_list")
    @mock.patch("elastic_class.get_cluster_health")
    @mock.patch("elastic_class.get_nodes")
    @mock.patch("elastic_class.elasticsearch.Elasticsearch")
    def test_default(self, mock_es, mock_nodes, mock_health, mock_list):

        """Function:  test_default

        Description:  Test with default settings.

        Arguments:

        """

        mock_es.return_value = self.es
        mock_nodes.return_value = self.nodes_data
        mock_health.return_value = self.health_data
        mock_list.return_value = self.repo_list

        es = elastic_class.ElasticSearchRepo(self.host_list, repo=self.repo)
        es.repo_dict = {"reponame":
                        {"type": "dbdump", "settings":
                         {"location": "/dir/path/dump"}},
                        "reponame2":
                        {"type": "dbdump", "settings":
                         {"location": "/dir/path/dump2"}}}

        self.assertEqual(es.delete_repo(self.repo2), (False, None))


if __name__ == "__main__":
    unittest.main()
