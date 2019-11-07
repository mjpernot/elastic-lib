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

        self.host_list = ["host1", "host2"]
        self.es = Elasticsearch(self.host_list)
        self.repo_dict = {"repo1": {"settings": {"location": "/dir/repo1"}},
                          "repo2": {"settings": {"location": "/dir/repo2"}}}
        self.results = {
            "DumpUsage": {"repo1": {"Partition": "/dir/repo1",
                                    "Total": "53gb",
                                    "Used": "15gb",
                                    "Free": "68mb",
                                    "Precent": 23},
                          "repo2": {"Partition": "/dir/repo2",
                                    "Total": "53gb",
                                    "Used": "14gb",
                                    "Free": "67mb",
                                    "Precent": 22}}}

        usage = collections.namedtuple('USAGE', 'total used free')
        self.usage1 = usage(53, 15, 68)
        self.usage2 = usage(53, 14, 67)

    @mock.patch("elastic_class.gen_libs")
    @mock.patch("elastic_class.ElasticSearchStatus.update_status",
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
        mock_libs.disk_usage.side_effect = [self.usage1, self.usage2]

        es = elastic_class.ElasticSearchStatus(self.host_list)
        es.repo_dict = self.repo_dict

        self.assertEqual(es.get_dump_disk_status(), self.results)


if __name__ == "__main__":
    unittest.main()
