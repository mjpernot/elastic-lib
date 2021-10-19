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
        test_connect

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.host_list = ["host1", "host2"]
        self.els = Elasticsearch(self.host_list)

    @mock.patch("elastic_class.ElasticSearch.update_status")
    @mock.patch("elastic_class.elasticsearch.Elasticsearch")
    def test_connect(self, mock_es, mock_status):

        """Function:  test_connect

        Description:  Test with connection to Elasticsearch.

        Arguments:

        """

        mock_es.return_value = self.els
        mock_status.return_value = True

        els = elastic_class.ElasticSearch(self.host_list)
        els.connect()
        self.assertEqual(
            (els.port, els.hosts, els.is_connected, els.data, els.logs),
            (9200, self.host_list, False, {}, {}))


if __name__ == "__main__":
    unittest.main()
