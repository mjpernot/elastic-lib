#!/usr/bin/python
# Classification (U)

"""Program:  elasticsearch_connect.py

    Description:  Unit testing of connect in elastic_class.ElasticSearch.

    Usage:
        test/unit/elastic_class/elasticsearch_connect.py

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


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_connect_false
        test_connect_true

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.host_list = ["host1", "host2"]
        self.els = Elasticsearch(self.host_list)

    @mock.patch("elastic_class.is_active")
    @mock.patch("elastic_class.ElasticSearch.update_status")
    @mock.patch("elastic_class.elasticsearch.Elasticsearch")
    def test_connect_false(self, mock_es, mock_status, mock_active):

        """Function:  test_connect_false

        Description:  Test with failed connection to Elasticsearch.

        Arguments:

        """

        mock_es.return_value = self.els
        mock_status.return_value = True
        mock_active.return_value = False

        els = elastic_class.ElasticSearch(self.host_list)
        els.connect()
        self.assertFalse(els.is_connected)

    @mock.patch("elastic_class.is_active")
    @mock.patch("elastic_class.ElasticSearch.update_status")
    @mock.patch("elastic_class.elasticsearch.Elasticsearch")
    def test_connect_true(self, mock_es, mock_status, mock_active):

        """Function:  test_connect_true

        Description:  Test with successful connection to Elasticsearch.

        Arguments:

        """

        mock_es.return_value = self.els
        mock_status.return_value = True
        mock_active.return_value = True

        els = elastic_class.ElasticSearch(self.host_list)
        els.connect()
        self.assertTrue(els.is_connected)


if __name__ == "__main__":
    unittest.main()
