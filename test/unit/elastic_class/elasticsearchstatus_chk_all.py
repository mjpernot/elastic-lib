# Classification (U)

"""Program:  elasticsearchstatus_chk_all.py

    Description:  Unit testing of chk_all in elastic_class.ElasticSearchStatus.

    Usage:
        test/unit/elastic_class/elasticsearchstatus_chk_all.py

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
        self.cutoff_cpu = 75
        self.cutoff_mem = 90
        self.cutoff_disk = 85


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_cutoff_disk_default
        test_cutoff_disk_value
        test_cutoff_mem_default
        test_cutoff_mem_value
        test_cutoff_cpu_default
        test_cutoff_cpu_value
        test_one_warn
        test_default_no_warn

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.host_list = ["host1", "host2"]
        self.els = Elasticsearch(self.host_list)
        self.results = {}
        self.results2 = {
            "ClusterWarning": {
                "ClusterStatus": {
                    "Reason": "Detected the cluster is not green",
                    "Status": "yellow"}}}

    @mock.patch("elastic_class.ElasticSearchStatus.get_cluster",
                mock.Mock(return_value={}))
    @mock.patch("elastic_class.ElasticSearchStatus.chk_disk",
                mock.Mock(return_value={}))
    @mock.patch("elastic_class.ElasticSearchStatus.chk_status",
                mock.Mock(return_value={}))
    @mock.patch("elastic_class.ElasticSearchStatus.chk_server",
                mock.Mock(return_value={}))
    @mock.patch("elastic_class.ElasticSearchStatus.chk_shards",
                mock.Mock(return_value={}))
    @mock.patch("elastic_class.ElasticSearchStatus.chk_nodes",
                mock.Mock(return_value={}))
    @mock.patch("elastic_class.ElasticSearchStatus.chk_mem",
                mock.Mock(return_value={}))
    @mock.patch("elastic_class.ElasticSearchStatus.update_status2",
                mock.Mock(return_value=True))
    @mock.patch("elastic_class.ElasticSearch.update_status",
                mock.Mock(return_value=True))
    @mock.patch("elastic_class.elasticsearch.Elasticsearch")
    def test_cutoff_disk_default(self, mock_es):

        """Function:  test_cutoff_disk_default

        Description:  Test with default cutoff_disk value.

        Arguments:

        """

        mock_es.return_value = self.els

        els = elastic_class.ElasticSearchStatus(self.host_list)

        self.assertEqual(els.chk_all(cutoff_disk=None), self.results)

    @mock.patch("elastic_class.ElasticSearchStatus.get_cluster",
                mock.Mock(return_value={}))
    @mock.patch("elastic_class.ElasticSearchStatus.chk_disk",
                mock.Mock(return_value={}))
    @mock.patch("elastic_class.ElasticSearchStatus.chk_status",
                mock.Mock(return_value={}))
    @mock.patch("elastic_class.ElasticSearchStatus.chk_server",
                mock.Mock(return_value={}))
    @mock.patch("elastic_class.ElasticSearchStatus.chk_shards",
                mock.Mock(return_value={}))
    @mock.patch("elastic_class.ElasticSearchStatus.chk_nodes",
                mock.Mock(return_value={}))
    @mock.patch("elastic_class.ElasticSearchStatus.chk_mem",
                mock.Mock(return_value={}))
    @mock.patch("elastic_class.ElasticSearchStatus.update_status2",
                mock.Mock(return_value=True))
    @mock.patch("elastic_class.ElasticSearch.update_status",
                mock.Mock(return_value=True))
    @mock.patch("elastic_class.elasticsearch.Elasticsearch")
    def test_cutoff_disk_value(self, mock_es):

        """Function:  test_cutoff_disk_value

        Description:  Test with cutoff_disk value passed.

        Arguments:

        """

        mock_es.return_value = self.els

        els = elastic_class.ElasticSearchStatus(self.host_list)

        self.assertEqual(els.chk_all(cutoff_disk=50), self.results)

    @mock.patch("elastic_class.ElasticSearchStatus.get_cluster",
                mock.Mock(return_value={}))
    @mock.patch("elastic_class.ElasticSearchStatus.chk_disk",
                mock.Mock(return_value={}))
    @mock.patch("elastic_class.ElasticSearchStatus.chk_status",
                mock.Mock(return_value={}))
    @mock.patch("elastic_class.ElasticSearchStatus.chk_server",
                mock.Mock(return_value={}))
    @mock.patch("elastic_class.ElasticSearchStatus.chk_shards",
                mock.Mock(return_value={}))
    @mock.patch("elastic_class.ElasticSearchStatus.chk_nodes",
                mock.Mock(return_value={}))
    @mock.patch("elastic_class.ElasticSearchStatus.chk_mem",
                mock.Mock(return_value={}))
    @mock.patch("elastic_class.ElasticSearchStatus.update_status2",
                mock.Mock(return_value=True))
    @mock.patch("elastic_class.ElasticSearch.update_status",
                mock.Mock(return_value=True))
    @mock.patch("elastic_class.elasticsearch.Elasticsearch")
    def test_cutoff_mem_default(self, mock_es):

        """Function:  test_cutoff_mem_default

        Description:  Test with default cutoff_mem value.

        Arguments:

        """

        mock_es.return_value = self.els

        els = elastic_class.ElasticSearchStatus(self.host_list)

        self.assertEqual(els.chk_all(cutoff_mem=None), self.results)

    @mock.patch("elastic_class.ElasticSearchStatus.get_cluster",
                mock.Mock(return_value={}))
    @mock.patch("elastic_class.ElasticSearchStatus.chk_disk",
                mock.Mock(return_value={}))
    @mock.patch("elastic_class.ElasticSearchStatus.chk_status",
                mock.Mock(return_value={}))
    @mock.patch("elastic_class.ElasticSearchStatus.chk_server",
                mock.Mock(return_value={}))
    @mock.patch("elastic_class.ElasticSearchStatus.chk_shards",
                mock.Mock(return_value={}))
    @mock.patch("elastic_class.ElasticSearchStatus.chk_nodes",
                mock.Mock(return_value={}))
    @mock.patch("elastic_class.ElasticSearchStatus.chk_mem",
                mock.Mock(return_value={}))
    @mock.patch("elastic_class.ElasticSearchStatus.update_status2",
                mock.Mock(return_value=True))
    @mock.patch("elastic_class.ElasticSearch.update_status",
                mock.Mock(return_value=True))
    @mock.patch("elastic_class.elasticsearch.Elasticsearch")
    def test_cutoff_mem_value(self, mock_es):

        """Function:  test_cutoff_mem_value

        Description:  Test with cutoff_mem value passed.

        Arguments:

        """

        mock_es.return_value = self.els

        els = elastic_class.ElasticSearchStatus(self.host_list)

        self.assertEqual(els.chk_all(cutoff_mem=50), self.results)

    @mock.patch("elastic_class.ElasticSearchStatus.get_cluster",
                mock.Mock(return_value={}))
    @mock.patch("elastic_class.ElasticSearchStatus.chk_disk",
                mock.Mock(return_value={}))
    @mock.patch("elastic_class.ElasticSearchStatus.chk_status",
                mock.Mock(return_value={}))
    @mock.patch("elastic_class.ElasticSearchStatus.chk_server",
                mock.Mock(return_value={}))
    @mock.patch("elastic_class.ElasticSearchStatus.chk_shards",
                mock.Mock(return_value={}))
    @mock.patch("elastic_class.ElasticSearchStatus.chk_nodes",
                mock.Mock(return_value={}))
    @mock.patch("elastic_class.ElasticSearchStatus.chk_mem",
                mock.Mock(return_value={}))
    @mock.patch("elastic_class.ElasticSearchStatus.update_status2",
                mock.Mock(return_value=True))
    @mock.patch("elastic_class.ElasticSearch.update_status",
                mock.Mock(return_value=True))
    @mock.patch("elastic_class.elasticsearch.Elasticsearch")
    def test_cutoff_cpu_default(self, mock_es):

        """Function:  test_cutoff_cpu_default

        Description:  Test with default cutoff_cpu value.

        Arguments:

        """

        mock_es.return_value = self.els

        els = elastic_class.ElasticSearchStatus(self.host_list)

        self.assertEqual(els.chk_all(cutoff_cpu=None), self.results)

    @mock.patch("elastic_class.ElasticSearchStatus.get_cluster",
                mock.Mock(return_value={}))
    @mock.patch("elastic_class.ElasticSearchStatus.chk_disk",
                mock.Mock(return_value={}))
    @mock.patch("elastic_class.ElasticSearchStatus.chk_status",
                mock.Mock(return_value={}))
    @mock.patch("elastic_class.ElasticSearchStatus.chk_server",
                mock.Mock(return_value={}))
    @mock.patch("elastic_class.ElasticSearchStatus.chk_shards",
                mock.Mock(return_value={}))
    @mock.patch("elastic_class.ElasticSearchStatus.chk_nodes",
                mock.Mock(return_value={}))
    @mock.patch("elastic_class.ElasticSearchStatus.chk_mem",
                mock.Mock(return_value={}))
    @mock.patch("elastic_class.ElasticSearchStatus.update_status2",
                mock.Mock(return_value=True))
    @mock.patch("elastic_class.ElasticSearch.update_status",
                mock.Mock(return_value=True))
    @mock.patch("elastic_class.elasticsearch.Elasticsearch")
    def test_cutoff_cpu_value(self, mock_es):

        """Function:  test_cutoff_cpu_value

        Description:  Test with cutoff_cpu value passed.

        Arguments:

        """

        mock_es.return_value = self.els

        els = elastic_class.ElasticSearchStatus(self.host_list)

        self.assertEqual(els.chk_all(cutoff_cpu=50), self.results)

    @mock.patch("elastic_class.ElasticSearchStatus.get_cluster",
                mock.Mock(return_value={}))
    @mock.patch("elastic_class.ElasticSearchStatus.chk_disk",
                mock.Mock(return_value={}))
    @mock.patch("elastic_class.ElasticSearchStatus.chk_status",
                mock.Mock(return_value={
                    "ClusterWarning": {
                        "ClusterStatus": {
                            "Reason": "Detected the cluster is not green",
                            "Status": "yellow"}}}))
    @mock.patch("elastic_class.ElasticSearchStatus.chk_server",
                mock.Mock(return_value={}))
    @mock.patch("elastic_class.ElasticSearchStatus.chk_shards",
                mock.Mock(return_value={}))
    @mock.patch("elastic_class.ElasticSearchStatus.chk_nodes",
                mock.Mock(return_value={}))
    @mock.patch("elastic_class.ElasticSearchStatus.chk_mem",
                mock.Mock(return_value={}))
    @mock.patch("elastic_class.ElasticSearchStatus.update_status2",
                mock.Mock(return_value=True))
    @mock.patch("elastic_class.ElasticSearch.update_status",
                mock.Mock(return_value=True))
    @mock.patch("elastic_class.elasticsearch.Elasticsearch")
    def test_one_warn(self, mock_es):

        """Function:  test_one_warn

        Description:  Test with one warning.

        Arguments:

        """

        mock_es.return_value = self.els

        els = elastic_class.ElasticSearchStatus(self.host_list)

        self.assertEqual(els.chk_all(), self.results2)

    @mock.patch("elastic_class.ElasticSearchStatus.get_cluster",
                mock.Mock(return_value={}))
    @mock.patch("elastic_class.ElasticSearchStatus.chk_disk",
                mock.Mock(return_value={}))
    @mock.patch("elastic_class.ElasticSearchStatus.chk_status",
                mock.Mock(return_value={}))
    @mock.patch("elastic_class.ElasticSearchStatus.chk_server",
                mock.Mock(return_value={}))
    @mock.patch("elastic_class.ElasticSearchStatus.chk_shards",
                mock.Mock(return_value={}))
    @mock.patch("elastic_class.ElasticSearchStatus.chk_nodes",
                mock.Mock(return_value={}))
    @mock.patch("elastic_class.ElasticSearchStatus.chk_mem",
                mock.Mock(return_value={}))
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

        self.assertEqual(els.chk_all(), self.results)


if __name__ == "__main__":
    unittest.main()
