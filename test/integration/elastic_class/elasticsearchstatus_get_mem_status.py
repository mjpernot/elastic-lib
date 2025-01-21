# Classification (U)

"""Program:  elasticsearchstatus_get_mem_status.py

    Description:  Integration testing of get_mem_status method in
        ElasticSearchStatus class in elastic_class.py.

    Usage:
        test/integration/elastic_class/elasticsearchstatus_get_mem_status.py

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


def bytes_2_readable(size, precision=2):

    """Function:  bytes_2_readable

    Description:  Converts a size (in bytes) in the appropriate readable size
        with post-tag symbol.

    Arguments:
        (input) size -> Size in bytes to convert.
        (input) precision -> Percision after decimal.

    """

    suffix = ["B", "KB", "MB", "GB", "TB"]
    suf_index = 0

    while size > 1024 and suf_index < 4:
        suf_index += 1
        size = size / 1024.0

    return f"{size:.{precision}f}{suffix[suf_index]}"


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
        mem_total = bytes_2_readable(ess.mem_total)
        mem_used = bytes_2_readable(ess.mem_used)
        mem_free = bytes_2_readable(ess.mem_free)
        results = {
            "Memory": {"Percent": ess.mem_per_used, "Total": mem_total,
                       "Used": mem_used, "Free": mem_free}}

        self.assertEqual(ess.get_mem_status(), results)


if __name__ == "__main__":
    unittest.main()
