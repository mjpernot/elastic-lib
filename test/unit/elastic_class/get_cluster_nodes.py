# Classification (U)

"""Program:  get_cluster_nodes.py

    Description:  Unit testing of get_cluster_nodes in elastic_class class.

    Usage:
        test/unit/elastic_class/get_cluster_nodes.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import unittest

# Local
sys.path.append(os.getcwd())
import elastic_class                            # pylint:disable=E0401,C0413
import version                                  # pylint:disable=E0401,C0413

__version__ = version.__version__


class Repo():                                           # pylint:disable=R0903

    """Class:  Repo

    Description:  Class representation of the cat class.

    Methods:
        snapshots

    """

    def info(self):

        """Method:  info

        Description:  Stub holder for nodes.info method.

        Arguments:

        """

        return {"node1": {"data": "/dir/data", "logs": "/dir/logs"},
                "node2": {"data": "/dir/data2", "logs": "/dir/logs2"}}


class Elasticsearch():                                  # pylint:disable=R0903

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
        self.nodes = Repo()


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
        self.results = {"node1": {"data": "/dir/data", "logs": "/dir/logs"},
                        "node2": {"data": "/dir/data2", "logs": "/dir/logs2"}}

    def test_default(self):

        """Function:  test_default

        Description:  Test with default settings.

        Arguments:

        """

        self.assertEqual(elastic_class.get_cluster_nodes(self.els),
                         self.results)


if __name__ == "__main__":
    unittest.main()
