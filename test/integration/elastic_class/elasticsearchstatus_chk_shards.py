# Classification (U)

"""Program:  elasticsearchstatus_chk_shards.py

    Description:  Integration testing of chk_shards method in
        ElasticSearchStatus class in elastic_class.py.

    Usage:
        test/integration/elastic_class/elasticsearchstatus_chk_shards.py

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
        shards = [
            item for item in ess.shard_list if item["state"] != "STARTED"]

        if ess.unassigned_shards > 0 or ess.active_shards_percent < 100 \
           or shards:
            self.assertTrue(ess.chk_shards()["ShardWarning"])

        else:
            self.assertFalse(ess.chk_shards())


if __name__ == "__main__":
    unittest.main()
