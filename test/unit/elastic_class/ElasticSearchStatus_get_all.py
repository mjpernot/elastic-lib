#!/usr/bin/python
# Classification (U)

"""Program:  ElasticSearchStatus_get_all.py

    Description:  Unit testing of get_all in elastic_class.ElasticSearchStatus.

    Usage:
        test/unit/elastic_class/ElasticSearchStatus_get_all.py

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

    """

    def __init__(self, host_list, port=9200):

        """Method:  __init__

        Description:  Initialization instance of the class.

        Arguments:

        """

        self.hosts = host_list
        self.port = port


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Initialization for unit testing.
        test_default -> Test with default settings.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.host_list = ["host1", "host2"]
        self.es = Elasticsearch(self.host_list)
        self.results = {"cluster": "clustername"}
        self.results2 = {"cluster": "clustername",
                         "Nodes": ["node1", "node2"]}

    @mock.patch("elastic_class.ElasticSearchStatus.get_cluster",
                mock.Mock(return_value={"cluster": "clustername"})) 
    @mock.patch("elastic_class.ElasticSearchStatus.get_nodes",
                mock.Mock(return_value={"Nodes": ["node1", "node2"]})) 
    @mock.patch("elastic_class.ElasticSearchStatus.get_node_status",
                mock.Mock(return_value={})) 
    @mock.patch("elastic_class.ElasticSearchStatus.get_svr_status",
                mock.Mock(return_value={})) 
    @mock.patch("elastic_class.ElasticSearchStatus.get_mem_status",
                mock.Mock(return_value={})) 
    @mock.patch("elastic_class.ElasticSearchStatus.get_shrd_status",
                mock.Mock(return_value={})) 
    @mock.patch("elastic_class.ElasticSearchStatus.get_gen_status",
                mock.Mock(return_value={})) 
    @mock.patch("elastic_class.ElasticSearchStatus.get_disk_status",
                mock.Mock(return_value={})) 
    @mock.patch("elastic_class.ElasticSearchStatus.update_status2",
                mock.Mock(return_value=True))
    @mock.patch("elastic_class.ElasticSearch.update_status",
                mock.Mock(return_value=True))
    @mock.patch("elastic_class.elasticsearch.Elasticsearch")
    def test_default2(self, mock_es):

        """Function:  test_default2

        Description:  Test with default settings.

        Arguments:

        """

        mock_es.return_value = self.es

        es = elastic_class.ElasticSearchStatus(self.host_list)

        self.assertEqual(es.get_all(), self.results2)

    @mock.patch("elastic_class.ElasticSearchStatus.get_cluster",
                mock.Mock(return_value={"cluster": "clustername"})) 
    @mock.patch("elastic_class.ElasticSearchStatus.get_nodes",
                mock.Mock(return_value={})) 
    @mock.patch("elastic_class.ElasticSearchStatus.get_node_status",
                mock.Mock(return_value={})) 
    @mock.patch("elastic_class.ElasticSearchStatus.get_svr_status",
                mock.Mock(return_value={})) 
    @mock.patch("elastic_class.ElasticSearchStatus.get_mem_status",
                mock.Mock(return_value={})) 
    @mock.patch("elastic_class.ElasticSearchStatus.get_shrd_status",
                mock.Mock(return_value={})) 
    @mock.patch("elastic_class.ElasticSearchStatus.get_gen_status",
                mock.Mock(return_value={})) 
    @mock.patch("elastic_class.ElasticSearchStatus.get_disk_status",
                mock.Mock(return_value={})) 
    @mock.patch("elastic_class.ElasticSearchStatus.update_status2",
                mock.Mock(return_value=True))
    @mock.patch("elastic_class.ElasticSearch.update_status",
                mock.Mock(return_value=True))
    @mock.patch("elastic_class.elasticsearch.Elasticsearch")
    def test_default(self, mock_es):

        """Function:  test_default

        Description:  Test with default settings.

        Arguments:

        """

        mock_es.return_value = self.es

        es = elastic_class.ElasticSearchStatus(self.host_list)

        self.assertEqual(es.get_all(), self.results)


if __name__ == "__main__":
    unittest.main()
