# Classification (U)

"""Program:  informationget_info.py

    Description:  Unit testing of get_info in elastic_class.ElasticSearch
        class.

    Usage:
        test/unit/elastic_class/informationget_info.py

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
        test_default

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        host_list = ["https://hostname:9200"]
        self.els = elastic_class.ElasticSearch(host_list)
        self.els.connect()
        self.results = {"cluster_name": "ClusterName", "name": "ServerName"}

    @mock.patch("elastic_class.elasticsearch.Elasticsearch.info",
                mock.Mock(
                    return_value={
                        "cluster_name": "ClusterName", "name": "ServerName"}))
    def test_default(self):

        """Function:  test_default

        Description:  Test with default settings.

        Arguments:

        """

        self.assertEqual(self.els.get_info(), self.results)


if __name__ == "__main__":
    unittest.main()
