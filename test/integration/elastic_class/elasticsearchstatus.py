# Classification (U)

"""Program:  elasticsearchstatus.py

    Description:  Integration testing of ElasticSearchStatus class in
        elastic_class.py.

    Usage:
        test/integration/elastic_class/elasticsearchstatus.py

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
        test_cutoff_mem_set
        test_cutoff_mem_default
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
        els = elastic_class.ElasticSearchStatus(
            self.cfg.host, user=self.cfg.user, japd=self.cfg.japd,
            ca_cert=self.cfg.ssl_client_ca)
        self.cfg.ssl_client_ca = temp_val

        self.assertTrue(els.config["use_ssl"])

    def test_no_ca_cert_passed(self):

        """Function:  test_no_ca_cert_passed

        Description:  Test with no ca certificate authority passed.

        Arguments:

        """

        results = {"http_auth": (self.cfg.user, self.cfg.japd)}
        els = elastic_class.ElasticSearchStatus(
            self.cfg.host, user=self.cfg.user, japd=self.cfg.japd,
            ca_cert=self.cfg.ssl_client_ca)

        self.assertEqual(els.config, results)

    def test_login_info_passed(self):

        """Function:  test_login_info_passed

        Description:  Test with login information passed.

        Arguments:

        """

        results = {"http_auth": (self.cfg.user, self.cfg.japd)}
        ess = elastic_class.ElasticSearchStatus(
            self.cfg.host, user=self.cfg.user, japd=self.cfg.japd)
        self.assertEqual(ess.config, results)

    def test_japd_only_passed(self):

        """Function:  test_japd_only_passed

        Description:  Test with only japd argument passed.

        Arguments:

        """

        ess = elastic_class.ElasticSearchStatus(
            self.cfg.host, japd=self.cfg.japd)
        self.assertEqual(ess.config, {})

    def test_user_only_passed(self):

        """Function:  test_user_only_passed

        Description:  Test with only user argument passed.

        Arguments:

        """

        ess = elastic_class.ElasticSearchStatus(
            self.cfg.host, user=self.cfg.user)
        self.assertEqual(ess.config, {})

    def test_login_info_not_passed(self):

        """Function:  test_login_info_not_passed

        Description:  Test with no login information passed.

        Arguments:

        """

        ess = elastic_class.ElasticSearchStatus(self.cfg.host)
        self.assertEqual(ess.config, {})

    def test_cutoff_mem_set(self):

        """Function:  test_cutoff_mem_set

        Description:  Test with cutoff_mem set to value.

        Arguments:

        """

        ess = elastic_class.ElasticSearchStatus(
            self.cfg.host, repo=self.repo_name, repo_dir=self.repo_dir,
            cutoff_mem=95)

        self.assertEqual(ess.cutoff_mem, 95)

    def test_cutoff_mem_default(self):

        """Function:  test_cutoff_mem_default

        Description:  Test with cutoff_mem set to default.

        Arguments:

        """

        ess = elastic_class.ElasticSearchStatus(
            self.cfg.host, repo=self.repo_name, repo_dir=self.repo_dir)

        self.assertEqual(ess.cutoff_mem, 90)

    def test_init(self):

        """Function:  test_init

        Description:  Test to see if class instance is created.

        Arguments:

        """

        ess = elastic_class.ElasticSearchStatus(self.cfg.host)

        self.assertFalse(ess.unassigned_shards)


if __name__ == "__main__":
    unittest.main()
