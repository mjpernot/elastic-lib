# Classification (U)

"""Program:  elasticsearchrepo_createrepo.py

    Description:  Integration testing of ElasticSearchRepo.create_repo
        method in elastic_class.py.

    Usage:
        test/integration/elastic_class/elasticsearchrepo_createrepo.py

    Arguments:

"""

# Libraries and Global Variables
from __future__ import print_function

# Standard
import sys
import os
import shutil
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
        test_repo_is_created
        test_repo_dir_is_passed
        test_repo_dir_is_set
        test_repo_name_is_passed
        test_repo_name_is_set
        test_repo_name_not_set
        tearDown

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
        self.repo_name = "TEST_REPO"
        self.repo_name2 = "TEST_REPO2"
        self.repo_dir = os.path.join(self.cfg.log_repo_dir, self.repo_name)
        self.phy_repo_dir = os.path.join(self.cfg.phy_repo_dir, self.repo_name)
        self.repo_dir2 = "/REP_DIR"
        self.repo_dir3 = "/REP_DIR3"
        esr = elastic_class.ElasticSearchRepo(
            self.cfg.host, repo=self.repo_name)

        if esr.repo_dict:
            print("ERROR: Test environment not clean - repositories exist.")
            self.skipTest("Pre-conditions not met.")

    def test_repo_is_created(self):

        """Function:  test_repo_is_created

        Description:  Test to see if repo is created.

        Arguments:

        """

        esr = elastic_class.ElasticSearchRepo(
            self.cfg.host, repo=self.repo_name, repo_dir=self.repo_dir,
            user=self.cfg.user, japd=self.cfg.japd)
        esr.connect()
        status, msg = esr.create_repo()

        self.assertEqual((status, msg), (False, None))

        esr.delete_repo()

    def test_repo_dir_is_passed(self):

        """Function:  test_repo_dir_is_passed

        Description:  Test to see if repo directory is passed.

        Arguments:

        """

        esr = elastic_class.ElasticSearchRepo(
            self.cfg.host, repo_dir=self.repo_dir2, user=self.cfg.user,
            japd=self.cfg.japd)

        status, msg = esr.create_repo(repo_dir=self.repo_dir3)

        self.assertEqual(
            (status, msg),
            (True,
             "ERROR: Missing repo name or directory: 'None', '/REP_DIR3'"))

    def test_repo_dir_is_set(self):

        """Function:  test_repo_dir_is_set

        Description:  Test to see if repo directory is set.

        Arguments:

        """

        esr = elastic_class.ElasticSearchRepo(
            self.cfg.host, repo_dir=self.repo_dir2, user=self.cfg.user,
            japd=self.cfg.japd)
        esr.connect()
        status, msg = esr.create_repo()

        self.assertEqual(
            (status, msg),
            (True,
             "ERROR: Missing repo name or directory: 'None', '/REP_DIR'"))

    def test_repo_name_is_passed(self):

        """Function:  test_repo_name_is_passed

        Description:  Test to see if repo name is passed.

        Arguments:

        """

        esr = elastic_class.ElasticSearchRepo(
            self.cfg.host, repo=self.repo_name, user=self.cfg.user,
            japd=self.cfg.japd)
        esr.connect()
        status, msg = esr.create_repo(repo_name=self.repo_name2)

        self.assertEqual(
            (status, msg),
            (True,
             "ERROR: Missing repo name or directory: 'TEST_REPO2', 'None'"))

    def test_repo_name_is_set(self):

        """Function:  test_repo_name_is_set

        Description:  Test to see if repo name is set.

        Arguments:

        """

        esr = elastic_class.ElasticSearchRepo(
            self.cfg.host, repo=self.repo_name, user=self.cfg.user,
            japd=self.cfg.japd)
        esr.connect()
        status, msg = esr.create_repo()

        self.assertEqual(
            (status, msg),
            (True,
             "ERROR: Missing repo name or directory: 'TEST_REPO', 'None'"))

    def test_repo_name_not_set(self):

        """Function:  test_repo_name_not_set

        Description:  Test to see if repo name is not set.

        Arguments:

        """

        esr = elastic_class.ElasticSearchRepo(
            self.cfg.host, user=self.cfg.user, japd=self.cfg.japd)
        esr.connect()
        status, msg = esr.create_repo()

        self.assertEqual(
            (status, msg),
            (True, "ERROR: Missing repo name or directory: 'None', 'None'"))

    def tearDown(self):

        """Function:  tearDown

        Description:  Clean up of integration testing.

        Arguments:

        """

        if os.path.isdir(self.phy_repo_dir):
            shutil.rmtree(self.phy_repo_dir)


if __name__ == "__main__":
    unittest.main()
