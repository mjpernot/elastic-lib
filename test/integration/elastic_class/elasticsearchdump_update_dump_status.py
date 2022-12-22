# Classification (U)

"""Program:  elasticsearchdump_update_dump_status.py

    Description:  Integration testing of update_dump_status in
        ElasticSearchDump class in elastic_class.py.

    Usage:
        test/integration/elastic_class/elasticsearchdump_update_dump_status.py

    Arguments:

"""

# Libraries and Global Variables
from __future__ import print_function

# Standard
import sys
import os
import unittest

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
        test_repo_not_passed
        test_dump_list_is_empty
        test_dump_name_set

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
        self.phy_repo_dir = os.path.join(self.cfg.phy_repo_dir, self.repo_name)

        esr = elastic_class.ElasticSearchRepo(
            self.cfg.host, repo=self.repo_name, repo_dir=self.repo_dir)

        if esr.repo_dict:
            print("ERROR: Test environment not clean - repositories exist.")
            self.skipTest("Pre-conditions not met.")

    def test_repo_not_passed(self):

        """Function:  test_repo_not_passed

        Description:  Test if repo name is not passed to program.

        Arguments:

        """

        esd = elastic_class.ElasticSearchDump(
            self.cfg.host, user=self.cfg.user, japd=self.cfg.japd)
        esd.connect()

        if esd.repo_name:
            self.assertTrue(esd.repo_name and esd.type)

        else:
            self.assertTrue(not esd.repo_name and not esd.type)

    def test_dump_list_is_empty(self):

        """Function:  test_dump_list_is_empty

        Description:  Test to see if dump_list is empty.

        Arguments:

        """

        esd = elastic_class.ElasticSearchDump(
            self.cfg.host, repo=self.repo_name, user=self.cfg.user,
            japd=self.cfg.japd)
        esd.connect()

        self.assertTrue(not esd.dump_list)

    def test_dump_name_set(self):

        """Function:  test_dump_name_set

        Description:  Test to see dump_name is set.

        Arguments:

        """

        esd = elastic_class.ElasticSearchDump(
            self.cfg.host, user=self.cfg.user, japd=self.cfg.japd)
        esd.connect()

        self.assertTrue(esd.dump_name)


if __name__ == "__main__":
    unittest.main()
