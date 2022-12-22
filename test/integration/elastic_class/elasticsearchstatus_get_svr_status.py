# Classification (U)

"""Program:  elasticsearchstatus_get_svr_status.py

    Description:  Integration testing of get_svr_status method in
        ElasticSearchStatus class in elastic_class.py.

    Usage:
        test/integration/elastic_class/elasticsearchstatus_get_svr_status.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import unittest

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
        data = ess.uptime / 1000
        seconds = data % 60
        data /= 60
        minutes = data % 60
        data /= 60
        hours = data % 24
        data /= 24
        days = data
        uptime = "%d days %d hours %d minutes %d seconds" \
                 % (days, hours, minutes, seconds)
        results = {
            "Server": {
                "Uptime": uptime, "AllocatedCPU": ess.alloc_cpu,
                "CPUActive": ess.cpu_active}}

        self.assertEqual(ess.get_svr_status(), results)


if __name__ == "__main__":
    unittest.main()
