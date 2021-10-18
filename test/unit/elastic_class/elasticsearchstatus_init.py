#!/usr/bin/python
# Classification (U)

"""Program:  elasticsearchstatus_init.py

    Description:  Unit testing of __init__ in elastic_class.ElasticSearchStatus
        class.

    Usage:
        test/unit/elastic_class/elasticsearchstatus_init.py

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
        info

    """

    def __init__(self, host_list, port=9200):

        """Method:  __init__

        Description:  Initialization instance of the class.

        Arguments:

        """

        self.hosts = host_list
        self.port = port
        self.ping_status = True
        self.info_status = {"cluster_name":
                            "ClusterName", "name": "servername"}

    def info(self):

        """Method:  info

        Description:  Stub holder for Elasticsearch.info method.

        Arguments:

        """

        return self.info_status


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_disk_arg
        test_cpu_arg
        test_mem_arg
        test_default

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.host_list = ["host1", "host2"]
        self.els = Elasticsearch(self.host_list)

    @mock.patch("elastic_class.ElasticSearch.update_status",
                mock.Mock(return_value=True))
    @mock.patch("elastic_class.ElasticSearchStatus.update_status2",
                mock.Mock(return_value=True))
    def test_disk_arg(self):

        """Function:  test_disk_arg

        Description:  Test passing disk argument.

        Arguments:

        """

        els = elastic_class.ElasticSearchStatus(self.host_list, cutoff_disk=30)
        self.assertEqual((els.hosts, els.cutoff_disk), (self.host_list, 30))

    @mock.patch("elastic_class.ElasticSearch.update_status",
                mock.Mock(return_value=True))
    @mock.patch("elastic_class.ElasticSearchStatus.update_status2",
                mock.Mock(return_value=True))
    def test_cpu_arg(self):

        """Function:  test_cpu_arg

        Description:  Test passing cpu argument.

        Arguments:

        """

        els = elastic_class.ElasticSearchStatus(self.host_list, cutoff_cpu=20)
        self.assertEqual((els.hosts, els.cutoff_cpu), (self.host_list, 20))

    @mock.patch("elastic_class.ElasticSearch.update_status",
                mock.Mock(return_value=True))
    @mock.patch("elastic_class.ElasticSearchStatus.update_status2",
                mock.Mock(return_value=True))
    def test_mem_arg(self):

        """Function:  test_mem_arg

        Description:  Test passing memory argument.

        Arguments:

        """

        els = elastic_class.ElasticSearchStatus(self.host_list, cutoff_mem=10)
        self.assertEqual((els.hosts, els.cutoff_mem), (self.host_list, 10))

    @mock.patch("elastic_class.ElasticSearch.update_status",
                mock.Mock(return_value=True))
    @mock.patch("elastic_class.ElasticSearchStatus.update_status2",
                mock.Mock(return_value=True))
    def test_default(self):

        """Function:  test_default

        Description:  Test with default settings.

        Arguments:

        """

        els = elastic_class.ElasticSearchStatus(self.host_list)
        self.assertEqual((els.hosts, els.failed_nodes, els.alloc_cpu,
                          els.cpu_active, els.pending_tasks),
                         (self.host_list, None, None, None, None))


if __name__ == "__main__":
    unittest.main()
