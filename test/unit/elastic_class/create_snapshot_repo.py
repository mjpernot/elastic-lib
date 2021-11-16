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
        __init__
        create_repository

    """

    def __init__(self):

        """Method:  __init__

        Description:  Initialization of class.

        Arguments:

        """

        self.repository = None
        self.body = None
        self.verify = None

    def create_repository(self, repository, body, verify):

        """Method:  create_repository

        Description:  Stub for snapshot.create_repository method.

        Arguments:

        """

        self.repository = repository
        self.body = body
        self.verify = verify

        return {"acknowledged": True}


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
        self.snapshot = Repo()
        self.results = {"acknowledged": True}


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
        self.els = Elasticsearch(self.host_list)
        self.results = {"acknowledged": True}

    def test_default(self):

        """Function:  test_default

        Description:  Test with default settings.

        Arguments:

        """

        self.assertEqual(elastic_class.create_snapshot_repo(
            self.els, self.repo_name, self.body, True), self.results)


if __name__ == "__main__":
    unittest.main()
