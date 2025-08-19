# Classification (U)

"""Program:  elasticsearch_get_shards.py

    Description:  Unit testing of get_shards in elastic_class.ElasticSearch.

    Usage:
        python test/unit/elastic_class/elasticsearch_get_shards.py

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


class Cat():                                            # pylint:disable=R0903
    """Class:  Cat

    Description:  Class representation of the Elasticsearch.cat class.

    Methods:
        shards

    """

    def shards(self, format="json"):            # pylint:disable=W0622,W0613

        """Method:  shards

        Description:  Method representation of Elasticsearch.cat.shards.

        Arguments:

        """

        return []


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
        self.cat = Cat()


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_get_shards

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.host_list = ["https://hostname:9200"]
        self.els = Elasticsearch(self.host_list)

    @mock.patch("elastic_class.is_active", mock.Mock(return_value=False))
    @mock.patch("elastic_class.ElasticSearch.update_status",
                mock.Mock(return_value=True))
    @mock.patch("elastic_class.elasticsearch.Elasticsearch")
    def test_get_shards(self, mock_es):

        """Function:  test_get_shards

        Description:  Test with successful list of shards.

        Arguments:

        """

        mock_es.return_value = self.els
        els = elastic_class.ElasticSearch(self.host_list)
        els.connect()

        self.assertEqual(els.get_shards(), [])


if __name__ == "__main__":
    unittest.main()
