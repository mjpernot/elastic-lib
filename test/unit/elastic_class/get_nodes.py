#!/usr/bin/python
# Classification (U)

"""Program:  get_nodes.py

    Description:  Unit testing of get_nodes in elastic_class class.

    Usage:
        test/unit/elastic_class/get_nodes.py

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
        snapshots -> Stub holder for nodes.info method.

    """

    def info(self):

        """Method:  info

        Description:  Stub holder for nodes.info method.

        Arguments:

        """

        return {"nodes": {"node1": {"data": "/dir/data", "logs": "/dir/logs"},
                          "node2": {"data": "/dir/data2",
                                    "logs": "/dir/logs2"}}}


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
        self.nodes = Repo()


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
        self.repo = "reponame"
        self.els = Elasticsearch(self.host_list)
        self.results = {"node1": {"data": "/dir/data", "logs": "/dir/logs"},
                        "node2": {"data": "/dir/data2", "logs": "/dir/logs2"}}

    def test_default(self):

        """Function:  test_default

        Description:  Test with default settings.

        Arguments:

        """

        self.assertEqual(elastic_class.get_nodes(self.els), self.results)


if __name__ == "__main__":
    unittest.main()
