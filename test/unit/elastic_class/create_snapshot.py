# Classification (U)

"""Program:  create_snapshot.py

    Description:  Unit testing of create_snapshot in elastic_class class.

    Usage:
        test/unit/elastic_class/create_snapshot.py

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

    Description:  Class representation of the snapshot class.

    Methods:
        create

    """

    def create(self, repository, body, snapshot):

        """Method:  create

        Description:  Stub holder for snapshot.create method.

        Arguments:

        """


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
        self.snapshot = Repo()


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
        self.repo_name = "reponame"
        self.body = {"indices": "dbs", "ignore_unavailable": True}
        self.dump_name = "dumpname"
        self.els = Elasticsearch(self.host_list)

    def test_default(self):

        """Function:  test_default

        Description:  Test with default settings.

        Arguments:

        """

        self.assertFalse(elastic_class.create_snapshot(
            self.els, self.repo_name, self.body, self.dump_name))


if __name__ == "__main__":
    unittest.main()
