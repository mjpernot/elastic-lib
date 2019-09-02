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
        test_dump_list_is_set -> Test if dump list has data in it.
        test_dump_list_is_empty -> Test if dump list is empty.
        test_repo_is_set -> Test if dump location is set.
        test_repo_not_set -> Test if repo name is not set and type is not set.
        test_multi_repo -> Test if multiple repos are present.
        test_single_repo -> Test if single repo is present.
        test_repo_not_passed -> Test if repo name is not passed to program.
        test_repo_not_exist -> Test if repo name does not exist.
        test_connect -> Test to successfully connect to Elasticsearch.
        test_init -> Test to see if class instance is created.
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
        self.repo_name = "TEST_INTR_REPO"
        self.repo_name2 = "TEST_INTR_REPO2"
        self.repo_dir = os.path.join(self.cfg.base_repo_dir, self.repo_name)
        self.repo_dir2 = os.path.join(self.cfg.base_repo_dir, self.repo_name2)

        ER = elastic_class.ElasticSearchRepo(self.cfg.host,
                                             repo=self.repo_name,
                                             repo_dir=self.repo_dir)

        if ER.repo_dict:
            print("ERROR: Test environment not clean - repositories exist.")
            self.skipTest("Pre-conditions not met.")

    def test_dump_list_is_set(self):

        """Function:  test_dump_list_is_set

        Description:  Test if dump list has data in it.

        Arguments:

        """

        ER = elastic_class.ElasticSearchRepo(self.cfg.host,
                                             repo=self.repo_name,
                                             repo_dir=self.repo_dir)

        ER.create_repo()

        ES = elastic_class.ElasticSearchDump(self.cfg.host,
                                             repo=self.repo_name)
        ES.dump_db()

        ES2 = elastic_class.ElasticSearchDump(self.cfg.host,
                                              repo=self.repo_name)

        if ES2.dump_list:
            status = True

        else:
            status = False

        ER.delete_repo()

        self.assertTrue(status)

    def test_dump_list_is_empty(self):

        """Function:  test_dump_list_is_empty

        Description:  Test if dump list is empty.

        Arguments:

        """

        ER = elastic_class.ElasticSearchRepo(self.cfg.host,
                                             repo=self.repo_name,
                                             repo_dir=self.repo_dir)

        ER.create_repo()

        ES = elastic_class.ElasticSearchDump(self.cfg.host)

        if not ES.dump_list:
            status = True

        else:
            status = False

        ER.delete_repo()

        self.assertTrue(status)

    def test_repo_is_set(self):

        """Function:  test_repo_is_set

        Description:  Test if dump location is set.

        Arguments:

        """

        ER = elastic_class.ElasticSearchRepo(self.cfg.host,
                                             repo=self.repo_name,
                                             repo_dir=self.repo_dir)

        ER.create_repo()

        ES = elastic_class.ElasticSearchDump(self.cfg.host)

        if ES.dump_loc == self.repo_dir:
            status = True

        else:
            status = False

        ER.delete_repo()

        self.assertTrue(status)

    def test_repo_not_set(self):

        """Function:  test_repo_not_set

        Description:  Test if repo name is not set and type is not set.

        Arguments:

        """

        ES = elastic_class.ElasticSearchDump(self.cfg.host)

        if not ES.type:
            status = True

        else:
            status = False

        self.assertTrue(status)

    def test_multi_repo(self):

        """Function:  test_multi_repo

        Description:  Test if multiple repos are present.

        Arguments:

        """

        ER = elastic_class.ElasticSearchRepo(self.cfg.host,
                                             repo=self.repo_name,
                                             repo_dir=self.repo_dir)

        ER.create_repo()
        ER.create_repo(repo_name=self.repo_name2, repo_dir=self.repo_dir2)

        ES = elastic_class.ElasticSearchDump(self.cfg.host)

        if ES.repo_name is None:
            status = True

        else:
            status = False

        ER.delete_repo()
        ER.delete_repo(repo_name=self.repo_name2)

        self.assertTrue(status)

    def test_single_repo(self):

        """Function:  test_single_repo

        Description:  Test if single repo is present.

        Arguments:

        """

        ER = elastic_class.ElasticSearchRepo(self.cfg.host,
                                             repo=self.repo_name,
                                             repo_dir=self.repo_dir)

        ER.create_repo()

        ES = elastic_class.ElasticSearchDump(self.cfg.host)

        if ES.repo_name == self.repo_name:
            status = True

        else:
            status = False

        ER.delete_repo()

        self.assertTrue(status)

    def test_repo_not_passed(self):

        """Function:  test_repo_not_passed

        Description:  Test if repo name is not passed to program.

        Arguments:

        """

        ES = elastic_class.ElasticSearchDump(self.cfg.host)

        if not ES.repo_name and not ES.type:
            status = True

        else:
            status = False

        self.assertTrue(status)

    def test_repo_not_exist(self):

        """Function:  test_repo_not_exist

        Description:  Test if repo name does not exist.

        Arguments:

        """

        ES = elastic_class.ElasticSearchDump(self.cfg.host,
                                             repo=self.repo_name)

        if not ES.repo_name and not ES.type:
            status = True

        else:
            status = False

        self.assertTrue(status)

    def test_connect(self):

        """Function:  test_connect

        Description:  Test to successfully connect to Elasticsearch.

        Arguments:

        """

        ES = elastic_class.ElasticSearchDump(self.cfg.host)

        if not ES.repo_name and not ES.type:
            status = True

        else:
            status = False

        self.assertTrue(status)

    def test_init(self):

        """Function:  test_init

        Description:  Test to see if class instance is created.

        Arguments:

        """

        host_list = "Host_Name"

        with gen_libs.no_std_out():
            ES = elastic_class.ElasticSearchDump(host_list)

        if not ES.dump_name:
            status = True

        else:
            status = False

        self.assertTrue(status)

    def tearDown(self):

        """Function:  tearDown

        Description:  Clean up of integration testing.

        Arguments:

        """

        if os.path.isdir(self.repo_dir):
            shutil.rmtree(self.repo_dir)

        if os.path.isdir(self.repo_dir2):
            shutil.rmtree(self.repo_dir2)


if __name__ == "__main__":
    unittest.main()
