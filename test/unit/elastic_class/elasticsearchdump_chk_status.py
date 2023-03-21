# Classification (U)

"""Program:  elasticsearchdump_chk_status.py

    Description:  Unit testing of _chk_status in
        elastic_class.ElasticSearchDump class.

    Usage:
        test/unit/elastic_class/elasticsearchdump_chk_status.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import unittest
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
        __init__
        get_repository
        create

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.repository = None
        self.body = None
        self.snapshot = None

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

        """

        self.repository = repository
        self.body = body
        self.snapshot = snapshot

        return True


class Elasticsearch(object):

    """Class:  ElasticSearch

    Description:  Class representation of the Elasticsearch class.

    Methods:
        __init__
        ping
        info

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
        setUp
        test_unknown_dump
        test_failed_dump
        test_partial_dump
        test_incompatible_dump
        test_in_progress_dump
        test_success_dump

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
        self.break_flag = False
        self.nodes_data = {"serverid1": {"name": "hostname1", "settings":
                                         {"path": {"data": ["/dir/data1"],
                                                   "logs": ["/dir/logs1"]}}},
                           "serverid2": {"name": "hostname2", "settings":
                                         {"path": {"data": ["/dir/data2"],
                                                   "logs": ["/dir/logs2"]}}}}
        self.health_data = {"status": "green", "cluster_name": "ClusterName"}
        self.get_dump_list = (
            [{"snapshot": "dump1", "state": "SUCCESS",
              "shards": {"failed": 0}},
             {"snapshot": "dump2", "state": "SUCCESS",
              "shards": {"failed": 0}},
             {"snapshot": "dump3", "state": "SUCCESS",
              "shards": {"failed": 0}}], True, None)
        self.get_dump_list2 = (
            [{"snapshot": "dump1", "state": "SUCCESS",
              "shards": {"failed": 0}},
             {"snapshot": "dump2", "state": "SUCCESS",
              "shards": {"failed": 0}},
             {"snapshot": "dump3", "state": "IN_PROGRESS",
              "shards": {"failed": 0}}], True, None)
        self.get_dump_list3 = (
            [{"snapshot": "dump1", "state": "SUCCESS",
              "shards": {"failed": 0}},
             {"snapshot": "dump2", "state": "SUCCESS",
              "shards": {"failed": 0}},
             {"snapshot": "dump3", "state": "INCOMPATIBLE",
              "shards": {"failed": 0}}], True, None)
        self.get_dump_list4 = (
            [{"snapshot": "dump1", "state": "SUCCESS",
              "shards": {"failed": 0}},
             {"snapshot": "dump2", "state": "SUCCESS",
              "shards": {"failed": 0}},
             {"snapshot": "dump3", "state": "PARTIAL",
              "shards": {"failed": 0}}], True, None)
        self.get_dump_list5 = (
            [{"snapshot": "dump1", "state": "SUCCESS",
              "shards": {"failed": 0}},
             {"snapshot": "dump2", "state": "SUCCESS",
              "shards": {"failed": 0}},
             {"snapshot": "dump3", "state": "FAILED",
              "shards": {"failed": 0}}], True, None)
        self.get_dump_list6 = (
            [{"snapshot": "dump1", "state": "SUCCESS",
              "shards": {"failed": 0}},
             {"snapshot": "dump2", "state": "SUCCESS",
              "shards": {"failed": 0}},
             {"snapshot": "dump3", "state": "UNKNOWN",
              "shards": {"failed": 0}}], True, None)

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

        mock_es.return_value = self.els
        mock_list.return_value = self.get_dump_list6
        mock_nodes.return_value = self.nodes_data
        mock_health.return_value = self.health_data

        els = elastic_class.ElasticSearchDump(self.host_list, repo=self.repo)
        els.connect()
        els.dump_name = "dump3"
        self.assertEqual(
            els._chk_status(self.break_flag),
            (True, "Unknown error 'UNKNOWN' detected on reponame", False))

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

        mock_es.return_value = self.els
        mock_list.return_value = self.get_dump_list5
        mock_nodes.return_value = self.nodes_data
        mock_health.return_value = self.health_data

        els = elastic_class.ElasticSearchDump(self.host_list, repo=self.repo)
        els.connect()
        els.dump_name = "dump3"
        self.assertEqual(
            els._chk_status(self.break_flag),
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
    def test_partial_dump(self, mock_es, mock_list, mock_nodes, mock_health):

        """Function:  test_partial_dump

        Description:  Test with dump returning Partial.

        Arguments:

        """

        mock_es.return_value = self.els
        mock_list.return_value = self.get_dump_list4
        mock_nodes.return_value = self.nodes_data
        mock_health.return_value = self.health_data

        els = elastic_class.ElasticSearchDump(self.host_list, repo=self.repo)
        els.connect()
        els.dump_name = "dump3"
        self.assertEqual(
            els._chk_status(self.break_flag),
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
                               mock_health):

        """Function:  test_incompatible_dump

        Description:  Test with dump returning Incompatible.

        Arguments:

        """

        mock_es.return_value = self.els
        mock_list.return_value = self.get_dump_list3
        mock_nodes.return_value = self.nodes_data
        mock_health.return_value = self.health_data

        els = elastic_class.ElasticSearchDump(self.host_list, repo=self.repo)
        els.connect()
        els.dump_name = "dump3"
        self.assertEqual(
            els._chk_status(self.break_flag),
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
                              mock_health):

        """Function:  test_in_progress_dump

        Description:  Test with dump returning In Progress/Success.

        Arguments:

        """

        mock_es.return_value = self.els
        mock_list.return_value = self.get_dump_list2
        mock_nodes.return_value = self.nodes_data
        mock_health.return_value = self.health_data

        els = elastic_class.ElasticSearchDump(self.host_list, repo=self.repo)
        els.connect()
        els.dump_name = "dump3"
        self.assertEqual(
            els._chk_status(self.break_flag), (False, None, False))

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
    def test_success_dump(self, mock_es, mock_list, mock_nodes, mock_health):

        """Function:  test_success_dump

        Description:  Test with dump returning Success.

        Arguments:

        """

        mock_es.return_value = self.els
        mock_list.return_value = self.get_dump_list
        mock_nodes.return_value = self.nodes_data
        mock_health.return_value = self.health_data

        els = elastic_class.ElasticSearchDump(self.host_list, repo=self.repo)
        els.connect()
        els.dump_name = "dump3"
        self.assertEqual(els._chk_status(self.break_flag), (False, None, True))


if __name__ == "__main__":
    unittest.main()
