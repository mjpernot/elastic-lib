#!/usr/bin/python
# Classification (U)

"""Program:  elasticsearchrepo.py

    Description:  Integration testing of ElasticSearchRepo in elastic_class.py.

    Usage:
        test/integration/elastic_class/elasticsearchrepo.py

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
import lib.gen_libs as gen_libs
import elastic_class
import version

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_repo_is_set
        test_connect
        test_init

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.base_dir = "test/integration/elastic_class"
        self.test_path = os.path.join(os.getcwd(), self.base_dir)
        self.config_path = os.path.join(self.test_path, "config")
        self.cfg = gen_libs.load_module("elastic", self.config_path)
        self.repo_name = "TEST_INTR_REPO"
        self.repo_dir = os.path.join(self.cfg.log_repo_dir, self.repo_name)
        esr = elastic_class.ElasticSearchRepo(self.cfg.host,
                                              repo=self.repo_name)

        if esr.repo_dict:
            print("ERROR: Test environment not clean - repositories exist.")
            self.skipTest("Pre-conditions not met.")

    def test_repo_is_set(self):

        """Function:  test_repo_not_exist

        Description:  Test if repo attributes are set properly.

        Arguments:

        """

        esr = elastic_class.ElasticSearchRepo(
            self.cfg.host, repo=self.repo_name, repo_dir=self.repo_dir)

        self.assertTrue(
            esr.repo == self.repo_name and esr.repo_dir == self.repo_dir)

    def test_connect(self):

        """Function:  test_connect

        Description:  Test to successfully connect to Elasticsearch.

        Arguments:

        """

        esr = elastic_class.ElasticSearchRepo(self.cfg.host)

        self.assertTrue(not esr.repo and not esr.repo_dict)

    def test_init(self):

        """Function:  test_init

        Description:  Test to see if class instance is created.

        Arguments:

        """

        host_list = "Host_Name"
        esr = elastic_class.ElasticSearchRepo(host_list)

        self.assertTrue(not esr.repo)


if __name__ == "__main__":
    unittest.main()
