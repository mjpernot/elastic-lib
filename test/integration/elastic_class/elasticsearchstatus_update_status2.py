#!/usr/bin/python
# Classification (U)

"""Program:  elasticsearchstatus_update_status2.py

    Description:  Integration testing of update_status2 method in
        ElasticSearchStatus class in elastic_class.py.

    Usage:
        test/integration/elastic_class/elasticsearchstatus_update_status2.py

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
        test_mem_free
        test_disk_list

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

    def test_mem_free(self):

        """Function:  test_mem_free

        Description:  Test with mem_free is set.

        Arguments:

        """

        ess = elastic_class.ElasticSearchStatus(
            self.cfg.host, user=self.cfg.user, japd=self.cfg.japd)
        ess.connect()

        self.assertTrue(ess.mem_free)

    def test_disk_list(self):

        """Function:  test_disk_list

        Description:  Test with disk_list is set.

        Arguments:

        """

        ess = elastic_class.ElasticSearchStatus(
            self.cfg.host, user=self.cfg.user, japd=self.cfg.japd)
        ess.connect()

        self.assertTrue(ess.disk_list)


if __name__ == "__main__":
    unittest.main()
