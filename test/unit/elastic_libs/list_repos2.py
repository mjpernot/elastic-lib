#!/usr/bin/python
# Classification (U)

"""Program:  list_repos2.py

    Description:  Unit testing of list_repos2 in elastic_libs.py.

    Usage:
        test/unit/elastic_libs/list_repos2.py

    Arguments:
        None

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
import mock

# Local
sys.path.append(os.getcwd())
import elastic_libs
import lib.gen_libs as gen_libs
import version

# Version
__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Super-Class:  unittest.TestCase

    Sub-Classes:  None

    Methods:
        setUp -> Unit testing initilization.
        test_print_empty -> Test printing of empty list.
        test_print_dump -> Test printing of dump list.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:
            None

        """

        self.list_mult = {u'BACKUP_TEST2':
                          {u'type': u'fs', u'settings':
                           {u'compress': u'true',
                            u'location': u'/mnt/BACKUP_TEST2'}},
                          u'BACKUP_TEST':
                          {u'type': u'fs',
                           u'settings': {u'compress': u'true',
                                         u'location': u'/mnt/BACKUP_TEST'}}}

        self.empty_list = []

    def test_print_empty(self):

        """Function:  test_print_empty

        Description:  Test printing of empty list.

        Arguments:
            None

        """

        with gen_libs.no_std_out():
            self.assertFalse(elastic_libs.list_repos2(self.empty_list))

    def test_print_dump(self):

        """Function:  test_print_dump

        Description:  Test printing of dump list.

        Arguments:
            None

        """

        with gen_libs.no_std_out():
            self.assertFalse(elastic_libs.list_repos2(self.list_mult))


if __name__ == "__main__":
    unittest.main()
