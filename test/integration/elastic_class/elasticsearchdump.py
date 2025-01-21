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
        test_ca_cert_passed
        test_no_ca_cert_passed
        test_login_info_passed
        test_japd_only_passed
        test_user_only_passed
        test_login_info_not_passed
        test_dump_list_is_empty
        test_repo_not_set
        test_repo_not_passed
        test_repo_not_exist
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

    def test_ca_cert_passed(self):

        """Function:  test_ca_cert_passed

        Description:  Test with ca certificate authority passed.

        Arguments:

        """

        temp_val = self.cfg.ssl_client_ca
        self.cfg.ssl_client_ca = "ca_cert.pem"
        els = elastic_class.ElasticSearchDump(
            self.cfg.host, user=self.cfg.user, japd=self.cfg.japd,
            ca_cert=self.cfg.ssl_client_ca)
        self.cfg.ssl_client_ca = temp_val

        self.assertEqual(els.config["use_ssl"], True)

    def test_no_ca_cert_passed(self):

        """Function:  test_no_ca_cert_passed

        Description:  Test with no ca certificate authority passed.

        Arguments:

        """

        results = {"http_auth": (self.cfg.user, self.cfg.japd)}
        els = elastic_class.ElasticSearchDump(
            self.cfg.host, user=self.cfg.user, japd=self.cfg.japd,
            ca_cert=self.cfg.ssl_client_ca)

        self.assertEqual(els.config, results)

    def test_login_info_passed(self):

        """Function:  test_login_info_passed

        Description:  Test with login information passed.

        Arguments:

        """

        results = {"http_auth": (self.cfg.user, self.cfg.japd)}
        els = elastic_class.ElasticSearchDump(
            self.cfg.host, user=self.cfg.user, japd=self.cfg.japd)
        self.assertEqual(els.config, results)

    def test_japd_only_passed(self):

        """Function:  test_japd_only_passed

        Description:  Test with only japd argument passed.

        Arguments:

        """

        els = elastic_class.ElasticSearchDump(
            self.cfg.host, japd=self.cfg.japd)
        self.assertEqual(els.config, {})

    def test_user_only_passed(self):

        """Function:  test_user_only_passed

        Description:  Test with only user argument passed.

        Arguments:

        """

        els = elastic_class.ElasticSearchDump(
            self.cfg.host, user=self.cfg.user)
        self.assertEqual(els.config, {})

    def test_login_info_not_passed(self):

        """Function:  test_login_info_not_passed

        Description:  Test with no login information passed.

        Arguments:

        """

        els = elastic_class.ElasticSearchDump(self.cfg.host)
        self.assertEqual(els.config, {})

    def test_dump_list_is_empty(self):

        """Function:  test_dump_list_is_empty

        Description:  Test if dump list is empty.

        Arguments:

        """

        esd = elastic_class.ElasticSearchDump(self.cfg.host)

        self.assertTrue(not esd.dump_list)

    def test_repo_not_set(self):

        """Function:  test_repo_not_set

        Description:  Test if repo name is not set and type is not set.

        Arguments:

        """

        esd = elastic_class.ElasticSearchDump(self.cfg.host)

        self.assertTrue(not esd.type)

    def test_repo_not_passed(self):

        """Function:  test_repo_not_passed

        Description:  Test if repo name is not passed to program.

        Arguments:

        """

        esd = elastic_class.ElasticSearchDump(self.cfg.host)

        self.assertTrue(not esd.repo_name and not esd.type)

    def test_repo_passed(self):

        """Function:  test_repo_passed

        Description:  Test if repo name is passed.

        Arguments:

        """

        esd = elastic_class.ElasticSearchDump(
            self.cfg.host, repo=self.repo_name)

        self.assertEqual(esd.repo_name, self.repo_name)

    def test_init(self):

        """Function:  test_init

        Description:  Test to see if class instance is created.

        Arguments:

        """

        esd = elastic_class.ElasticSearchDump(self.cfg.host)

        self.assertTrue(not esd.dump_name)


if __name__ == "__main__":
    unittest.main()
