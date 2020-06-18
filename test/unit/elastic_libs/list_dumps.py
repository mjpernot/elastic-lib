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
        setUp -> Unit testing initilization.
        test_print_empty -> Test printing of empty list.
        test_print_dump -> Test printing of dump list.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.list_mult = [[u'yavin_bkp_20171004-1153', u'SUCCESS',
                           u'1507118001', u'11:53:21', u'1507118120',
                           u'11:55:20', u'1.9m', u'35', u'175', u'0', u'175'],
                          [u'yavin_bkp_20171010-1234', u'SUCCESS',
                           u'1507638885', u'12:34:45', u'1507639060',
                           u'12:37:40', u'2.9m', u'41', u'205', u'0', u'205']]
        self.empty_list = []

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
            self.assertFalse(elastic_libs.list_dumps(self.list_mult))


if __name__ == "__main__":
    unittest.main()
