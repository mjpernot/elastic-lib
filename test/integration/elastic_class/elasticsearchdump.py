#!/usr/bin/python
# Classification (U)

"""Program:  elasticsearchdump.py

    Description:  Integration testing of ElasticSearchDump in elastic_class.py.

    Usage:
        test/integration/elastic_class/elasticsearchdump.py

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
        test_dump_list_is_set
        test_dump_list_is_empty
        test_repo_is_set
        test_repo_not_set
        test_multi_repo
        test_single_repo
        test_repo_not_passed
        test_repo_not_exist
        test_connect
        test_init
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
        self.repo_name = "TEST_INTR_REPO"
        self.repo_name2 = "TEST_INTR_REPO2"
        self.repo_dir = os.path.join(self.cfg.log_repo_dir, self.repo_name)
        self.repo_dir2 = os.path.join(self.cfg.log_repo_dir, self.repo_name2)
        self.phy_repo_dir = os.path.join(self.cfg.phy_repo_dir, self.repo_name)
        self.phy_repo_dir2 = os.path.join(self.cfg.phy_repo_dir,
                                          self.repo_name2)
        esr = elastic_class.ElasticSearchRepo(
            self.cfg.host, repo=self.repo_name, repo_dir=self.repo_dir)

        if esr.repo_dict:
            print("ERROR: Test environment not clean - repositories exist.")
            self.skipTest("Pre-conditions not met.")

    def test_dump_list_is_set(self):

        """Function:  test_dump_list_is_set

        Description:  Test if dump list has data in it.

        Arguments:

        """

        esr = elastic_class.ElasticSearchRepo(
            self.cfg.host, repo=self.repo_name, repo_dir=self.repo_dir)
        esr.create_repo()
        esd = elastic_class.ElasticSearchDump(self.cfg.host,
                                              repo=self.repo_name)
        esd.dump_db()
        esd2 = elastic_class.ElasticSearchDump(self.cfg.host,
                                               repo=self.repo_name)

        self.assertTrue(esd2.dump_list)

        esr.delete_repo()

    def test_dump_list_is_empty(self):

        """Function:  test_dump_list_is_empty

        Description:  Test if dump list is empty.

        Arguments:

        """

        esr = elastic_class.ElasticSearchRepo(
            self.cfg.host, repo=self.repo_name, repo_dir=self.repo_dir)
        esr.create_repo()
        esd = elastic_class.ElasticSearchDump(self.cfg.host)

        self.assertTrue(not esd.dump_list)

        esr.delete_repo()

    def test_repo_is_set(self):

        """Function:  test_repo_is_set

        Description:  Test if dump location is set.

        Arguments:

        """

        esr = elastic_class.ElasticSearchRepo(
            self.cfg.host, repo=self.repo_name, repo_dir=self.repo_dir)
        esr.create_repo()
        esd = elastic_class.ElasticSearchDump(self.cfg.host)

        self.assertTrue(esd.dump_loc == self.repo_dir)

        esr.delete_repo()

    def test_repo_not_set(self):

        """Function:  test_repo_not_set

        Description:  Test if repo name is not set and type is not set.

        Arguments:

        """

        esd = elastic_class.ElasticSearchDump(self.cfg.host)

        self.assertTrue(not esd.type)

    def test_multi_repo(self):

        """Function:  test_multi_repo

        Description:  Test if multiple repos are present.

        Arguments:

        """

        esr = elastic_class.ElasticSearchRepo(
            self.cfg.host, repo=self.repo_name, repo_dir=self.repo_dir)
        esr.create_repo()
        esr.create_repo(repo_name=self.repo_name2, repo_dir=self.repo_dir2)
        esd = elastic_class.ElasticSearchDump(self.cfg.host)

        self.assertTrue(esd.repo_name is None)

        esr.delete_repo()
        esr.delete_repo(repo_name=self.repo_name2)

    def test_single_repo(self):

        """Function:  test_single_repo

        Description:  Test if single repo is present.

        Arguments:

        """

        esr = elastic_class.ElasticSearchRepo(
            self.cfg.host, repo=self.repo_name, repo_dir=self.repo_dir)
        esr.create_repo()
        esd = elastic_class.ElasticSearchDump(self.cfg.host)

        self.assertTrue(esd.repo_name == self.repo_name)

        esr.delete_repo()

    def test_repo_not_passed(self):

        """Function:  test_repo_not_passed

        Description:  Test if repo name is not passed to program.

        Arguments:

        """

        esd = elastic_class.ElasticSearchDump(self.cfg.host)

        self.assertTrue(not esd.repo_name and not esd.type)

    def test_repo_not_exist(self):

        """Function:  test_repo_not_exist

        Description:  Test if repo name does not exist.

        Arguments:

        """

        esd = elastic_class.ElasticSearchDump(self.cfg.host,
                                              repo=self.repo_name)

        self.assertTrue(not esd.repo_name and not esd.type)

    def test_connect(self):

        """Function:  test_connect

        Description:  Test to successfully connect to Elasticsearch.

        Arguments:

        """

        esd = elastic_class.ElasticSearchDump(self.cfg.host)

        self.assertTrue(not esd.repo_name and not esd.type)

    def test_init(self):

        """Function:  test_init

        Description:  Test to see if class instance is created.

        Arguments:

        """

        host_list = "Host_Name"

        with gen_libs.no_std_out():
            esd = elastic_class.ElasticSearchDump(host_list)

        self.assertTrue(not esd.dump_name)

    def tearDown(self):

        """Function:  tearDown

        Description:  Clean up of integration testing.

        Arguments:

        """

        if os.path.isdir(self.phy_repo_dir):
            shutil.rmtree(self.phy_repo_dir)

        if os.path.isdir(self.phy_repo_dir2):
            shutil.rmtree(self.phy_repo_dir2)


if __name__ == "__main__":
    unittest.main()
