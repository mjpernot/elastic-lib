# Classification (U)

"""Program:  elasticsearch_init.py

    Description:  Integration testing of initialization of the ElasticSearch
        class in elastic_class.py.

    Usage:
        test/integration/elastic_class/elasticsearch_init.py

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
        test_passed_scheme
        test_default_scheme
        test_ca_cert_passed
        test_no_ca_cert_passed
        test_login_info_passed
        test_japd_only_passed
        test_user_only_passed
        test_login_info_not_passed
        test_host_is_list
        test_init

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.ca_cert = "ca_cert.pem"
        self.scheme = "http"
        self.base_dir = "test/integration/elastic_class"
        self.test_path = os.path.join(os.getcwd(), self.base_dir)
        self.config_path = os.path.join(self.test_path, "config")
        self.cfg = gen_libs.load_module("elastic", self.config_path)

    def test_passed_scheme(self):

        """Function:  test_passed_scheme

        Description:  Test with scheme passed in.

        Arguments:

        """

        temp_val = self.cfg.ssl_client_ca
        self.cfg.ssl_client_ca = self.ca_cert
        els = elastic_class.ElasticSearch(
            self.cfg.host, user=self.cfg.user, japd=self.cfg.japd,
            ca_cert=self.cfg.ssl_client_ca, scheme=self.scheme)
        self.cfg.ssl_client_ca = temp_val

        self.assertEqual(els.config["scheme"], "http")

    def test_default_scheme(self):

        """Function:  test_default_scheme

        Description:  Test with default scheme used.

        Arguments:

        """

        temp_val = self.cfg.ssl_client_ca
        self.cfg.ssl_client_ca = self.ca_cert
        els = elastic_class.ElasticSearch(
            self.cfg.host, user=self.cfg.user, japd=self.cfg.japd,
            ca_cert=self.cfg.ssl_client_ca)
        self.cfg.ssl_client_ca = temp_val

        self.assertEqual(els.config["scheme"], "https")

    def test_ca_cert_passed(self):

        """Function:  test_ca_cert_passed

        Description:  Test with ca certificate authority passed.

        Arguments:

        """

        temp_val = self.cfg.ssl_client_ca
        self.cfg.ssl_client_ca = self.ca_cert
        els = elastic_class.ElasticSearch(
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
        els = elastic_class.ElasticSearch(
            self.cfg.host, user=self.cfg.user, japd=self.cfg.japd,
            ca_cert=self.cfg.ssl_client_ca)

        self.assertEqual(els.config, results)

    def test_login_info_passed(self):

        """Function:  test_login_info_passed

        Description:  Test with login information passed.

        Arguments:

        """

        results = {"http_auth": (self.cfg.user, self.cfg.japd)}
        els = elastic_class.ElasticSearch(
            self.cfg.host, user=self.cfg.user, japd=self.cfg.japd)

        self.assertEqual(els.config, results)

    def test_japd_only_passed(self):

        """Function:  test_japd_only_passed

        Description:  Test with only japd argument passed.

        Arguments:

        """

        els = elastic_class.ElasticSearch(self.cfg.host, japd=self.cfg.japd)

        self.assertEqual(els.config, {})

    def test_user_only_passed(self):

        """Function:  test_user_only_passed

        Description:  Test with only user argument passed.

        Arguments:

        """

        els = elastic_class.ElasticSearch(self.cfg.host, user=self.cfg.user)

        self.assertEqual(els.config, {})

    def test_login_info_not_passed(self):

        """Function:  test_login_info_not_passed

        Description:  Test with no login information passed.

        Arguments:

        """

        els = elastic_class.ElasticSearch(self.cfg.host)

        self.assertEqual(els.config, {})

    def test_host_is_list(self):

        """Function:  test_host_is_list

        Description:  Test to see if host is a list.

        Arguments:

        """

        els = elastic_class.ElasticSearch(
            self.cfg.host, user=self.cfg.user, japd=self.cfg.japd)

        self.assertTrue(els.hosts == self.cfg.host)

    def test_init(self):

        """Function:  test_init

        Description:  Test to see if class instance is created.

        Arguments:

        """

        host_list = ["Host_Name"]

        with gen_libs.no_std_out():
            els = elastic_class.ElasticSearch(host_list)

        self.assertTrue(els.hosts == host_list)


if __name__ == "__main__":
    unittest.main()
