# Classification (U)

"""Program:  elasticsearch_set_ssl_config.py

    Description:  Unit testing of set_ssl_config in
        elastic_class.ElasticSearch class.

    Usage:
        test/unit/elastic_class/elasticsearch_set_ssl_config.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import unittest

# Local
sys.path.append(os.getcwd())
import elastic_class                            # pylint:disable=E0401,C0413
import version                                  # pylint:disable=E0401,C0413

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_ca_cert_not_passed

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.host_list = ["host1", "host2"]
        self.ca_cert = "ca.crt"
        self.results = {}
        self.results2 = {"use_ssl": True, "ca_certs": self.ca_cert,
                         "scheme": "https"}

    def test_ca_cert_passed(self):

        """Function:  test_ca_cert_passed

        Description:  Test with ca_cert passed.

        Arguments:

        """

        els = elastic_class.ElasticSearch(
            self.host_list, ca_cert=self.ca_cert)
        self.assertEqual(els.config, self.results2)

    def test_ca_cert_not_passed(self):

        """Function:  test_ca_cert_not_passed

        Description:  Test with no ca_cert passed.

        Arguments:

        """

        els = elastic_class.ElasticSearch(self.host_list)
        self.assertEqual(els.config, self.results)


if __name__ == "__main__":
    unittest.main()
