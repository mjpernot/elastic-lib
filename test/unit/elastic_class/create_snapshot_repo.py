#!/usr/bin/python
# Classification (U)

"""Program:  create_snapshot_repo.py

    Description:  Unit testing of create_snapshot_repo in elastic_class class.

    Usage:
        test/unit/elastic_class/create_snapshot_repo.py

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

    Description:  Class representation of the snapshot class.

    Methods:
        create_repository -> Stub for snapshot.create_repository method.

    """

    def create_repository(self, reponame, body, verify):

        """Method:  create_repository

        Description:  Stub for snapshot.create_repository method.

        Arguments:
            (input) repository -> Name of repository.
            (input) body -> Dictionary of dump arguments.
            (input) verify -> True|False - Verify the repository.

        """

        pass


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
        self.repo_name = "reponame"
        self.body = {"indices": "dbs", "ignore_unavailable": True}
        self.es = Elasticsearch(self.host_list)

    def test_default(self):

        """Function:  test_default

        Description:  Test with default settings.

        Arguments:

        """

        self.assertFalse(elastic_class.create_snapshot(
            self.es, repository=self.repo_name, body=self.body,
            verify=True))


if __name__ == "__main__":
    unittest.main()
