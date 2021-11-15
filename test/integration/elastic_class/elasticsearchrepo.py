#!/usr/bin/python
# Classification (U)

"""Program:  elasticsearchrepo.py

    Description:  Integration testing of ElasticSearchRepo in elastic_class.py.

    Usage:
        test/integration/elastic_class/elasticsearchrepo.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os

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
        test_ca_cert_passed
        test_no_ca_cert_passed
        test_login_info_passed
        test_japd_only_passed
        test_user_only_passed
        test_login_info_not_passed
        test_repo_is_set
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
        self.repo_dir = os.path.join(self.cfg.log_repo_dir, self.repo_name)

    def test_ca_cert_passed(self):

        """Function:  test_ca_cert_passed

        Description:  Test with ca certificate authority passed.

        Arguments:

        """

        temp_val = self.cfg.ssl_client_ca
        self.cfg.ssl_client_ca = "ca_cert.pem"
        els = elastic_class.ElasticSearchRepo(
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
        els = elastic_class.ElasticSearchRepo(
            self.cfg.host, user=self.cfg.user, japd=self.cfg.japd,
            ca_cert=self.cfg.ssl_client_ca)

        self.assertEqual(els.config, results)

    def test_login_info_passed(self):

        """Function:  test_login_info_passed

        Description:  Test with login information passed.

        Arguments:

        """

        results = {"http_auth": (self.cfg.user, self.cfg.japd)}
        els = elastic_class.ElasticSearchRepo(
            self.cfg.host, user=self.cfg.user, japd=self.cfg.japd)
        self.assertEqual(els.config, results)

    def test_japd_only_passed(self):

        """Function:  test_japd_only_passed

        Description:  Test with only japd argument passed.

        Arguments:

        """

        els = elastic_class.ElasticSearchRepo(
            self.cfg.host, japd=self.cfg.japd)
        self.assertEqual(els.config, {})

    def test_user_only_passed(self):

        """Function:  test_user_only_passed

        Description:  Test with only user argument passed.

        Arguments:

        """

        els = elastic_class.ElasticSearchRepo(
            self.cfg.host, user=self.cfg.user)
        self.assertEqual(els.config, {})

    def test_login_info_not_passed(self):

        """Function:  test_login_info_not_passed

        Description:  Test with no login information passed.

        Arguments:

        """

        els = elastic_class.ElasticSearchRepo(self.cfg.host)
        self.assertEqual(els.config, {})

    def test_repo_is_set(self):

        """Function:  test_repo_not_exist

        Description:  Test if repo attributes are set properly.

        Arguments:

        """

        esr = elastic_class.ElasticSearchRepo(
            self.cfg.host, repo=self.repo_name, repo_dir=self.repo_dir)

        self.assertTrue(
            esr.repo == self.repo_name and esr.repo_dir == self.repo_dir)

    def test_init(self):

        """Function:  test_init

        Description:  Test to see if class instance is created.

        Arguments:

        """

        esr = elastic_class.ElasticSearchRepo(self.cfg.host)

        self.assertTrue(not esr.repo)


if __name__ == "__main__":
    unittest.main()
