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
import elasticsearch
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
        __init__
        master

    """

    def __init__(self):

        """Method:  __init__

        Description:  Initialization instance of the class.

        Arguments:

        """

        self.format = None
        self.masterlist = [
            {"node": "masternode", "ip": "ip_addr", "host": "hostname",
             "id": "idname"}]

    def master(self, format):

        """Method:  master

        Description:  Stub holder for cat.master method.

        Arguments:

        """

        self.format = format

        return self.masterlist


class Repo2():                                          # pylint:disable=R0903

    """Class:  Repo2

    Description:  Class representation of the cat class.

    Methods:
        __init__
        master

    """

    def __init__(self):

        """Method:  __init__

        Description:  Initialization instance of the class.

        Arguments:

        """

        self.format = None
        self.masterlist = [
            {"node": "masternode", "ip": "ip_addr", "host": "hostname",
             "id": "idname"}]

    def master(self, dataformat):

        """Method:  master

        Description:  Stub holder for cat.master method.

        Arguments:

        """

        self.format = dataformat

        return self.masterlist


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

        if elasticsearch.__version__ >= (8, 0, 0):
            self.cat = Repo()

        else:
            self.cat = Repo2()


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
        self.results = "masternode"

    def test_default(self):

        """Function:  test_default

        Description:  Test with default settings.

        Arguments:

        """

        self.assertEqual(elastic_class.get_master_name(self.els), self.results)


if __name__ == "__main__":
    unittest.main()
