#!/usr/bin/python
# Classification (U)

"""Program:  elasticsearchstatus_chk_shards.py

    Description:  Unit testing of chk_shards in
        elastic_class.ElasticSearchStatus.

    Usage:
        test/unit/elastic_class/elasticsearchstatus_chk_shards.py

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


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_nonop_warn
        test_active_warn
        test_unassigned_warn
        test_no_warn

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        # This is set to allow to show large differences.
        self.maxDiff = None
        self.host_list = ["host1", "host2"]
        self.els = Elasticsearch(self.host_list)
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
                "ListofShards": [["shard2", "d1", "d1", "STOPPED"]]}}}

    @mock.patch("elastic_class.ElasticSearchStatus.update_status2",
                mock.Mock(return_value=True))
    @mock.patch("elastic_class.ElasticSearch.update_status",
                mock.Mock(return_value=True))
    @mock.patch("elastic_class.elasticsearch.Elasticsearch")
    def test_nonop_warn(self, mock_es):

        """Function:  test_nonop_warn

        Description:  Test with non-operation shard warning.

        Arguments:

        """

        mock_es.return_value = self.els

        els = elastic_class.ElasticSearchStatus(self.host_list)
        els.unassigned_shards = self.unassigned_shards
        els.active_shards_percent = self.active_shards_percent
        els.shard_list = self.shard_list2

        self.assertEqual(els.chk_shards(), self.results4)

    @mock.patch("elastic_class.ElasticSearchStatus.update_status2",
                mock.Mock(return_value=True))
    @mock.patch("elastic_class.ElasticSearch.update_status",
                mock.Mock(return_value=True))
    @mock.patch("elastic_class.elasticsearch.Elasticsearch")
    def test_active_warn(self, mock_es):

        """Function:  test_active_warn

        Description:  Test with active shard warning.

        Arguments:

        """

        mock_es.return_value = self.els

        els = elastic_class.ElasticSearchStatus(self.host_list)
        els.unassigned_shards = self.unassigned_shards
        els.active_shards_percent = self.active_shards_percent2
        els.shard_list = self.shard_list

        self.assertEqual(els.chk_shards(), self.results3)

    @mock.patch("elastic_class.ElasticSearchStatus.update_status2",
                mock.Mock(return_value=True))
    @mock.patch("elastic_class.ElasticSearch.update_status",
                mock.Mock(return_value=True))
    @mock.patch("elastic_class.elasticsearch.Elasticsearch")
    def test_unassigned_warn(self, mock_es):

        """Function:  test_unassigned_warn

        Description:  Test with unassigned shard warning.

        Arguments:

        """

        mock_es.return_value = self.els

        els = elastic_class.ElasticSearchStatus(self.host_list)
        els.unassigned_shards = self.unassigned_shards2
        els.active_shards_percent = self.active_shards_percent
        els.shard_list = self.shard_list
        els.num_shards = self.num_shards

        self.assertEqual(els.chk_shards(), self.results2)

    @mock.patch("elastic_class.ElasticSearchStatus.update_status2",
                mock.Mock(return_value=True))
    @mock.patch("elastic_class.ElasticSearch.update_status",
                mock.Mock(return_value=True))
    @mock.patch("elastic_class.elasticsearch.Elasticsearch")
    def test_no_warn(self, mock_es):

        """Function:  test_no_warn

        Description:  Test with no warnings.

        Arguments:

        """

        mock_es.return_value = self.els

        els = elastic_class.ElasticSearchStatus(self.host_list)
        els.unassigned_shards = self.unassigned_shards
        els.active_shards_percent = self.active_shards_percent
        els.shard_list = self.shard_list

        self.assertEqual(els.chk_shards(), self.results)


if __name__ == "__main__":
    unittest.main()
