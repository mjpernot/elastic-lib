#!/usr/bin/python
# Classification (U)

"""Program:  elasticsearchdump_dumpdb.py

    Description:  Integration testing of ElasticSearchDump.dump_db method
        in elastic_class.py.

    Usage:
        test/integration/elastic_class/elasticsearchdump_dumpdb.py

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
        test_dbs_multi_names
        test_dbs_is_successful
        test_dbs_is_not_str
        test_dump_list_updated
        test_dump_succesful
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
        self.repo_name = "TEST_INTR_REPO"
        self.repo_dir = os.path.join(self.cfg.log_repo_dir, self.repo_name)
        self.phy_repo_dir = os.path.join(self.cfg.phy_repo_dir, self.repo_name)
        self.msg = "ERROR:  Repository name not set."
        self.dbs_err = ["test_dump_error"]
        self.msg2 = \
            "ERROR:  Database name(s) is not a string: ['test_dump_error']"

    def test_dbs_multi_names(self):

        """Function:  test_dbs_multi_names

        Description:  Test dumping two databases.

        Note:  In Elasticsearch v7.4.0, one dump was equal to one dump
            directory.  However, in Elasticsearch v7.12.0. one dump has
            multiple dump directories.

        Arguments:

        """

        esr = elastic_class.ElasticSearchRepo(
            self.cfg.host, repo=self.repo_name, repo_dir=self.repo_dir,
            user=self.cfg.user, japd=self.cfg.japd)
        esr.connect()
        esr.create_repo()

        esd = elastic_class.ElasticSearchDump(
            self.cfg.host, repo=self.repo_name, user=self.cfg.user,
            japd=self.cfg.japd)
        esd.connect()

        # Capture 2 databases/indices name in Elasticsearch.
        dbs = ','.join(
            [str(y[2]) for y in [
                x.split() for x in esd.els.cat.indices().splitlines()]][0:2])

        err_flag, _ = esd.dump_db(dbs)
        dir_path = os.path.join(self.phy_repo_dir, "indices")

        # Count number of databases/indices dumped to repository.
        cnt = len([name for name in os.listdir(dir_path)
                   if os.path.isdir(os.path.join(dir_path, name))])

        esr.delete_repo()

        self.assertFalse(err_flag)
        self.assertTrue(cnt > 1)

    def test_dbs_is_successful(self):

        """Function:  test_dbs_is_successful

        Description:  Test dumping single database.

        Note:  In Elasticsearch v7.4.0, one dump was equal to one dump
            directory.  However, in Elasticsearch v7.12.0. one dump has
            multiple dump directories.

        Arguments:

        """

        esr = elastic_class.ElasticSearchRepo(
            self.cfg.host, repo=self.repo_name, repo_dir=self.repo_dir,
            user=self.cfg.user, japd=self.cfg.japd)
        esr.connect()
        esr.create_repo()

        esd = elastic_class.ElasticSearchDump(
            self.cfg.host, repo=self.repo_name, user=self.cfg.user,
            japd=self.cfg.japd)
        esd.connect()

        # Capture the first database/indice name in Elasticsearch.
        dbs = str([name.split()
                   for name in esd.els.cat.indices().splitlines()][0][2])

        err_flag, _ = esd.dump_db(dbs)
        dir_path = os.path.join(self.phy_repo_dir, "indices")

        # Count number of databases/indices dumped to repository.
        cnt = len([name for name in os.listdir(dir_path)
                   if os.path.isdir(os.path.join(dir_path, name))])

        esr.delete_repo()

        self.assertFalse(err_flag)
        self.assertTrue(cnt > 0)

    def test_dbs_is_not_str(self):

        """Function:  test_dbs_is_not_str

        Description:  Test database name is not a string.

        Arguments:

        """

        esr = elastic_class.ElasticSearchRepo(
            self.cfg.host, repo=self.repo_name, repo_dir=self.repo_dir,
            user=self.cfg.user, japd=self.cfg.japd)
        esr.connect()
        esr.create_repo()

        esd = elastic_class.ElasticSearchDump(
            self.cfg.host, repo=self.repo_name, user=self.cfg.user,
            japd=self.cfg.japd)
        esd.connect()
        err_flag, status_msg = esd.dump_db(self.dbs_err)

        self.assertEqual((err_flag, status_msg), (True, self.msg2))

    def test_dump_list_updated(self):

        """Function:  test_dump_list_updated

        Description:  Test dump list is updated after dump.

        Arguments:

        """

        esr = elastic_class.ElasticSearchRepo(
            self.cfg.host, repo=self.repo_name, repo_dir=self.repo_dir,
            user=self.cfg.user, japd=self.cfg.japd)
        esr.connect()
        esr.create_repo()

        esd = elastic_class.ElasticSearchDump(
            self.cfg.host, repo=self.repo_name, user=self.cfg.user,
            japd=self.cfg.japd)
        esd.connect()
        err_flag, _ = esd.dump_db()

        esr.delete_repo()

        self.assertFalse(err_flag)
        self.assertEqual(len(esd.dump_list), 1)

    def test_dump_succesful(self):

        """Function:  test_dump_succesful

        Description:  Test dump of database is successful.

        Arguments:

        """

        esr = elastic_class.ElasticSearchRepo(
            self.cfg.host, repo=self.repo_name, repo_dir=self.repo_dir,
            user=self.cfg.user, japd=self.cfg.japd)
        esr.connect()
        esr.create_repo()

        esd = elastic_class.ElasticSearchDump(
            self.cfg.host, repo=self.repo_name, user=self.cfg.user,
            japd=self.cfg.japd)
        esd.connect()

        err_flag, status_msg = esd.dump_db()

        esr.delete_repo()

        self.assertEqual((err_flag, status_msg), (False, None))

    def test_repo_name_is_set(self):

        """Function:  test_repo_name_is_set

        Description:  Test repo name is set, but not present.

        Arguments:

        """

        esd = elastic_class.ElasticSearchDump(
            self.cfg.host, repo=self.repo_name, user=self.cfg.user,
            japd=self.cfg.japd)
        esd.connect()

        err_flag, status_msg = esd.dump_db()

        self.assertEqual((err_flag, status_msg), (True, self.msg))

    def test_repo_name_not_set(self):

        """Function:  test_repo_name_not_set

        Description:  Test repo name is not set for dump.

        Arguments:

        """

        esd = elastic_class.ElasticSearchDump(
            self.cfg.host, user=self.cfg.user, japd=self.cfg.japd)
        esd.connect()

        err_flag, status_msg = esd.dump_db()

        self.assertEqual((err_flag, status_msg), (True, self.msg))

    def tearDown(self):

        """Function:  tearDown

        Description:  Clean up of integration testing.

        Arguments:

        """

        if os.path.isdir(self.phy_repo_dir):
            shutil.rmtree(self.phy_repo_dir)


if __name__ == "__main__":
    unittest.main()
