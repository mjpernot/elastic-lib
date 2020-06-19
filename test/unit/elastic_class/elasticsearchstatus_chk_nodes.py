#!/usr/bin/python
# Classification (U)

"""Program:  elasticsearchstatus_chk_nodes.py

    Description:  Unit testing of chk_nodes in
        elastic_class.ElasticSearchStatus.

    Usage:
        test/unit/elastic_class/elasticsearchstatus_chk_nodes.py

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
        self.failed_nodes = 0
        self.failed_nodes2 = 1
        self.total_nodes = 3
        self.results = {}
        self.results2 = {
            "NodeFailure": {"Reason": "Detected failure on one or more nodes",
                            "FailedNodes": self.failed_nodes2,
                            "TotalNodes": self.total_nodes}}

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
        els.failed_nodes = self.failed_nodes2
        els.total_nodes = self.total_nodes

        self.assertEqual(els.chk_nodes(), self.results2)

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
        els.failed_nodes = self.failed_nodes
        els.total_nodes = self.total_nodes

        self.assertEqual(els.chk_nodes(), self.results)


if __name__ == "__main__":
    unittest.main()
