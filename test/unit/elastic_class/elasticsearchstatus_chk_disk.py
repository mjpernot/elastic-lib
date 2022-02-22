#!/usr/bin/python
# Classification (U)

"""Program:  elasticsearchstatus_chk_disk.py

    Description:  Unit testing of chk_disk in
        elastic_class.ElasticSearchStatus.

    Usage:
        test/unit/elastic_class/elasticsearchstatus_chk_disk.py

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
        test_new_arg_warn
        test_new_arg_no_warn
        test_default_warn
        test_default_no_warn

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.host_list = ["host1", "host2"]
        self.disk_list = [
            {"node": "nodename", "disk.total": "100gb", "shards": "101",
             "disk.avail": "75gb", "disk.used": "20gb", "host": "servername",
             "disk.percent": "21", "ip": "ip.addr", "disk.indices": "15gb"},
            {"node": "nodename2", "disk.total": "110gb", "shards": "101",
             "disk.avail": "65gb", "disk.used": "30gb", "host": "servername2",
             "disk.percent": "31", "ip": "ip.addr2", "disk.indices": "20gb"}]
        self.disk_list2 = [
            {"node": "nodename", "disk.total": "100gb", "shards": "101",
             "disk.avail": "75gb", "disk.used": "20gb", "host": "servername",
             "disk.percent": "21", "ip": "ip.addr", "disk.indices": "15gb"},
            {"node": "nodename2", "disk.total": "110gb", "shards": "101",
             "disk.avail": "65gb", "disk.used": "30gb", "host": "servername2",
             "disk.percent": "90", "ip": "ip.addr2", "disk.indices": "20gb"}]
        self.results = {}
        self.results2 = {
            "DiskWarning": {"nodename2": {
                "Reason": "Have reached disk usage threshold",
                "ThresholdPercent": 85,
                "UsedPercent": "90",
                "TotalDisk": "110gb",
                "TotalUsed": "30gb",
                "Available": "65gb",
                "ElasticSearchUsed": "20gb"}}}
        self.results3 = {
            "DiskWarning": {"nodename2": {
                "Reason": "Have reached disk usage threshold",
                "ThresholdPercent": 87,
                "UsedPercent": "90",
                "TotalDisk": "110gb",
                "TotalUsed": "30gb",
                "Available": "65gb",
                "ElasticSearchUsed": "20gb"}}}
        self.els = elastic_class.ElasticSearchStatus(self.host_list)

    @mock.patch("elastic_class.ElasticSearchStatus.update_status2",
                mock.Mock(return_value=True))
    @mock.patch("elastic_class.ElasticSearch.update_status",
                mock.Mock(return_value=True))
    @mock.patch("elastic_class.elasticsearch.Elasticsearch")
    def test_new_arg_warn(self, mock_es):

        """Function:  test_new_arg_warn

        Description:  Test with new cutoff with warning.

        Arguments:

        """

        mock_es.return_value = self.els

        self.els.disk_list = self.disk_list2

        self.assertEqual(self.els.chk_disk(cutoff_disk=87), self.results3)

    @mock.patch("elastic_class.ElasticSearchStatus.update_status2",
                mock.Mock(return_value=True))
    @mock.patch("elastic_class.ElasticSearch.update_status",
                mock.Mock(return_value=True))
    @mock.patch("elastic_class.elasticsearch.Elasticsearch")
    def test_new_arg_no_warn(self, mock_es):

        """Function:  test_new_arg_no_warn

        Description:  Test with new cutoff and no warning.

        Arguments:

        """

        mock_es.return_value = self.els

        self.els.disk_list = self.disk_list2

        self.assertEqual(self.els.chk_disk(cutoff_disk=95), self.results)

    @mock.patch("elastic_class.ElasticSearchStatus.update_status2",
                mock.Mock(return_value=True))
    @mock.patch("elastic_class.ElasticSearch.update_status",
                mock.Mock(return_value=True))
    @mock.patch("elastic_class.elasticsearch.Elasticsearch")
    def test_default_warn(self, mock_es):

        """Function:  test_default_warn

        Description:  Test with default settings with warning.

        Arguments:

        """

        mock_es.return_value = self.els

        self.els.disk_list = self.disk_list2

        self.assertEqual(self.els.chk_disk(), self.results2)

    @mock.patch("elastic_class.ElasticSearchStatus.update_status2",
                mock.Mock(return_value=True))
    @mock.patch("elastic_class.ElasticSearch.update_status",
                mock.Mock(return_value=True))
    @mock.patch("elastic_class.elasticsearch.Elasticsearch")
    def test_default_no_warn(self, mock_es):

        """Function:  test_default_no_warn

        Description:  Test with default settings and no warning.

        Arguments:

        """

        mock_es.return_value = self.els

        self.els.disk_list = self.disk_list

        self.assertEqual(self.els.chk_disk(), self.results)


if __name__ == "__main__":
    unittest.main()
