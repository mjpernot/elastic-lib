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
        test_unassigned_warn
        test_unassigned_no_warn
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
        self.els = Elasticsearch(self.host_list)
        self.disk_list = [
            ["995", "69mb", "16gb", "53gb", "69gb", "23", "ip1", "ip2",
             "hostname1"],
            ["990", "68mb", "15gb", "53gb", "68gb", "22", "ip3", "ip4",
             "hostname2"]]
        self.disk_list2 = [
            ["995", "69mb", "16gb", "53gb", "69gb", "23", "ip1", "ip2",
             "hostname1"],
            ["990", "68mb", "15gb", "53gb", "68gb", "90", "ip3", "ip4",
             "hostname2"]]
        self.disk_list3 = [
            ["995", "69mb", "16gb", "53gb", "69gb", "23", "ip1", "ip2",
             "hostname1"],
            ["2", "UNASSIGNED"],
            ["990", "68mb", "15gb", "53gb", "68gb", "22", "ip3", "ip4",
             "hostname2"]]
        self.disk_list4 = [
            ["995", "69mb", "16gb", "53gb", "69gb", "23", "ip1", "ip2",
             "hostname1"],
            ["2", "UNASSIGNED"],
            ["990", "68mb", "15gb", "53gb", "68gb", "90", "ip3", "ip4",
             "hostname2"]]
        self.results = {}
        self.results2 = {
            "DiskWarning": {"hostname2": {
                "Reason": "Have reached disk usage threshold",
                "ThresholdPercent": 85,
                "UsedPercent": "90",
                "TotalDisk": "68gb",
                "TotalUsed": "15gb",
                "Available": "53gb",
                "ElasticSearchUsed": "68mb"}}}
        self.results3 = {
            "DiskWarning": {"hostname2": {
                "Reason": "Have reached disk usage threshold",
                "ThresholdPercent": 87,
                "UsedPercent": "90",
                "TotalDisk": "68gb",
                "TotalUsed": "15gb",
                "Available": "53gb",
                "ElasticSearchUsed": "68mb"}}}

    @mock.patch("elastic_class.ElasticSearchStatus.update_status2",
                mock.Mock(return_value=True))
    @mock.patch("elastic_class.ElasticSearch.update_status",
                mock.Mock(return_value=True))
    @mock.patch("elastic_class.elasticsearch.Elasticsearch")
    def test_unassigned_warn(self, mock_es):

        """Function:  test_unassigned_warn

        Description:  Test with unassigned disk and warning.

        Arguments:

        """

        mock_es.return_value = self.els

        els = elastic_class.ElasticSearchStatus(self.host_list)
        els.disk_list = self.disk_list4

        self.assertEqual(els.chk_disk(), self.results2)

    @mock.patch("elastic_class.ElasticSearchStatus.update_status2",
                mock.Mock(return_value=True))
    @mock.patch("elastic_class.ElasticSearch.update_status",
                mock.Mock(return_value=True))
    @mock.patch("elastic_class.elasticsearch.Elasticsearch")
    def test_unassigned_no_warn(self, mock_es):

        """Function:  test_unassigned_no_warn

        Description:  Test with unassigned disk and no warning.

        Arguments:

        """

        mock_es.return_value = self.els

        els = elastic_class.ElasticSearchStatus(self.host_list)
        els.disk_list = self.disk_list3

        self.assertEqual(els.chk_disk(), self.results)

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

        els = elastic_class.ElasticSearchStatus(self.host_list)
        els.disk_list = self.disk_list2

        self.assertEqual(els.chk_disk(cutoff_disk=87), self.results3)

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

        els = elastic_class.ElasticSearchStatus(self.host_list)
        els.disk_list = self.disk_list2

        self.assertEqual(els.chk_disk(cutoff_disk=95), self.results)

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

        els = elastic_class.ElasticSearchStatus(self.host_list)
        els.disk_list = self.disk_list2

        self.assertEqual(els.chk_disk(), self.results2)

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

        els = elastic_class.ElasticSearchStatus(self.host_list)
        els.disk_list = self.disk_list

        self.assertEqual(els.chk_disk(), self.results)


if __name__ == "__main__":
    unittest.main()
