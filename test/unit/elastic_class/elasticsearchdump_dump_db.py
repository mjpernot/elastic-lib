#!/usr/bin/python
# Classification (U)

"""Program:  elasticsearchdump_dump_db.py

    Description:  Unit testing of dump_db in elastic_class.ElasticSearchDump.

    Usage:
        test/unit/elastic_class/elasticsearchdump_dump_db.py

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
import version

__version__ = version.__version__


class Repo(object):

    """Class:  Repo

    Description:  Class representation of the snapshot class.

    Methods:
        get_repository

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
        __init__
        info

    """

    def __init__(self, host_list, port=9200):

        """Method:  __init__

        Description:  Initialization instance of the class.

        Arguments:

        """

        self.hosts = host_list
        self.port = port
        self.info_status = {"cluster_name": "ClusterName",
                            "name": "servername"}
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
        setUp
        test_no_repo_name
        test_bad_db_name
        test_default

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.host_list = ["host1", "host2"]
        self.host_str = "host1, host2"
        self.repo = "reponame"
        self.els = Elasticsearch(self.host_list)
        self.dbs = "dbname"
        self.dbs2 = ["dbname"]
        self.nodes_data = {"serverid1": {"name": "hostname1", "settings":
                                         {"path": {"data": ["/dir/data1"],
                                                   "logs": ["/dir/logs1"]}}},
                           "serverid2": {"name": "hostname2", "settings":
                                         {"path": {"data": ["/dir/data2"],
                                                   "logs": ["/dir/logs2"]}}}}
        self.health_data = {"status": "green", "cluster_name": "ClusterName"}

    @mock.patch("elastic_class.is_active", mock.Mock(return_value=True))
    @mock.patch("elastic_class.create_snapshot", mock.Mock())
    @mock.patch("elastic_class.get_cluster_nodes",
                mock.Mock(return_value={"_nodes": {"total": 3}}))
    @mock.patch("elastic_class.get_master_name",
                mock.Mock(return_value="MasterName"))
    @mock.patch("elastic_class.get_info",
                mock.Mock(return_value={"name": "localservername"}))
    @mock.patch("elastic_class.elastic_libs.get_latest_dump",
                mock.Mock(side_effect=["dump2", "dump3"]))
    @mock.patch("elastic_class.ElasticSearchDump._chk_status",
                mock.Mock(return_value=(False, None, True)))
    @mock.patch("elastic_class.get_cluster_health")
    @mock.patch("elastic_class.get_nodes")
    @mock.patch("elastic_class.get_dump_list")
    @mock.patch("elastic_class.elasticsearch.Elasticsearch")
    def test_no_repo_name(self, mock_es, mock_list, mock_nodes, mock_health):

        """Function:  test_no_repo_name

        Description:  Test with no repo name set.

        Arguments:

        """

        mock_es.return_value = self.els
        mock_list.side_effect = [["dump1", "dump2"],
                                 ["dump1", "dump2", "dump3"]]
        mock_nodes.return_value = self.nodes_data
        mock_health.return_value = self.health_data

        els = elastic_class.ElasticSearchDump(self.host_list, repo=self.repo)
        els.repo_name = None
        self.assertEqual(
            els.dump_db(self.dbs),
            (True, "ERROR:  Repository name not set."))

    @mock.patch("elastic_class.is_active", mock.Mock(return_value=True))
    @mock.patch("elastic_class.create_snapshot", mock.Mock())
    @mock.patch("elastic_class.get_cluster_nodes",
                mock.Mock(return_value={"_nodes": {"total": 3}}))
    @mock.patch("elastic_class.get_master_name",
                mock.Mock(return_value="MasterName"))
    @mock.patch("elastic_class.get_info",
                mock.Mock(return_value={"name": "localservername"}))
    @mock.patch("elastic_class.elastic_libs.get_latest_dump",
                mock.Mock(side_effect=["dump2", "dump3"]))
    @mock.patch("elastic_class.ElasticSearchDump._chk_status",
                mock.Mock(return_value=(False, None, True)))
    @mock.patch("elastic_class.get_cluster_health")
    @mock.patch("elastic_class.get_nodes")
    @mock.patch("elastic_class.get_dump_list")
    @mock.patch("elastic_class.elasticsearch.Elasticsearch")
    def test_bad_db_name(self, mock_es, mock_list, mock_nodes, mock_health):

        """Function:  test_bad_db_name

        Description:  Test with bad database name.

        Arguments:

        """

        mock_es.return_value = self.els
        mock_list.side_effect = [["dump1", "dump2"],
                                 ["dump1", "dump2", "dump3"]]
        mock_nodes.return_value = self.nodes_data
        mock_health.return_value = self.health_data

        els = elastic_class.ElasticSearchDump(self.host_list, repo=self.repo)
        self.assertEqual(
            els.dump_db(self.dbs2),
            (True, "ERROR:  Database name(s) is not a string: ['dbname']"))

    @mock.patch("elastic_class.is_active", mock.Mock(return_value=True))
    @mock.patch("elastic_class.create_snapshot", mock.Mock())
    @mock.patch("elastic_class.get_cluster_nodes",
                mock.Mock(return_value={"_nodes": {"total": 3}}))
    @mock.patch("elastic_class.get_master_name",
                mock.Mock(return_value="MasterName"))
    @mock.patch("elastic_class.get_info",
                mock.Mock(return_value={"name": "localservername"}))
    @mock.patch("elastic_class.elastic_libs.get_latest_dump",
                mock.Mock(side_effect=["dump2", "dump3"]))
    @mock.patch("elastic_class.ElasticSearchDump._chk_status",
                mock.Mock(return_value=(False, None, True)))
    @mock.patch("elastic_class.get_cluster_health")
    @mock.patch("elastic_class.get_nodes")
    @mock.patch("elastic_class.get_dump_list")
    @mock.patch("elastic_class.elasticsearch.Elasticsearch")
    def test_default(self, mock_es, mock_list, mock_nodes, mock_health):

        """Function:  test_default

        Description:  Test with default settings.

        Arguments:

        """

        mock_es.return_value = self.els
        mock_list.side_effect = [["dump1", "dump2"],
                                 ["dump1", "dump2", "dump3"]]
        mock_nodes.return_value = self.nodes_data
        mock_health.return_value = self.health_data

        els = elastic_class.ElasticSearchDump(self.host_list, repo=self.repo)
        self.assertEqual(els.dump_db(self.dbs), (False, None))


if __name__ == "__main__":
    unittest.main()
