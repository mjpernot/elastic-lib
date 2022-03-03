#!/usr/bin/python
# Classification (U)

"""Program:  get_disks.py

    Description:  Unit testing of get_disks in elastic_class class.

    Usage:
        test/unit/elastic_class/get_disks.py

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
        allocation

    """

    def __init__(self):

        """Method:  __init__

        Description:  Initialization instance of the class.

        Arguments:

        """

        self.format = None
        self.disks = [
            {"node": "nodename", "disk.total": "100gb", "shards": "101",
             "disk.avail": "75gb", "disk.used": "20gb", "host": "servername",
             "disk.percent": "21", "ip": "ip.addr", "disk.indices": "15gb"},
            {"node": "nodename2", "disk.total": "110gb", "shards": "101",
             "disk.avail": "65gb", "disk.used": "30gb", "host": "servername2",
             "disk.percent": "31", "ip": "ip.addr2", "disk.indices": "20gb"}]

    def allocation(self, format):

        """Method:  allocation

        Description:  Stub holder for cat.allocation method.

        Arguments:

        """

        self.format = format

        return self.disks


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
            {"node": "nodename", "disk.total": "100gb", "shards": "101",
             "disk.avail": "75gb", "disk.used": "20gb", "host": "servername",
             "disk.percent": "21", "ip": "ip.addr", "disk.indices": "15gb"},
            {"node": "nodename2", "disk.total": "110gb", "shards": "101",
             "disk.avail": "65gb", "disk.used": "30gb", "host": "servername2",
             "disk.percent": "31", "ip": "ip.addr2", "disk.indices": "20gb"}]

    def test_default(self):

        """Function:  test_default

        Description:  Test with default settings.

        Arguments:

        """

        self.assertEqual(elastic_class.get_disks(self.els), self.results)


if __name__ == "__main__":
    unittest.main()
