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
        self.els = elastic_class.ElasticSearch(self.host_list)
        self.els.connect()

    @mock.patch("elastic_class.elasticsearch.Elasticsearch.ping",
                mock.Mock(return_value=True))
    def test_ping(self):

        """Function:  test_ping

        Description:  Test with successful ping to Elasticsearch.

        Arguments:

        """

        self.assertTrue(self.els.is_active())


if __name__ == "__main__":
    unittest.main()
