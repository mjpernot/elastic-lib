#!/usr/bin/python
# Classification (U)

"""Program:  ElasticSearchDump_chk_status.py

    Description:  Unit testing of _chk_status in
        elastic_class.ElasticSearchDump class.

    Usage:
        test/unit/elastic_class/ElasticSearchDump_chk_status.py

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
        create -> Stub holder for snapshot.create method.

    """

    def get_repository(self):

        """Method:  get_repository

        Description:  Stub holder for snapshot.get_repository method.

        Arguments:

        """

        return {"reponame": {"type": "dbdump", "settings":
                             {"location": "/dir/path/dump"}}}

    def create(self, repository, body, snapshot):

        """Method:  create

        Description:  Stub holder for snapshot.create method.

        Arguments:
            (input) repository -> Repository name.
            (input) body -> Database dump command.
            (input) snapshot -> Database dump respository information.

        """

        return True


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
        test_unknown_dump -> Test with dump returning Unknown error.
        test_failed_dump -> Test with dump returning Failed.
        test_partial_dump -> Test with dump returning Partial.
        test_incompatible_dump -> Test with dump returning Incompatible.
        test_in_progress_dump -> Test with dump returning In Progress/Success.
        test_success_dump -> Test with dump returning Success.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.host_list = ["host1", "host2"]
        self.host_str = "host1, host2"
        self.repo = "reponame"
        self.es = Elasticsearch(self.host_list)
        self.break_flag = False
        self.nodes_data = {"serverid1": {"name": "hostname1", "settings":
            {"path": {"data": ["/dir/data1"], "logs": ["/dir/logs1"]}}},
            "serverid2": {"name": "hostname2", "settings":
            {"path": {"data": ["/dir/data2"], "logs": ["/dir/logs2"]}}}}
        self.info_data = {"name": "localservername"}
        self.health_data = {"status": "green", "cluster_name": "ClusterName"}
        self.master_name = "MasterName"
        self.cluster_data = {"_nodes": {"total": 3}}

    @mock.patch("elastic_class.get_cluster_nodes",
                mock.Mock(return_value={"_nodes": {"total": 3}}))
    @mock.patch("elastic_class.get_master_name",
                mock.Mock(return_value="MasterName"))
    @mock.patch("elastic_class.get_info",
                mock.Mock(return_value={"name": "localservername"}))
    @mock.patch("elastic_class.elastic_libs.get_latest_dump",
                mock.Mock(side_effect=["dump2", "dump3"]))
    @mock.patch("elastic_class.get_cluster_health")
    @mock.patch("elastic_class.get_nodes")
    @mock.patch("elastic_class.get_dump_list")
    @mock.patch("elastic_class.elasticsearch.Elasticsearch")
    def test_unknown_dump(self, mock_es, mock_list, mock_nodes, mock_health):

        """Function:  test_unknown_dump

        Description:  Test with dump returning Unknown error.

        Arguments:

        """

        mock_es.return_value = self.es
        mock_list.side_effect = [["dump1", "dump2"], [["dump1"], ["dump2"],
            ["dump3", "UNKNOWN", None, None, None, None, None, None, None, 0]]]
        mock_nodes.return_value = self.nodes_data
        mock_health.return_value = self.health_data

        es = elastic_class.ElasticSearchDump(self.host_list, repo=self.repo)
        es.dump_name = "dump3"
        self.assertEqual(es._chk_status(self.break_flag),
            (True, "Unknown error detected on reponame", False))


    @mock.patch("elastic_class.get_cluster_nodes",
                mock.Mock(return_value={"_nodes": {"total": 3}}))
    @mock.patch("elastic_class.get_master_name",
                mock.Mock(return_value="MasterName"))
    @mock.patch("elastic_class.get_info",
                mock.Mock(return_value={"name": "localservername"}))
    @mock.patch("elastic_class.elastic_libs.get_latest_dump",
                mock.Mock(side_effect=["dump2", "dump3"]))
    @mock.patch("elastic_class.get_cluster_health")
    @mock.patch("elastic_class.get_nodes")
    @mock.patch("elastic_class.get_dump_list")
    @mock.patch("elastic_class.elasticsearch.Elasticsearch")
    def test_failed_dump(self, mock_es, mock_list, mock_nodes, mock_health):

        """Function:  test_failed_dump

        Description:  Test with dump returning Failed.

        Arguments:

        """

        mock_es.return_value = self.es
        mock_list.side_effect = [["dump1", "dump2"], [["dump1"], ["dump2"],
            ["dump3", "FAILED", None, None, None, None, None, None, None, 0]]]
        mock_nodes.return_value = self.nodes_data
        mock_health.return_value = self.health_data


        es = elastic_class.ElasticSearchDump(self.host_list, repo=self.repo)
        es.dump_name = "dump3"
        self.assertEqual(es._chk_status(self.break_flag),
            (True, "Dump failed to finish on reponame", False))

    @mock.patch("elastic_class.get_cluster_nodes",
                mock.Mock(return_value={"_nodes": {"total": 3}}))
    @mock.patch("elastic_class.get_master_name",
                mock.Mock(return_value="MasterName"))
    @mock.patch("elastic_class.get_info",
                mock.Mock(return_value={"name": "localservername"}))
    @mock.patch("elastic_class.elastic_libs.get_latest_dump",
                mock.Mock(side_effect=["dump2", "dump3"]))
    @mock.patch("elastic_class.get_cluster_health")
    @mock.patch("elastic_class.get_nodes")
    @mock.patch("elastic_class.get_dump_list")
    @mock.patch("elastic_class.elasticsearch.Elasticsearch")
    def test_partial_dump(self, mock_es, mock_list, mock_nodes, mock_cluster):

        """Function:  test_partial_dump

        Description:  Test with dump returning Partial.

        Arguments:

        """

        mock_es.return_value = self.es
        mock_list.side_effect = [["dump1", "dump2"], [["dump1"], ["dump2"],
            ["dump3", "PARTIAL", None, None, None, None, None, None, None, 0]]]
        mock_nodes.return_value = self.nodes_data
        mock_health.return_value = self.health_data

        es = elastic_class.ElasticSearchDump(self.host_list, repo=self.repo)
        es.dump_name = "dump3"
        self.assertEqual(es._chk_status(self.break_flag),
            (True, "Partial dump completed on reponame", False))

    @mock.patch("elastic_class.get_cluster_nodes",
                mock.Mock(return_value={"_nodes": {"total": 3}}))
    @mock.patch("elastic_class.get_master_name",
                mock.Mock(return_value="MasterName"))
    @mock.patch("elastic_class.get_info",
                mock.Mock(return_value={"name": "localservername"}))
    @mock.patch("elastic_class.elastic_libs.get_latest_dump",
                mock.Mock(side_effect=["dump2", "dump3"]))
    @mock.patch("elastic_class.get_cluster_health")
    @mock.patch("elastic_class.get_nodes")
    @mock.patch("elastic_class.get_dump_list")
    @mock.patch("elastic_class.elasticsearch.Elasticsearch")
    def test_incompatible_dump(self, mock_es, mock_list, mock_nodes,
                               mock_cluster):

        """Function:  test_incompatible_dump

        Description:  Test with dump returning Incompatible.

        Arguments:

        """

        mock_es.return_value = self.es
        mock_list.side_effect = [["dump1", "dump2"], [["dump1"], ["dump2"],
            ["dump3", "INCOMPATIBLE", None, None, None, None, None, None, None,
             0]]]
        mock_nodes.return_value = self.nodes_data
        mock_health.return_value = self.health_data

        es = elastic_class.ElasticSearchDump(self.host_list, repo=self.repo)
        es.dump_name = "dump3"
        self.assertEqual(es._chk_status(self.break_flag),
            (True, "Older version of ES detected: reponame", False))

    @mock.patch("elastic_class.get_cluster_nodes",
                mock.Mock(return_value={"_nodes": {"total": 3}}))
    @mock.patch("elastic_class.get_master_name",
                mock.Mock(return_value="MasterName"))
    @mock.patch("elastic_class.get_info",
                mock.Mock(return_value={"name": "localservername"}))
    @mock.patch("elastic_class.elastic_libs.get_latest_dump",
                mock.Mock(side_effect=["dump2", "dump3"]))
    @mock.patch("elastic_class.get_cluster_health")
    @mock.patch("elastic_class.get_nodes")
    @mock.patch("elastic_class.get_dump_list")
    @mock.patch("elastic_class.elasticsearch.Elasticsearch")
    def test_in_progress_dump(self, mock_es, mock_list, mock_nodes,
                              mock_cluster):

        """Function:  test_in_progress_dump

        Description:  Test with dump returning In Progress/Success.

        Arguments:

        """

        mock_es.return_value = self.es
        mock_list.side_effect = [["dump1", "dump2"], [["dump1"], ["dump2"],
            ["dump3", "IN_PROGRESS", None, None, None, None, None, None, None,
             0],
            ["dump3", "SUCCESS", None, None, None, None, None, None, None, 0]]]
        mock_nodes.return_value = self.nodes_data
        mock_health.return_value = self.health_data

        es = elastic_class.ElasticSearchDump(self.host_list, repo=self.repo)
        es.dump_name = "dump3"
        self.assertEqual(es._chk_status(self.break_flag), (False, None, True))

    @mock.patch("elastic_class.get_cluster_nodes",
                mock.Mock(return_value={"_nodes": {"total": 3}}))
    @mock.patch("elastic_class.get_master_name",
                mock.Mock(return_value="MasterName"))
    @mock.patch("elastic_class.get_info",
                mock.Mock(return_value={"name": "localservername"}))
    @mock.patch("elastic_class.elastic_libs.get_latest_dump",
                mock.Mock(side_effect=["dump2", "dump3"]))
    @mock.patch("elastic_class.get_cluster_health")
    @mock.patch("elastic_class.get_nodes")
    @mock.patch("elastic_class.get_dump_list")
    @mock.patch("elastic_class.elasticsearch.Elasticsearch")
    def test_success_dump(self, mock_es, mock_list, mock_nodes, mock_cluster):

        """Function:  test_success_dump

        Description:  Test with dump returning Success.

        Arguments:

        """

        mock_es.return_value = self.es
        mock_list.side_effect = [["dump1", "dump2"], [["dump1"], ["dump2"],
            ["dump3", "SUCCESS", None, None, None, None, None, None, None, 0]]]
        mock_nodes.return_value = self.nodes_data
        mock_health.return_value = self.health_data

        es = elastic_class.ElasticSearchDump(self.host_list, repo=self.repo)
        es.dump_name = "dump3"
        self.assertEqual(es._chk_status(self.break_flag), (False, None, True))


if __name__ == "__main__":
    unittest.main()
