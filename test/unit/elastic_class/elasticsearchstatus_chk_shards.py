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

        self.host_list = ["host1", "host2"]
        self.els = elastic_class.ElasticSearchStatus(self.host_list)
        self.unassigned_shards = 0
        self.unassigned_shards2 = 1
        self.active_shards_percent = 100
        self.active_shards_percent2 = 90
        self.shard_list = [
            {"node": "nodename", "index": "indexname", "docs": "10",
             "shard": "0", "state": "STARTED", "prirep": "p", "ip": "ip_addr",
             "store": "5mb"},
            {"node": "nodename2", "index": "indexname2", "docs": "20",
             "shard": "0", "state": "STARTED", "prirep": "p", "ip": "ip_addr2",
             "store": "15mb"}]
        self.shard_list2 = [
            {"node": "nodename", "index": "indexname", "docs": "10",
             "shard": "0", "state": "STARTED", "prirep": "p", "ip": "ip_addr",
             "store": "5mb"},
            {"node": "nodename2", "index": "indexname2", "docs": "20",
             "shard": "0", "state": "UNASSIGNED", "prirep": "p",
             "ip": "ip_addr2", "store": "15mb"}]
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
                "ListofShards": [
                    {"node": "nodename2", "index": "indexname2", "docs": "20",
                     "shard": "0", "state": "UNASSIGNED", "prirep": "p",
                     "ip": "ip_addr2", "store": "15mb"}]}}}

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

        self.els.unassigned_shards = self.unassigned_shards
        self.els.active_shards_percent = self.active_shards_percent
        self.els.shard_list = self.shard_list2

        self.assertEqual(self.els.chk_shards(), self.results4)

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

        self.els.unassigned_shards = self.unassigned_shards
        self.els.active_shards_percent = self.active_shards_percent2
        self.els.shard_list = self.shard_list

        self.assertEqual(self.els.chk_shards(), self.results3)

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

        self.els.unassigned_shards = self.unassigned_shards2
        self.els.active_shards_percent = self.active_shards_percent
        self.els.shard_list = self.shard_list
        self.els.num_shards = self.num_shards

        self.assertEqual(self.els.chk_shards(), self.results2)

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

        self.els.unassigned_shards = self.unassigned_shards
        self.els.active_shards_percent = self.active_shards_percent
        self.els.shard_list = self.shard_list

        self.assertEqual(self.els.chk_shards(), self.results)


if __name__ == "__main__":
    unittest.main()
