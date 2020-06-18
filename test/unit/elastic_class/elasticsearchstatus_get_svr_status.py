#!/usr/bin/python
# Classification (U)

"""Program:  elasticsearchstatus_get_svr_status.py

    Description:  Unit testing of get_svr_status in
        elastic_class.ElasticSearchStatus.

    Usage:
        test/unit/elastic_class/elasticsearchstatus_get_svr_status.py

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
        test_default -> Test with default settings.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.host_list = ["host1", "host2"]
        self.els = Elasticsearch(self.host_list)
        self.uptime = 1234567890
        self.alloc_cpu = 3
        self.cpu_active = 2
        self.results = {
            "Server": {"Uptime": "14 days 6 hours 56 minutes 7 seconds",
                       "AllocatedCPU": 3, "CPUActive": 2}}

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

        els = elastic_class.ElasticSearchStatus(self.host_list)
        els.uptime = self.uptime
        els.alloc_cpu = self.alloc_cpu
        els.cpu_active = self.cpu_active

        self.assertEqual(els.get_svr_status(), self.results)


if __name__ == "__main__":
    unittest.main()
