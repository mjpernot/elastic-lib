#!/usr/bin/python
# Classification (U)

"""Program:  elastic_search.py

    Description:  Integration testing of ElasticSearch in elastic_class.py.

    Usage:
        test/integration/elastic_class/elastic_search.py

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
        setUp -> Unit testing initilization.
        test_ping_failure -> Test if ping is a failure.
        test_ping_success -> Test to if ping is successful.
        test_host_is_list -> Test to see if host is a list.
        test_init -> Test to see if class instance is created.

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

    def test_ping_failure(self):

        """Function:  test_ping_failure

        Description:  Test if ping is a failure.

        Arguments:

        """

        with gen_libs.no_std_out():
            els = elastic_class.ElasticSearch(self.cfg.host, port=9201)

        print("Ignore above message, part of the test.")

        if not els.els:
            status = True

        else:
            status = False

        self.assertTrue(status)

    def test_ping_success(self):

        """Function:  test_ping_success

        Description:  Test to if ping is successful.

        Arguments:

        """

        els = elastic_class.ElasticSearch(self.cfg.host)

        if els.cluster_name:
            status = True

        else:
            status = False

        self.assertTrue(status)

    def test_host_is_list(self):

        """Function:  test_host_is_list

        Description:  Test to see if host is a list.

        Arguments:

        """

        els = elastic_class.ElasticSearch(self.cfg.host)

        if els.hosts == self.cfg.host:
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
            els = elastic_class.ElasticSearch(host_list)

        if els.hosts == host_list:
            status = True

        else:
            status = False

        self.assertTrue(status)


if __name__ == "__main__":
    unittest.main()
