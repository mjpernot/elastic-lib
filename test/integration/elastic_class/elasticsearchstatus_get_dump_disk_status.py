# Classification (U)

"""Program:  elasticsearchstatus_get_dump_disk_status.py

    Description:  Integration testing of get_dump_disk_status method in
        ElasticSearchStatus class in elastic_class.py.

    Usage:
    test/integration/elastic_class/elasticsearchstatus_get_dump_disk_status.py

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
        test_data

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

    def test_data(self):

        """Function:  test_data

        Description:  Test with correct data is returned.

        Arguments:

        """

        ess = elastic_class.ElasticSearchStatus(
            self.cfg.host, user=self.cfg.user, japd=self.cfg.japd)
        ess.connect()

        if ess.repo_dict:
            self.assertTrue(ess.get_dump_disk_status()["DumpUsage"])

        else:
            self.assertFalse(ess.get_dump_disk_status()["DumpUsage"])


if __name__ == "__main__":
    unittest.main()
