# Classification (U)

"""Program:  elasticsearchrepo_update_repo_status.py

    Description:  Integration testing of update_repo_status method in
        ElasticSearchRepo class in elastic_class.py.

    Usage:
        test/integration/elastic_class/elasticsearchrepo_update_repo_status.py

    Arguments:

"""

# Libraries and Global Variables
from __future__ import print_function

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
        test_repo_dict

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
        esr = elastic_class.ElasticSearchRepo(
            self.cfg.host, repo=self.repo_name)

        if esr.repo_dict:
            print("ERROR: Test environment not clean - repositories exist.")
            self.skipTest("Pre-conditions not met.")

    def test_repo_dict(self):

        """Function:  test_repo_dict

        Description:  Test with repo_dict is set to empty.

        Arguments:

        """

        esr = elastic_class.ElasticSearchRepo(
            self.cfg.host, user=self.cfg.user, japd=self.cfg.japd)
        esr.connect()

        if esr.repo_dict:
            self.assertTrue(esr.repo_dict)

        else:
            self.assertFalse(esr.repo_dict)


if __name__ == "__main__":
    unittest.main()
