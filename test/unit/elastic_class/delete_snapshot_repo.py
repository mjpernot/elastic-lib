# Classification (U)

"""Program:  delete_snapshot_repo.py

    Description:  Unit testing of delete_snapshot_repo in elastic_class class.

    Usage:
        test/unit/elastic_class/delete_snapshot_repo.py

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

    Description:  Class representation of the snapshot class.

    Methods:
        __init__
        delete_repository

    """

    def __init__(self):

        """Method:  __init__

        Description:  Initialization of class.

        Arguments:

        """

        self.name = None

    def delete_repository(self, name):

        """Method:  delete_repository

        Description:  Stub for snapshot.delete_repository method.

        Arguments:

        """

        self.name = name

        return {"acknowledged": True}


class Repo2():                                           # pylint:disable=R0903

    """Class:  Repo2

    Description:  Class representation of the snapshot class.

    Methods:
        __init__
        delete_repository

    """

    def __init__(self):

        """Method:  __init__

        Description:  Initialization of class.

        Arguments:

        """

        self.repository = None

    def delete_repository(self, repository):

        """Method:  delete_repository

        Description:  Stub for snapshot.delete_repository method.

        Arguments:

        """

        self.repository = repository

        return {"acknowledged": True}


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
            self.snapshot = Repo()

        else:
            self.snapshot = Repo2()


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
        self.els = Elasticsearch(self.host_list)
        self.results = {"acknowledged": True}

    def test_default(self):

        """Function:  test_default

        Description:  Test with default settings.

        Arguments:

        """

        self.assertEqual(elastic_class.delete_snapshot_repo(
            self.els, self.repo_name), self.results)


if __name__ == "__main__":
    unittest.main()
