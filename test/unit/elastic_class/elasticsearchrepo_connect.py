# Classification (U)

"""Program:  elasticsearchrepo_connect.py

    Description:  Unit testing of connect in elastic_class.elasticsearchrepo.

    Usage:
        test/unit/elastic_class/elasticsearchrepo_connect.py

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

    @mock.patch("elastic_class.is_active", mock.Mock(return_value=False))
    @mock.patch("elastic_class.ElasticSearch.update_status",
                mock.Mock(return_value=True))
    @mock.patch("elastic_class.elasticsearch.Elasticsearch")
    def test_connect_false(self, mock_es):

        """Function:  test_connect_false

        Description:  Test with failed connection to Elasticsearch.

        Arguments:

        """

        mock_es.return_value = self.els

        els = elastic_class.ElasticSearchRepo(self.host_list)
        els.connect()
        self.assertFalse(els.is_connected)

    @mock.patch("elastic_class.ElasticSearchRepo.update_repo_status",
                mock.Mock(return_value=True))
    @mock.patch("elastic_class.is_active", mock.Mock(return_value=True))
    @mock.patch("elastic_class.ElasticSearch.update_status",
                mock.Mock(return_value=True))
    @mock.patch("elastic_class.elasticsearch.Elasticsearch")
    def test_connect_true(self, mock_es):

        """Function:  test_connect_true

        Description:  Test with successful connection to Elasticsearch.

        Arguments:

        """

        mock_es.return_value = self.els

        els = elastic_class.ElasticSearchRepo(self.host_list)
        els.connect()
        self.assertTrue(els.is_connected)


if __name__ == "__main__":
    unittest.main()
