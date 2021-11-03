#!/usr/bin/python
# Classification (U)

"""Program:  elasticsearch_update.py

    Description:  Integration testing of update of the ElasticSearch
        class in elastic_class.py.

    Usage:
        test/integration/elastic_class/elasticsearch_update.py

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
        test_update_success

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

    def test_update_success(self):

        """Function:  test_update_success

        Description:  Test to if update has been successful.

        Arguments:

        """

        els = elastic_class.ElasticSearch(
            self.cfg.host, user=self.cfg.user, japd=self.cfg.japd)
        els.connect()

        self.assertTrue(els.total_nodes > 0)


if __name__ == "__main__":
    unittest.main()
