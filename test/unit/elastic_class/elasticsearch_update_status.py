#!/usr/bin/python
# Classification (U)

"""Program:  elasticsearch_update_status.py

    Description:  Unit testing of update_status in elastic_class.ElasticSearch.

    Usage:
        test/unit/elastic_class/elasticsearch_update_status.py

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
        self.ping_status = True
        self.info_status = {"cluster_name":
                            "ClusterName", "name": "servername"}

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
        test_single_node
        test_multiple_nodes
        test_update_status

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        dir_data = "/dir/data1"
        dir_log = "/dir/logs1"
        self.host_list = ["host1", "host2"]
        self.els = Elasticsearch(self.host_list)
        self.nodes_data = {"serverid1": {"name": "hostname1", "settings":
                                         {"path": {"data": [dir_data],
                                                   "logs": [dir_log]}}},
                           "serverid2": {"name": "hostname2", "settings":
                                         {"path":
                                          {"data": ["/dir/data2"],
                                           "logs": ["/dir/logs2"]}}}}
        self.nodes_data2 = {"serverid1": {"name": "hostname1", "settings":
                                          {"path": {"data": [dir_data],
                                                    "logs": [dir_log]}}}}
        self.info_data = {"name": "localservername"}
        self.health_data = {"status": "green", "cluster_name": "ClusterName"}
        self.master_name = "MasterName"
        self.cluster_data = {"_nodes": {"total": 3}}
        self.data_results = {"hostname1": [dir_data],
                             "hostname2": ["/dir/data2"]}
        self.logs_results = {"hostname1": [dir_log],
                             "hostname2": ["/dir/logs2"]}

    @mock.patch("elastic_class.is_active", mock.Mock(return_value=True))
    @mock.patch("elastic_class.get_cluster_nodes")
    @mock.patch("elastic_class.get_master_name")
    @mock.patch("elastic_class.get_cluster_health")
    @mock.patch("elastic_class.get_info")
    @mock.patch("elastic_class.get_nodes")
    @mock.patch("elastic_class.elasticsearch.Elasticsearch")
    def test_single_node(self, mock_es, mock_nodes, mock_info, mock_health,
                         mock_master, mock_cluster):

        """Function:  test_single_node

        Description:  Test with one node.

        Arguments:

        """

        mock_es.return_value = self.els
        mock_nodes.return_value = self.nodes_data2
        mock_info.return_value = self.info_data
        mock_health.return_value = self.health_data
        mock_master.return_value = self.master_name
        mock_cluster.return_value = self.cluster_data

        els = elastic_class.ElasticSearch(self.host_list)
        els.connect()
        self.assertEqual(len(els.nodes), 1)

    @mock.patch("elastic_class.is_active", mock.Mock(return_value=True))
    @mock.patch("elastic_class.get_cluster_nodes")
    @mock.patch("elastic_class.get_master_name")
    @mock.patch("elastic_class.get_cluster_health")
    @mock.patch("elastic_class.get_info")
    @mock.patch("elastic_class.get_nodes")
    @mock.patch("elastic_class.elasticsearch.Elasticsearch")
    def test_multiple_nodes(self, mock_es, mock_nodes, mock_info, mock_health,
                            mock_master, mock_cluster):

        """Function:  test_multiple_nodes

        Description:  Test with two nodes.

        Arguments:

        """

        mock_es.return_value = self.els
        mock_nodes.return_value = self.nodes_data
        mock_info.return_value = self.info_data
        mock_health.return_value = self.health_data
        mock_master.return_value = self.master_name
        mock_cluster.return_value = self.cluster_data

        els = elastic_class.ElasticSearch(self.host_list)
        els.connect()
        self.assertEqual(len(els.nodes), 2)

    @mock.patch("elastic_class.is_active", mock.Mock(return_value=True))
    @mock.patch("elastic_class.get_cluster_nodes")
    @mock.patch("elastic_class.get_master_name")
    @mock.patch("elastic_class.get_cluster_health")
    @mock.patch("elastic_class.get_info")
    @mock.patch("elastic_class.get_nodes")
    @mock.patch("elastic_class.elasticsearch.Elasticsearch")
    def test_update_status(self, mock_es, mock_nodes, mock_info, mock_health,
                           mock_master, mock_cluster):

        """Function:  test_update_status

        Description:  Test with update_status method.

        Arguments:

        """

        mock_es.return_value = self.els
        mock_nodes.return_value = self.nodes_data
        mock_info.return_value = self.info_data
        mock_health.return_value = self.health_data
        mock_master.return_value = self.master_name
        mock_cluster.return_value = self.cluster_data

        els = elastic_class.ElasticSearch(self.host_list)
        els.connect()
        self.assertEqual(
            (els.port, els.hosts, els.is_connected, els.data, els.logs),
            (9200, self.host_list, True, self.data_results, self.logs_results))


if __name__ == "__main__":
    unittest.main()
