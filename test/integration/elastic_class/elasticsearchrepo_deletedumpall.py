#!/usr/bin/python
# Classification (U)

"""Program:  elasticsearchrepo_deletedumpall.py

    Description:  Integration testing of ElasticSearchRepo.delete_dump_all
        method in elastic_class.py.

    Usage:
        test/integration/elastic_class/elasticsearchrepo_deletedumpall.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import shutil

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
        test_dumps_are_deleted
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
        self.dump_name = "test_dump"
        self.dump_name2 = "test_dump2"
        self.repo_dir = os.path.join(self.cfg.log_repo_dir, self.repo_name)
        self.phy_repo_dir = os.path.join(self.cfg.phy_repo_dir, self.repo_name)
        esr = elastic_class.ElasticSearchRepo(self.cfg.host,
                                              repo=self.repo_name)

        if esr.repo_dict:
            print("ERROR: Test environment not clean - repositories exist.")
            self.skipTest("Pre-conditions not met.")

    def test_dumps_are_deleted(self):

        """Function:  test_dumps_are_deleted

        Description:  Test to see if dumps are deleted.

        Arguments:

        """

        esr = elastic_class.ElasticSearchRepo(
            self.cfg.host, repo=self.repo_name, repo_dir=self.repo_dir)
        esr.create_repo()

        esd = elastic_class.ElasticSearchDump(self.cfg.host,
                                              repo=self.repo_name)
        esd.dump_name = self.dump_name
        esd.dump_db()
        esd.dump_name = self.dump_name2
        esd.dump_db()

        status, msg = esr.delete_dump_all(dump_name=self.dump_name)

        esd2 = elastic_class.ElasticSearchDump(self.cfg.host,
                                               repo=self.repo_name)

        esr.delete_repo()

        self.assertEqual((status, msg, len(esd2.dump_list)), (False, None, 0))

    def test_repo_not_found(self):

        """Function:  test_repo_not_found

        Description:  Test to see if repository is not found.

        Arguments:

        """

        esr = elastic_class.ElasticSearchRepo(self.cfg.host,
                                              repo=self.repo_name)

        status, msg = esr.delete_dump_all()

        self.assertEqual(
            (status, msg),
            (True,
             "ERROR:  Repo:  TEST_REPO is not present or missing argument."))

    def test_repo_name_not_set(self):

        """Function:  test_repo_name_not_set

        Description:  Test to see if repo name is not set.

        Arguments:

        """

        esr = elastic_class.ElasticSearchRepo(self.cfg.host)

        status, msg = esr.delete_dump_all()

        self.assertEqual(
            (status, msg),
            (True, "ERROR:  Repo:  None is not present or missing argument."))

    def tearDown(self):

        """Function:  tearDown

        Description:  Clean up of integration testing.

        Arguments:

        """

        if os.path.isdir(self.phy_repo_dir):
            shutil.rmtree(self.phy_repo_dir)


if __name__ == "__main__":
    unittest.main()
