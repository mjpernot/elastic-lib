#!/usr/bin/python
# Classification (U)

"""Program:  list_dumps.py

    Description:  Unit testing of list_dumps in elastic_libs.py.

    Usage:
        test/unit/elastic_libs/list_dumps.py

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
import elastic_libs
import lib.gen_libs as gen_libs
import version

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_print_raw
        test_print_empty
        test_print_dump

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        # Test me
        self.list_multi = [
            {"snapshot": "dump1", "state": "SUCCESS",
             "start_time": "2022-02-16TO08:15:12.013Z",
             "shards": {"successful": 12, "failed": 0, "total": 12}},
            {"snapshot": "dump2", "state": "SUCCESS",
             "start_time": "2022-02-21TO09:11:11.122Z",
             "shards": {"successful": 15, "failed": 0, "total": 15}}]
        self.empty_list = []

    def test_print_raw(self):

        """Function:  test_print_raw

        Description:  Test printing with raw option.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertFalse(
                elastic_libs.list_dumps(self.list_multi, raw=True))

    def test_print_empty(self):

        """Function:  test_print_empty

        Description:  Test printing of empty list.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertFalse(elastic_libs.list_dumps(self.empty_list))

    def test_print_dump(self):

        """Function:  test_print_dump

        Description:  Test printing of dump list.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertFalse(elastic_libs.list_dumps(self.list_multi))


if __name__ == "__main__":
    unittest.main()
