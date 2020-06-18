#!/usr/bin/python
# Classification (U)

"""Program:  ElasticSearchStatus_get_dump_disk_status.py

    Description:  Unit testing of get_dump_disk_status in
        elastic_class.ElasticSearchStatus.

    Usage:
        test/unit/elastic_class/ElasticSearchStatus_get_dump_disk_status.py

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
import collections

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

        # This is set to allow to show large differences.
        self.maxDiff = None
        self.host_list = ["host1", "host2"]
        self.es = Elasticsearch(self.host_list)
        self.repo_dict = {"repo1": {"settings": {"location": "/dir/repo1"}},
                          "repo2": {"settings": {"location": "/dir/repo2"}}}
        self.results = {
            "DumpUsage": {"repo1": {"Used": "15.00GB",
                                    "Partition": "/dir/repo1",
                                    "Percent": 28.30188679245283,
                                    "Free": "68.00MB",
                                    "Total": "53.00GB"},
                          "repo2": {"Used": "14.00GB",
                                    "Partition": "/dir/repo2",
                                    "Percent": 26.41509433962264,
                                    "Free": "67.00MB",
                                    "Total": "53.00GB"}}}

        usage = collections.namedtuple('USAGE', 'total used free')
        self.usage1 = usage(56908316672, 16106127360, 71303168)
        self.usage2 = usage(56908316672, 15032385536, 70254592)

    @mock.patch("elastic_class.gen_libs.disk_usage")
    @mock.patch("elastic_class.ElasticSearchStatus.update_status2",
                mock.Mock(return_value=True))
    @mock.patch("elastic_class.ElasticSearch.update_status",
                mock.Mock(return_value=True))
    @mock.patch("elastic_class.elasticsearch.Elasticsearch")
    def test_default(self, mock_es, mock_libs):

        """Function:  test_default

        Description:  Test with default settings.

        Arguments:

        """

        mock_es.return_value = self.es
        mock_libs.side_effect = [self.usage1, self.usage2]

        es = elastic_class.ElasticSearchStatus(self.host_list)
        es.repo_dict = self.repo_dict

        self.assertEqual(es.get_dump_disk_status(), self.results)


if __name__ == "__main__":
    unittest.main()
