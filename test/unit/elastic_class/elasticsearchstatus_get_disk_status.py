#!/usr/bin/python
# Classification (U)

"""Program:  elasticsearchstatus_get_disk_status.py

    Description:  Unit testing of get_disk_status in
        elastic_class.ElasticSearchStatus.

    Usage:
        test/unit/elastic_class/elasticsearchstatus_get_disk_status.py

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
        test_default

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
        self.results = {
            "DiskUsage": {
                "nodename": {
                    "Total": "100gb", "Available": "75gb", "TotalUsed": "20gb",
                    "ESUsed": "15gb", "Percent": "21"},
                "nodename2": {
                    "Total": "110gb", "Available": "65gb", "TotalUsed": "30gb",
                    "ESUsed": "20gb", "Percent": "31"}}}
        self.els = elastic_class.ElasticSearchStatus(self.host_list)
        self.els.disk_list = self.disk_list

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

        self.assertEqual(self.els.get_disk_status(), self.results)


if __name__ == "__main__":
    unittest.main()
