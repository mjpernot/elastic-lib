#!/usr/bin/python
# Classification (U)

"""Program:  ElasticSearchStatus_chk_shards.py

    Description:  Unit testing of chk_shards in
        elastic_class.ElasticSearchStatus.

    Usage:
        test/unit/elastic_class/ElasticSearchStatus_chk_shards.py

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
        test_nonop_warn -> Test with non-operation shard warning.
        test_active_warn -> Test with active shard warning.
        test_unassigned_warn -> Test with unassigned shard warning.
        test_no_warn -> Test with no warnings.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.host_list = ["host1", "host2"]
        self.es = Elasticsearch(self.host_list)
        self.unassigned_shards = 0
        self.unassigned_shards2 = 1
        self.active_shards_percent = 100
        self.active_shards_percent2 = 90
        self.shard_list = [["shard1", "d1", "d1", "STARTED"],
                           ["shard2", "d1", "d1", "STARTED"]]
        self.shard_list2 = [["shard1", "d1", "d1", "STARTED"],
                            ["shard2", "d1", "d1", "STOPPED"]]
        self.num_shards = 10
        self.results = {}
        self.results2 = {
            "ShardWarning": {"UnassignedShards": {
                "Reason": "Detected unassigned shards",
                "Unassigned": self.unassigned_shards2,
                "Total": self.num_shards}}}
        self.results3 = {
            "ShardWarning": {"ActiveShardsPercent": {
                "Reason": "Detected less than 100% active shards",
                "Percentage": self.active_shards_percent2}}}
        self.results4 = {
            "ShardWarning": {"NonOperationShards": {
                "Reason": "Detected shards not in operational mode",
                "ListofShards": ["shard2", "d1", "d1", "STOPPED"]}}}

    @mock.patch("elastic_class.ElasticSearchStatus.update_status",
                mock.Mock(return_value=True))
    @mock.patch("elastic_class.ElasticSearch.update_status",
                mock.Mock(return_value=True))
    @mock.patch("elastic_class.elasticsearch.Elasticsearch")
    def test_nonop_warn(self, mock_es):

        """Function:  test_nonop_warn

        Description:  Test with non-operation shard warning.

        Arguments:

        """

        mock_es.return_value = self.es

        es = unassigned_shards = self.unassigned_shards
        es.active_shards_percent = self.active_shards_percent
        es.shard_list = self.shard_lis2

        self.assertEqual(es.chk_shards(), self.results4)

    @mock.patch("elastic_class.ElasticSearchStatus.update_status",
                mock.Mock(return_value=True))
    @mock.patch("elastic_class.ElasticSearch.update_status",
                mock.Mock(return_value=True))
    @mock.patch("elastic_class.elasticsearch.Elasticsearch")
    def test_active_warn(self, mock_es):

        """Function:  test_active_warn

        Description:  Test with active shard warning.

        Arguments:

        """

        mock_es.return_value = self.es

        es = unassigned_shards = self.unassigned_shards
        es.active_shards_percent = self.active_shards_percent2
        es.shard_list = self.shard_list

        self.assertEqual(es.chk_shards(), self.results3)

    @mock.patch("elastic_class.ElasticSearchStatus.update_status",
                mock.Mock(return_value=True))
    @mock.patch("elastic_class.ElasticSearch.update_status",
                mock.Mock(return_value=True))
    @mock.patch("elastic_class.elasticsearch.Elasticsearch")
    def test_unassigned_warn(self, mock_es):

        """Function:  test_unassigned_warn

        Description:  Test with unassigned shard warning.

        Arguments:

        """

        mock_es.return_value = self.es

        es = unassigned_shards = self.unassigned_shards2
        es.active_shards_percent = self.active_shards_percent
        es.shard_list = self.shard_list

        self.assertEqual(es.chk_shards(), self.results2)

    @mock.patch("elastic_class.ElasticSearchStatus.update_status",
                mock.Mock(return_value=True))
    @mock.patch("elastic_class.ElasticSearch.update_status",
                mock.Mock(return_value=True))
    @mock.patch("elastic_class.elasticsearch.Elasticsearch")
    def test_no_warn(self, mock_es):

        """Function:  test_no_warn

        Description:  Test with no warnings.

        Arguments:

        """

        mock_es.return_value = self.es

        es = elastic_class.ElasticSearchStatus(self.host_list)
        es.unassigned_shards = self.unassigned_shards
        es.active_shards_percent = self.active_shards_percent
        es.shard_list = self.shard_list

        self.assertEqual(es.chk_shards(), self.results)


if __name__ == "__main__":
    unittest.main()
