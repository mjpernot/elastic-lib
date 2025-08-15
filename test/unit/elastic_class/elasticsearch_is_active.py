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
import unittest
import mock

# Local
sys.path.append(os.getcwd())
import elastic_class                            # pylint:disable=E0401,C0413
import version                                  # pylint:disable=E0401,C0413

__version__ = version.__version__


class Elasticsearch():                                  # pylint:disable=R0903

    """Class:  ElasticSearch

    Description:  Class representation of the Elasticsearch class.

    Methods:
        __init__
        ping

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

    def ping(self):

        """Method:  ping

        Description:  Stub holder for Elasticsearch.ping method.

        Arguments:

        """

        return True


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_ping

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.host_list = ["http://hostname:9200"]
        self.els = elastic_class.Elasticsearch(self.host_list)
        self.connect()
#        self.els = Elasticsearch(self.host_list)

#    @mock.patch("elastic_class.is_active", mock.Mock(return_value=True))
#    @mock.patch("elastic_class.ElasticSearch.update_status",
#                mock.Mock(return_value=True))
#    @mock.patch("elastic_class.elasticsearch.Elasticsearch")
#    def test_ping(self, mock_es):

    @mock.patch("elastic_class.elasticsearch.Elasticsearch.ping",
                mock.Mock(return_value=True))
    def test_ping(self):

        """Function:  test_ping

        Description:  Test with successful ping to Elasticsearch.

        Arguments:

        """

#        els = elastic_class.ElasticSearch(self.host_list)
#        els.is_active()

        self.assertTrue(els.is_active())

#        mock_es.return_value = self.els

#        els = elastic_class.ElasticSearch(self.host_list)
#        els.connect()
#        self.assertTrue(els.is_connected)


if __name__ == "__main__":
    unittest.main()
