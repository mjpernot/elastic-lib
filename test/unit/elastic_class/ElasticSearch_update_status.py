#!/usr/bin/python
# Classification (U)

"""Program:  ElasticSearch_update_status.py

    Description:  Unit testing of update_status in elastic_class.ElasticSearch.

    Usage:
        test/unit/elastic_class/ElasticSearch_update_status.py

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
        self.info_status = {"cluster_name": "ClusterName", "name": "servername"}

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
        test_ping_false -> Test ping of Elasticsearch server is False.
        test_ping_true -> Test ping of Elasticsearch server is True.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.host_list = ["host1", "host2"]
        self.es = Elasticsearch(self.host_list)
        self.nodes_data = {"serverid1": {"name": "hostname1", "settings":
            {"path": {"data": ["/dir/data1"], "logs": ["/dir/logs1"]}}},
            "serverid2": {"name": "hostname2", "settings":
            {"path": {"data": ["/dir/data2"], "logs": ["/dir/logs2"]}}}}
        self.data_results = {"hostname1": ["/dir/data1"],
            "hostname2": ["/dir/data2"]}
        self.logs_results = {"hostname1": ["/dir/logs1"],
            "hostname2": ["/dir/logs2"]}

    @mock.patch("elastic_class.elasticsearch.Elasticsearch")
    def test_ping_false(self, mock_es):

        """Function:  test_ping_false

        Description:  Test ping of Elasticsearch server is False.

        Arguments:

        """

        self.es.ping_status = False
        mock_es.return_value = self.es

        es = elastic_class.ElasticSearch(self.host_list)
        es.update_status()
        self.assertEqual((es.port, es.hosts, es.is_connected, es.data,
                          es.logs),
                         (9200, self.host_list, False, {}, {}))

    @mock.patch("elastic_class.get_nodes")
    @mock.patch("elastic_class.elasticsearch.Elasticsearch")
    def test_ping_true(self, mock_es, mock_nodes):

        """Function:  test_ping_true

        Description:  Test ping of Elasticsearch server is True.

        Arguments:

        """

        mock_es.return_value = self.es
        mock_nodes.return_value = self.nodes_data

        es = elastic_class.ElasticSearch(self.host_list)
        es.update_status()
        self.assertEqual((es.port, es.hosts, es.is_connected, es.data,
                          es.logs),
                         (9200, self.host_list, True, self.data_results,
                         self.logs_results))


if __name__ == "__main__":
    unittest.main()
