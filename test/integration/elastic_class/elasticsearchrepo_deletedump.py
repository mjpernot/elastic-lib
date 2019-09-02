#!/usr/bin/python
# Classification (U)

"""Program:  elasticsearchrepo_deletedump.py

    Description:  Integration testing of ElasticSearchRepo.delete_dump
        method in elastic_class.py.

    Usage:
        test/integration/elastic_class/elasticsearchrepo_deletedump.py

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
import mock

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
        setUp -> Unit testing initilization.
        test_dump_is_deleted -> Test to see if dump is deleted.
        test_dump_not_found -> Test to see if dump is not found.
        test_repo_not_found -> Test to see if repository is not found.
        test_repo_name_is_passed -> Test to see if repo name is passed.
        test_repo_name_is_set -> Test to see if repo name is set.
        test_repo_name_not_set -> Test to see if repo name is not set.
        tearDown -> Clean up of integration testing.

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
        self.repo_dir = os.path.join(self.cfg.base_repo_dir, self.repo_name)

        ER = elastic_class.ElasticSearchRepo(self.cfg.host,
                                             repo=self.repo_name)

        if ER.repo_dict:
            print("ERROR: Test environment not clean - repositories exist.")
            self.skipTest("Pre-conditions not met.")

    def test_dump_is_deleted(self):

        """Function:  test_dump_is_deleted

        Description:  Test to see if dump is deleted.

        Arguments:

        """

        ER = elastic_class.ElasticSearchRepo(self.cfg.host,
                                             repo=self.repo_name,
                                             repo_dir=self.repo_dir)
        ER.create_repo()

        ES = elastic_class.ElasticSearchDump(self.cfg.host,
                                             repo=self.repo_name)
        ES.dump_name = self.dump_name
        ES.dump_db()

        status, msg = ER.delete_dump(dump_name=self.dump_name)

        ER.delete_repo()

        self.assertEqual((status, msg), (False, None))

    def test_dump_not_found(self):

        """Function:  test_dump_not_found

        Description:  Test to see if dump is not found.

        Arguments:

        """

        ER = elastic_class.ElasticSearchRepo(self.cfg.host,
                                             repo=self.repo_name,
                                             repo_dir=self.repo_dir)

        ER.create_repo()

        status, msg = ER.delete_dump(dump_name=self.dump_name)

        ER.delete_repo()

        self.assertEqual(
            (status, msg),
            (True, "ERROR: Dump: test_dump not in Repository: TEST_REPO"))

    def test_repo_not_found(self):

        """Function:  test_repo_not_found

        Description:  Test to see if repository is not found.

        Arguments:

        """

        ER = elastic_class.ElasticSearchRepo(self.cfg.host,
                                             repo=self.repo_name)

        status, msg = ER.delete_dump(dump_name=self.dump_name)

        self.assertEqual(
            (status, msg),
            (True,
             "ERROR: Missing arg/repo not exist, Repo: %s, Dump: %s" %
             (self.repo_name, self.dump_name)))

    def test_repo_name_is_passed(self):

        """Function:  test_repo_name_is_passed

        Description:  Test to see if repo name is passed.

        Arguments:

        """

        ER = elastic_class.ElasticSearchRepo(self.cfg.host)

        status, msg = ER.delete_dump(repo_name=self.repo_name)

        self.assertEqual(
            (status, msg),
            (True,
             "ERROR: Missing arg/repo not exist, Repo: TEST_REPO, Dump: None"))

    def test_repo_name_is_set(self):

        """Function:  test_repo_name_is_set

        Description:  Test to see if repo name is set.

        Arguments:

        """

        ER = elastic_class.ElasticSearchRepo(self.cfg.host,
                                             repo=self.repo_name)

        status, msg = ER.delete_dump()

        self.assertEqual(
            (status, msg),
            (True,
             "ERROR: Missing arg/repo not exist, Repo: TEST_REPO, Dump: None"))

    def test_repo_name_not_set(self):

        """Function:  test_repo_name_not_set

        Description:  Test to see if repo name is not set.

        Arguments:

        """

        ER = elastic_class.ElasticSearchRepo(self.cfg.host)

        status, msg = ER.delete_dump()

        self.assertEqual(
            (status, msg),
            (True,
             "ERROR: Missing arg/repo not exist, Repo: None, Dump: None"))

    def tearDown(self):

        """Function:  tearDown

        Description:  Clean up of integration testing.

        Arguments:

        """

        if os.path.isdir(self.repo_dir):
            shutil.rmtree(self.repo_dir)


if __name__ == "__main__":
    unittest.main()
