#!/usr/bin/python
# Classification (U)

"""Program:  delete_snapshot.py

    Description:  Unit testing of delete_snapshot in elastic_class class.

    Usage:
        test/unit/elastic_class/delete_snapshot.py

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
        delete

    """

    def __init__(self):

        """Method:  __init__

        Description:  Initialization of class.

        Arguments:

        """

        self.repository = None
        self.snapshot = None

    def delete(self, repository, snapshot):

        """Method:  delete

        Description:  Stub holder for snapshot.delete method.

        Arguments:

        """

        self.repository = repository
        self.snapshot = snapshot

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
        self.dump_name = "dumpname"
        self.els = Elasticsearch(self.host_list)
        self.results = {"acknowledged": True}

    def test_default(self):

        """Function:  test_default

        Description:  Test with default settings.

        Arguments:

        """

        self.assertEqual(elastic_class.delete_snapshot(
            self.els, self.repo_name, self.dump_name), self.results)


if __name__ == "__main__":
    unittest.main()
