# Classification (U)

"""Program:  elasticsearchstatus_get_shrd_status.py

    Description:  Unit testing of get_shrd_status in
        elastic_class.ElasticSearchStatus.

    Usage:
        test/unit/elastic_class/elasticsearchstatus_get_shrd_status.py

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

        self.host_list = ["host1", "host2"]
        self.els = Elasticsearch(self.host_list)
        self.active_shards_percent = 80
        self.unassigned_shards = 11
        self.num_shards = 111
        self.num_primary = 75
        self.results = {
            "Shards": {"Percent": self.active_shards_percent,
                       "Unassigned": self.unassigned_shards,
                       "Total": self.num_shards, "Primary": self.num_primary}}

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

        mock_es.return_value = self.els

        els = elastic_class.ElasticSearchStatus(self.host_list)
        els.active_shards_percent = self.active_shards_percent
        els.unassigned_shards = self.unassigned_shards
        els.num_shards = self.num_shards
        els.num_primary = self.num_primary

        self.assertEqual(els.get_shrd_status(), self.results)


if __name__ == "__main__":
    unittest.main()
