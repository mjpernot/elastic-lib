# Classification (U)

"""Program:  list_repos2.py

    Description:  Unit testing of list_repos2 in elastic_libs.py.

    Usage:
        test/unit/elastic_libs/list_repos2.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import unittest

# Local
sys.path.append(os.getcwd())
import elastic_libs                             # pylint:disable=E0401,C0413
import lib.gen_libs as gen_libs             # pylint:disable=E0401,C0413,R0402
import version                                  # pylint:disable=E0401,C0413

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_print_empty
        test_print_dump

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.list_mult = {'BACKUP_TEST2':
                          {'type': 'fs', 'settings':
                           {'compress': 'true',
                            'location': '/mnt/BACKUP_TEST2'}},
                          'BACKUP_TEST':
                          {'type': 'fs',
                           'settings': {'compress': 'true',
                                        'location': '/mnt/BACKUP_TEST'}}}

        self.empty_list = []

    def test_print_empty(self):

        """Function:  test_print_empty

        Description:  Test printing of empty list.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertFalse(elastic_libs.list_repos2(self.empty_list))

    def test_print_dump(self):

        """Function:  test_print_dump

        Description:  Test printing of dump list.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertFalse(elastic_libs.list_repos2(self.list_mult))


if __name__ == "__main__":
    unittest.main()
