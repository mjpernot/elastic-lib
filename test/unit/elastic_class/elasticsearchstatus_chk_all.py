#!/usr/bin/python
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
        test_one_warn -> Test with one warning.
        test_default_no_warn -> Test with default settings and no warning.

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
