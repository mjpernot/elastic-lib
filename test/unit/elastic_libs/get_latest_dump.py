#!/usr/bin/python
# Classification (U)

"""Program:  get_latest_dump.py

    Description:  Unit testing of get_latest_dump in elastic_libs.py.

    Usage:
        test/unit/elastic_libs/get_latest_dump.py

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
import version

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Unit testing initilization.
        test_list_reverse -> Test dump_list entries are reversed.
        test_list_multi -> Test dump_list has multiple entry.
        test_list_one -> Test dump_list has one entry.
        test_empty_list -> Test dump_list is empty.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.empty_list = []
        self.list_one = [[u'yavin_bkp_20171004-1153', u'SUCCESS',
                          u'1507118001', u'11:53:21', u'1507118120',
                          u'11:55:20', u'1.9m', u'35', u'175', u'0', u'175']]
        self.list_mult = [[u'yavin_bkp_20171004-1153', u'SUCCESS',
                           u'1507118001', u'11:53:21', u'1507118120',
                           u'11:55:20', u'1.9m', u'35', u'175', u'0', u'175'],
                          [u'yavin_bkp_20171010-1234', u'SUCCESS',
                           u'1507638885', u'12:34:45', u'1507639060',
                           u'12:37:40', u'2.9m', u'41', u'205', u'0', u'205'],
                          [u'yavin_bkp_20171011-1137', u'SUCCESS',
                           u'1507721867', u'11:37:47', u'1507722088',
                           u'11:41:28', u'3.6m', u'42', u'210', u'0', u'210'],
                          [u'yavin_bkp_20171011-1142', u'SUCCESS',
                           u'1507722132', u'11:42:12', u'1507722204',
                           u'11:43:24', u'1.1m', u'42', u'210', u'0', u'210']]
        self.list_revr = [[u'yavin_bkp_20171011-1142', u'SUCCESS',
                           u'1507722132', u'11:42:12', u'1507722204',
                           u'11:43:24', u'1.1m', u'42', u'210', u'0', u'210'],
                          [u'yavin_bkp_20171011-1137', u'SUCCESS',
                           u'1507721867', u'11:37:47', u'1507722088',
                           u'11:41:28', u'3.6m', u'42', u'210', u'0', u'210'],
                          [u'yavin_bkp_20171010-1234', u'SUCCESS',
                           u'1507638885', u'12:34:45', u'1507639060',
                           u'12:37:40', u'2.9m', u'41', u'205', u'0', u'205'],
                          [u'yavin_bkp_20171004-1153', u'SUCCESS',
                           u'1507118001', u'11:53:21', u'1507118120',
                           u'11:55:20', u'1.9m', u'35', u'175', u'0', u'175']]

    def test_list_reverse(self):

        """Function:  test_list_reverse

        Description:  Test dump_list entries are reversed.

        Arguments:

        """

        self.assertEqual(elastic_libs.get_latest_dump(self.list_revr),
                         ("yavin_bkp_20171011-1142"))

    def test_list_multi(self):

        """Function:  test_list_multi

        Description:  Test dump_list has multiple entry.

        Arguments:

        """

        self.assertEqual(elastic_libs.get_latest_dump(self.list_mult),
                         ("yavin_bkp_20171011-1142"))

    def test_list_one(self):

        """Function:  test_list_one

        Description:  Test dump_list has one entry.

        Arguments:

        """

        self.assertEqual(elastic_libs.get_latest_dump(self.list_one),
                         ("yavin_bkp_20171004-1153"))

    def test_empty_list(self):

        """Function:  test_empty_list

        Description:  Test dump_list is empty.

        Arguments:

        """

        self.assertEqual(elastic_libs.get_latest_dump(self.empty_list),
                         (None))


if __name__ == "__main__":
    unittest.main()
