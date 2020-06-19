#!/usr/bin/python
# Classification (U)

"""Program:  elasticsearchstatus_chk_status.py

    Description:  Unit testing of chk_status in
        elastic_class.ElasticSearchStatus.

    Usage:
        test/unit/elastic_class/elasticsearchstatus_chk_status.py

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
        test_tasks_warn -> Test with pending tasks warning.
        test_status_warn -> Test with cluster status warning.
        test_no_warn -> Test with no warnings.

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
        self.cluster_status = "green"
        self.cluster_status2 = "yellow"
        self.pending_tasks = 0
        self.pending_tasks2 = 10
        self.results = {}
        self.results2 = {
            "ClusterWarning": {"ClusterStatus": {
                "Reason": "Detected the cluster is not green",
                "Status": self.cluster_status2}}}
        self.results3 = {
            "ClusterWarning": {"PendingTasks": {
                "Reason": "Detected cluster has pending tasks",
                "Tasks": self.pending_tasks2}}}

    @mock.patch("elastic_class.ElasticSearchStatus.update_status2",
                mock.Mock(return_value=True))
    @mock.patch("elastic_class.ElasticSearch.update_status",
                mock.Mock(return_value=True))
    @mock.patch("elastic_class.elasticsearch.Elasticsearch")
    def test_tasks_warn(self, mock_es):

        """Function:  test_tasks_warn

        Description:  Test with pending tasks warning.

        Arguments:

        """

        mock_es.return_value = self.els

        els = elastic_class.ElasticSearchStatus(self.host_list)
        els.cluster_status = self.cluster_status
        els.pending_tasks = self.pending_tasks2

        self.assertEqual(els.chk_status(), self.results3)

    @mock.patch("elastic_class.ElasticSearchStatus.update_status2",
                mock.Mock(return_value=True))
    @mock.patch("elastic_class.ElasticSearch.update_status",
                mock.Mock(return_value=True))
    @mock.patch("elastic_class.elasticsearch.Elasticsearch")
    def test_status_warn(self, mock_es):

        """Function:  test_status_warn

        Description:  Test with cluster status warning.

        Arguments:

        """

        mock_es.return_value = self.els

        els = elastic_class.ElasticSearchStatus(self.host_list)
        els.cluster_status = self.cluster_status2
        els.pending_tasks = self.pending_tasks

        self.assertEqual(els.chk_status(), self.results2)

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
        els.cluster_status = self.cluster_status
        els.pending_tasks = self.pending_tasks

        self.assertEqual(els.chk_status(), self.results)


if __name__ == "__main__":
    unittest.main()
