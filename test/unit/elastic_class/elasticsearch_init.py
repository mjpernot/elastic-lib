#!/usr/bin/python
# Classification (U)

"""Program:  elasticsearch_init.py

    Description:  Unit testing of __init__ in elastic_class.ElasticSearch.

    Usage:
        test/unit/elastic_class/elasticsearch_init.py

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
import elastic_class
import version

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_login_info_passed2
        test_japd_only_passed2
        test_user_only_passed2
        test_login_info_not_passed2
        test_login_info_passed
        test_login_info_not_passed
        test_port_change
        test_host_list

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

    def test_login_info_passed2(self):

        """Function:  test_login_info_passed2

        Description:  Test with login information passed.

        Arguments:

        """

        els = elastic_class.ElasticSearch(
            self.host_list, user=self.user, japd=self.japd)
        self.assertEqual(els.config, self.results2)

    def test_japd_only_passed2(self):

        """Function:  test_japd_only_passed2

        Description:  Test with only japd argument passed.

        Arguments:

        """

        els = elastic_class.ElasticSearch(self.host_list, japd=self.japd)
        self.assertEqual(els.config, self.results)

    def test_user_only_passed2(self):

        """Function:  test_user_only_passed2

        Description:  Test with only user argument passed.

        Arguments:

        """

        els = elastic_class.ElasticSearch(self.host_list, user=self.user)
        self.assertEqual(els.config, self.results)

    def test_login_info_not_passed2(self):

        """Function:  test_login_info_not_passed2

        Description:  Test with no login information passed.

        Arguments:

        """

        els = elastic_class.ElasticSearch(self.host_list)
        self.assertEqual(els.config, self.results)

    def test_login_info_passed(self):

        """Function:  test_login_info_passed

        Description:  Test with login information passed.

        Arguments:

        """

        els = elastic_class.ElasticSearch(
            self.host_list, user=self.user, japd=self.japd)
        self.assertEqual((els.user, els.japd), (self.user, self.japd))

    def test_login_info_not_passed(self):

        """Function:  test_login_info_not_passed

        Description:  Test with no login information passed.

        Arguments:

        """

        els = elastic_class.ElasticSearch(self.host_list)
        self.assertEqual((els.user, els.japd), (None, None))

    def test_port_change(self):

        """Function:  test_port_change

        Description:  Test with change to port.

        Arguments:

        """

        els = elastic_class.ElasticSearch(self.host_list, port=9201)
        self.assertEqual((els.port, els.hosts), (9201, self.host_list))

    def test_host_list(self):

        """Function:  test_host_list

        Description:  Test host_list is a list.

        Arguments:

        """

        els = elastic_class.ElasticSearch(self.host_list)
        self.assertEqual((els.port, els.hosts), (9200, self.host_list))


if __name__ == "__main__":
    unittest.main()
