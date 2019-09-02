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
        test_dbs_multi_names -> Test dumping two databases.
        test_dbs_is_successful -> Test dumping single database.
        test_dbs_is_not_str -> Test database name is not a string.
        test_dump_list_updated -> Test dump list is updated after dump.
        test_dump_succesful -> Test dump of database is successful.
        test_repo_name_is_set -> Test repo name is set, but not present.
        test_repo_name_not_set -> Test repo name is not set for dump.
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
        self.repo_dir = os.path.join(self.cfg.base_repo_dir, self.repo_name)
        self.msg = "ERROR:  Repository name not set."
        self.dbs_err = ["test_dump_error"]
        self.msg2 = \
            "ERROR:  Database name(s) is not a string: ['test_dump_error']"

    def test_dbs_multi_names(self):

        """Function:  test_dbs_multi_names

        Description:  Test dumping two databases.

        Arguments:

        """

        ER = elastic_class.ElasticSearchRepo(self.cfg.host,
                                             repo=self.repo_name,
                                             repo_dir=self.repo_dir)
        ER.create_repo()

        ES = elastic_class.ElasticSearchDump(self.cfg.host,
                                             repo=self.repo_name)

        # Capture 2 databases/indices name in Elasticsearch.
        dbs = ','.join([str(y[2])
                        for y in [x.split()
                        for x in ES.es.cat.indices().splitlines()]][0:2])

        err_flag, status_msg = ES.dump_db(dbs)

        dir_path = os.path.join(self.repo_dir, "indices")

        # Count number of databases/indices dumped to repository.
        cnt = len([name for name in os.listdir(dir_path)
                   if os.path.isdir(os.path.join(dir_path, name))])

        ER.delete_repo()

        self.assertEqual(cnt, 2)

    def test_dbs_is_successful(self):

        """Function:  test_dump_succesful

        Description:  Test dumping single database.

        Arguments:

        """

        ER = elastic_class.ElasticSearchRepo(self.cfg.host,
                                             repo=self.repo_name,
                                             repo_dir=self.repo_dir)
        ER.create_repo()

        ES = elastic_class.ElasticSearchDump(self.cfg.host,
                                             repo=self.repo_name)

        # Capture the first database/indice name in Elasticsearch.
        dbs = str([x.split() for x in ES.es.cat.indices().splitlines()][0][2])

        err_flag, status_msg = ES.dump_db(dbs)

        dir_path = os.path.join(self.repo_dir, "indices")

        # Count number of databases/indices dumped to repository.
        cnt = len([name for name in os.listdir(dir_path)
                   if os.path.isdir(os.path.join(dir_path, name))])

        ER.delete_repo()

        self.assertEqual(cnt, 1)

    def test_dbs_is_not_str(self):

        """Function:  test_dbs_is_not_str

        Description:  Test database name is not a string.

        Arguments:

        """

        ER = elastic_class.ElasticSearchRepo(self.cfg.host,
                                             repo=self.repo_name,
                                             repo_dir=self.repo_dir)

        ER.create_repo()

        ES = elastic_class.ElasticSearchDump(self.cfg.host,
                                             repo=self.repo_name)

        err_flag, status_msg = ES.dump_db(self.dbs_err)

        self.assertEqual((err_flag, status_msg), (True, self.msg2))

    def test_dump_list_updated(self):

        """Function:  test_dump_list_updated

        Description:  Test dump list is updated after dump.

        Arguments:

        """

        ER = elastic_class.ElasticSearchRepo(self.cfg.host,
                                             repo=self.repo_name,
                                             repo_dir=self.repo_dir)

        ER.create_repo()

        ES = elastic_class.ElasticSearchDump(self.cfg.host,
                                             repo=self.repo_name)

        err_flag, status_msg = ES.dump_db()

        ER.delete_repo()

        self.assertEqual(len(ES.dump_list), 1)

    def test_dump_succesful(self):

        """Function:  test_dump_succesful

        Description:  Test dump of database is successful.

        Arguments:

        """

        ER = elastic_class.ElasticSearchRepo(self.cfg.host,
                                             repo=self.repo_name,
                                             repo_dir=self.repo_dir)

        ER.create_repo()

        ES = elastic_class.ElasticSearchDump(self.cfg.host,
                                             repo=self.repo_name)

        err_flag, status_msg = ES.dump_db()

        ER.delete_repo()

        self.assertEqual((err_flag, status_msg), (False, None))

    def test_repo_name_is_set(self):

        """Function:  test_repo_name_is_set

        Description:  Test repo name is set, but not present.

        Arguments:

        """

        ES = elastic_class.ElasticSearchDump(self.cfg.host,
                                             repo=self.repo_name)

        err_flag, status_msg = ES.dump_db()

        self.assertEqual((err_flag, status_msg), (True, self.msg))

    def test_repo_name_not_set(self):

        """Function:  test_repo_name_not_set

        Description:  Test repo name is not set for dump.

        Arguments:

        """

        ES = elastic_class.ElasticSearchDump(self.cfg.host)

        err_flag, status_msg = ES.dump_db()

        self.assertEqual((err_flag, status_msg), (True, self.msg))

    def tearDown(self):

        """Function:  tearDown

        Description:  Clean up of integration testing.

        Arguments:

        """

        if os.path.isdir(self.repo_dir):
            shutil.rmtree(self.repo_dir)


if __name__ == "__main__":
    unittest.main()
