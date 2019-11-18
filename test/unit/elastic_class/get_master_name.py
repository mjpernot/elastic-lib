#!/usr/bin/python
# Classification (U)

"""Program:  get_master_name.py

    Description:  Unit testing of get_master_name in elastic_class class.

    Usage:
        test/unit/elastic_class/get_master_name.py

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
        master -> Stub holder for cat.master method.

    """

    def master(self):

        """Method:  master

        Description:  Stub holder for cat.master method.

        Arguments:

        """

        return "serverid hostip serverip servername\n"


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
        self.cat = Repo()


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
        self.results = "servername"

    def test_default(self):

        """Function:  test_default

        Description:  Test with default settings.

        Arguments:

        """

        self.assertEqual(elastic_class.get_master_name(self.es), self.results)


if __name__ == "__main__":
    unittest.main()
