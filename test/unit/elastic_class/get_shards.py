#!/usr/bin/python
# Classification (U)

"""Program:  get_shards.py

    Description:  Unit testing of get_shards in elastic_class class.

    Usage:
        test/unit/elastic_class/get_shards.py

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

# Local
sys.path.append(os.getcwd())
import elastic_class
import version

__version__ = version.__version__


class Repo(object):

    """Class:  Repo

    Description:  Class representation of the cat class.

    Methods:
        __init__
        shards

    """

    def __init__(self):

        """Method:  __init__

        Description:  Initialization instance of the class.

        Arguments:

        """

        self.format = None
        self.shard_list = [
            {"node": "nodename", "index": "indexname", "docs": "10",
             "shard": "0", "state": "STARTED", "prirep": "p", "ip": "ip_addr",
             "store": "5mb"},
            {"node": "nodename2", "index": "indexname2", "docs": "20",
             "shard": "0", "state": "STARTED", "prirep": "p", "ip": "ip_addr2",
             "store": "15mb"}]

    def shards(self, format):

        """Method:  shards

        Description:  Stub holder for cat.shards method.

        Arguments:

        """

        self.format = format

        return self.shard_list


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
        self.cat = Repo()


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_default

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.host_list = ["host1", "host2"]
        self.repo = "reponame"
        self.els = Elasticsearch(self.host_list)
        self.results = [
            {"node": "nodename", "index": "indexname", "docs": "10",
             "shard": "0", "state": "STARTED", "prirep": "p", "ip": "ip_addr",
             "store": "5mb"},
            {"node": "nodename2", "index": "indexname2", "docs": "20",
             "shard": "0", "state": "STARTED", "prirep": "p", "ip": "ip_addr2",
             "store": "15mb"}]

    def test_default(self):

        """Function:  test_default

        Description:  Test with default settings.

        Arguments:

        """

        self.assertEqual(elastic_class.get_shards(self.els), self.results)


if __name__ == "__main__":
    unittest.main()
