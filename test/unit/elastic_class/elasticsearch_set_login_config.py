# Classification (U)

"""Program:  elasticsearch_set_login_config.py

    Description:  Unit testing of set_login_config in
        elastic_class.ElasticSearch class.

    Usage:
        test/unit/elastic_class/elasticsearch_set_login_config.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import unittest
import elasticsearch

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
        test_login_info_passed
        test_japd_only_passed
        test_user_only_passed
        test_login_info_not_passed

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.host_list = ["host1", "host2"]
        self.user = 'user'
        self.japd = 'japd'
        self.results = {}
        self.results2 = {"http_auth": (self.user, self.japd)}
        self.results3 = {"basic_auth": (self.user, self.japd)}

    def test_login_info_passed(self):

        """Function:  test_login_info_passed

        Description:  Test with login information passed.

        Arguments:

        """

        els = elastic_class.ElasticSearch(
            self.host_list, user=self.user, japd=self.japd)

        if elasticsearch.__version__ >= (8, 0, 0):
            results = self.results3

        else:
            results = self.results2

        self.assertEqual(els.config, results)

    def test_japd_only_passed(self):

        """Function:  test_japd_only_passed

        Description:  Test with only japd argument passed.

        Arguments:

        """

        els = elastic_class.ElasticSearch(self.host_list, japd=self.japd)
        self.assertEqual(els.config, self.results)

    def test_user_only_passed(self):

        """Function:  test_user_only_passed

        Description:  Test with only user argument passed.

        Arguments:

        """

        els = elastic_class.ElasticSearch(self.host_list, user=self.user)
        self.assertEqual(els.config, self.results)

    def test_login_info_not_passed(self):

        """Function:  test_login_info_not_passed

        Description:  Test with no login information passed.

        Arguments:

        """

        els = elastic_class.ElasticSearch(self.host_list)
        self.assertEqual(els.config, self.results)


if __name__ == "__main__":
    unittest.main()
