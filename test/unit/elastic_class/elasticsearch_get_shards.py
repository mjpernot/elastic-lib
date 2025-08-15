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

        host_list = ["http://hostname:9200"]
        self.els = elastic_class.ElasticSearch(host_list)
        self.els.connect()

    @mock.patch("elastic_class.elasticsearch.Elasticsearch.cat.shards",
                mock.Mock(return_value=[]))
    def test_get_shards(self):

        """Function:  test_get_shards

        Description:  Test with successful list of shards.

        Arguments:

        """

        self.assertEqual(self.els.get_shards(), [])


if __name__ == "__main__":
    unittest.main()
