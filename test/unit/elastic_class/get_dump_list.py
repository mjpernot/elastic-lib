#!/usr/bin/python
# Classification (U)

"""Program:  get_dump_list.py

    Description:  Unit testing of get_dump_list in elastic_class class.

    Usage:
        test/unit/elastic_class/get_dump_list.py

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
import lib.gen_libs as gen_libs
import version

__version__ = version.__version__


class Repo(object):

    """Class:  Repo

    Description:  Class representation of the cat class.

    Methods:
        snapshots -> Stub holder for cat.snapshots method.

    """

    def snapshots(self, repository):

        """Method:  snapshots

        Description:  Stub holder for cat.snapshots method.

        Arguments:

        """

        return "bkp_name SUCCESS start end\nbkp_name2 SUCCESS start end\n"


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
        self.snapshot = Repo()


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
        self.es = Elasticsearch(self.host_list)
        self.results = [["bkp_name", "SUCCESS", "start", "end"],
                        ["bkp_name2", "SUCCESS", "start", "end"]]

    def test_default(self, mock_es):

        """Function:  test_default

        Description:  Test with default settings.

        Arguments:

        """

        self.assertEqual(elastic_class.get_dump_list(self.es, repo=self.repo),
                         self.results)


if __name__ == "__main__":
    unittest.main()
