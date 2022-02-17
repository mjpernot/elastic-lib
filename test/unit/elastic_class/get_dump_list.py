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

# Local
sys.path.append(os.getcwd())
import elastic_class
import version

__version__ = version.__version__


class Repo(object):

    """Class:  Repo

    Description:  Class representation of the cat class.

    Methods:
        __init__
        get

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.repository = None
        self.snapshots = {"snapshots": [{"repo": "repo1"}]}
        self.snapshots2 = {"snapshots": [{"repo": "repo1"}, {"repo": "repo2"}]}

    def get(self, repository, snapshot):

        """Method:  get

        Description:  Stub holder for snapshot.get method.

        Arguments:

        """

        self.repository = repository

        if snapshot == "_all":
            return self.snapshots2

        else:
            return self.snapshots

        #return "bkp_name SUCCESS start end\nbkp_name2 SUCCESS start end\n"


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
        test_with_name

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.host_list = ["host1", "host2"]
        self.repo = "reponame"
        self.els = Elasticsearch(self.host_list)
        self.results = {"snapshots": [{"repo": "repo1"}]}
        self.results2 = {"snapshots": [{"repo": "repo1"}, {"repo": "repo2"}]}
        self.name = "repo1"

    def test_without_name(self):

        """Function:  test_without_name

        Description:  Test with no snapshot name passed.

        Arguments:

        """

        self.assertEqual(
            elastic_class.get_dump_list(
                self.els, repo=self.repo), self.results2)

    def test_with_name(self):

        """Function:  test_with_name

        Description:  Test with snapshot name passed.

        Arguments:

        """

        self.assertEqual(
            elastic_class.get_dump_list(
                self.els, repo=self.repo, snapshot=self.name), self.results)


if __name__ == "__main__":
    unittest.main()
