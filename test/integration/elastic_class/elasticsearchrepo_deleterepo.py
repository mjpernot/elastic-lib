# Classification (U)

"""Program:  elasticsearchrepo_deleterepo.py

    Description:  Integration testing of ElasticSearchRepo.delete_repo
        method in elastic_class.py.

    Usage:
        test/integration/elastic_class/elasticsearchrepo_deleterepo.py

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
import lib.gen_libs as gen_libs             # pylint:disable=E0401,C0413,R0402
import elastic_class                            # pylint:disable=E0401,C0413
import version                                  # pylint:disable=E0401,C0413

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_repo_is_deleted
        test_repo_not_found
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
        self.repo_dir = os.path.join(self.cfg.log_repo_dir, self.repo_name)
        self.phy_repo_dir = os.path.join(self.cfg.phy_repo_dir, self.repo_name)
        esr = elastic_class.ElasticSearchRepo(
            self.cfg.host, repo=self.repo_name)

        if esr.repo_dict:
            print("ERROR: Test environment not clean - repositories exist.")
            self.skipTest("Pre-conditions not met.")

    def test_repo_is_deleted(self):

        """Function:  test_repo_is_deleted

        Description:  Test to see if repo is deleted.

        Arguments:

        """

        esr = elastic_class.ElasticSearchRepo(
            self.cfg.host, repo=self.repo_name, repo_dir=self.repo_dir,
            user=self.cfg.user, japd=self.cfg.japd)
        esr.connect()
        esr.create_repo()
        status, msg = esr.delete_repo()

        self.assertEqual((status, msg), (False, None))

    def test_repo_not_found(self):

        """Function:  test_repo_not_found

        Description:  Test to see if repository is not found.

        Arguments:

        """

        esr = elastic_class.ElasticSearchRepo(
            self.cfg.host, repo=self.repo_name, user=self.cfg.user,
            japd=self.cfg.japd)
        esr.connect()
        status, msg = esr.delete_repo()

        self.assertEqual(
            (status, msg),
            (True, "ERROR: Missing repo or does not exist: TEST_REPO"))

    def test_repo_name_not_set(self):

        """Function:  test_repo_name_not_set

        Description:  Test to see if repo name is not set.

        Arguments:

        """

        esr = elastic_class.ElasticSearchRepo(
            self.cfg.host, user=self.cfg.user, japd=self.cfg.japd)
        esr.connect()
        status, msg = esr.delete_repo()

        self.assertEqual(
            (status, msg),
            (True, "ERROR: Missing repo or does not exist: None"))

    def tearDown(self):

        """Function:  tearDown

        Description:  Clean up of integration testing.

        Arguments:

        """

        if os.path.isdir(self.phy_repo_dir):
            shutil.rmtree(self.phy_repo_dir)


if __name__ == "__main__":
    unittest.main()
