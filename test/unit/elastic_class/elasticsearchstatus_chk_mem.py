#!/usr/bin/python
# Classification (U)

"""Program:  elasticsearchstatus_chk_mem.py

    Description:  Unit testing of chk_mem in
        elastic_class.ElasticSearchStatus.

    Usage:
        test/unit/elastic_class/elasticsearchstatus_chk_mem.py

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
        test_new_arg_warn -> Test with new cutoff and with warning.
        test_new_arg_no_warn -> Test with new cutoff and with no warning.
        test_default_warn -> Test with default settings and with warning.
        test_default_no_warn -> Test with default settings and no warning.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.host_list = ["host1", "host2"]
        self.els = Elasticsearch(self.host_list)
        self.mem_per_used = 80
        self.mem_per_used2 = 95
        self.mem_total = 234567890
        self.mem_used = 210000000
        self.results = {}
        self.results2 = {
            "MemoryWarning": {"Reason": "Have reach memory threshold",
                              "ThresholdPercent": 90,
                              "TotalMemory": "223.70MB",
                              "MemoryPercentUsage": self.mem_per_used2,
                              "MemoryUsed": "200.27MB"}}
        self.results3 = {
            "MemoryWarning": {"Reason": "Have reach memory threshold",
                              "ThresholdPercent": 85,
                              "TotalMemory": "223.70MB",
                              "MemoryPercentUsage": self.mem_per_used2,
                              "MemoryUsed": "200.27MB"}}

    @mock.patch("elastic_class.ElasticSearchStatus.update_status2",
                mock.Mock(return_value=True))
    @mock.patch("elastic_class.ElasticSearch.update_status",
                mock.Mock(return_value=True))
    @mock.patch("elastic_class.elasticsearch.Elasticsearch")
    def test_new_arg_warn(self, mock_es):

        """Function:  test_new_arg_warn

        Description:  Test with new cutoff and with warning.

        Arguments:

        """

        mock_es.return_value = self.els

        els = elastic_class.ElasticSearchStatus(self.host_list)
        els.mem_per_used = self.mem_per_used2
        els.mem_total = self.mem_total
        els.mem_used = self.mem_used

        self.assertEqual(els.chk_mem(cutoff_mem=85), self.results3)

    @mock.patch("elastic_class.ElasticSearchStatus.update_status2",
                mock.Mock(return_value=True))
    @mock.patch("elastic_class.ElasticSearch.update_status",
                mock.Mock(return_value=True))
    @mock.patch("elastic_class.elasticsearch.Elasticsearch")
    def test_new_arg_no_warn(self, mock_es):

        """Function:  test_new_arg_no_warn

        Description:  Test with new cutoff and with no warning.

        Arguments:

        """

        mock_es.return_value = self.els

        els = elastic_class.ElasticSearchStatus(self.host_list)
        els.mem_per_used = self.mem_per_used
        els.mem_total = self.mem_total

        self.assertEqual(els.chk_mem(cutoff_mem=85), self.results)

    @mock.patch("elastic_class.ElasticSearchStatus.update_status2",
                mock.Mock(return_value=True))
    @mock.patch("elastic_class.ElasticSearch.update_status",
                mock.Mock(return_value=True))
    @mock.patch("elastic_class.elasticsearch.Elasticsearch")
    def test_default_warn(self, mock_es):

        """Function:  test_default_warn

        Description:  Test with default settings and with warning.

        Arguments:

        """

        mock_es.return_value = self.els

        els = elastic_class.ElasticSearchStatus(self.host_list)
        els.mem_per_used = self.mem_per_used2
        els.mem_total = self.mem_total
        els.mem_used = self.mem_used

        self.assertEqual(els.chk_mem(), self.results2)

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
        els.mem_per_used = self.mem_per_used
        els.mem_total = self.mem_total

        self.assertEqual(els.chk_mem(), self.results)


if __name__ == "__main__":
    unittest.main()
