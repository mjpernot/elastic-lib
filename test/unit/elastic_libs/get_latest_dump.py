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
import unittest

# Local
sys.path.append(os.getcwd())
import elastic_libs                             # pylint:disable=E0401,C0413
import version                                  # pylint:disable=E0401,C0413

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_list_reverse
        test_list_multi
        test_list_one
        test_empty_list

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.list = []
        self.list1 = [{
            "snapshot": "yavin_bkp_20171004-1153", "state": "SUCCESS",
            "start_time_in_millis": 1507118001,
            "end_time_in_millis": 1507118120}]
        self.list2 = [
            {
                "snapshot": "yavin_bkp_20171004-1153", "state": "SUCCESS",
                "start_time_in_millis": 1507118001,
                "end_time_in_millis": 1507118120},
            {
                "snapshot": "yavin_bkp_20171010-1234", "state": "SUCCESS",
                "start_time_in_millis": 1507638885,
                "end_time_in_millis": 1507639060},
            {
                "snapshot": "yavin_bkp_20171011-1137", "state": "SUCCESS",
                "start_time_in_millis": 1507721867,
                "end_time_in_millis": 1507722088},
            {
                "snapshot": "yavin_bkp_20171011-1142", "state": "SUCCESS",
                "start_time_in_millis": 1507722132,
                "end_time_in_millis": 1507722204}]
        self.list3 = [
            {
                "snapshot": "yavin_bkp_20171011-1142", "state": "SUCCESS",
                "start_time_in_millis": 1507722132,
                "end_time_in_millis": 1507722204},
            {
                "snapshot": "yavin_bkp_20171011-1137", "state": "SUCCESS",
                "start_time_in_millis": 1507721867,
                "end_time_in_millis": 1507722088},
            {
                "snapshot": "yavin_bkp_20171010-1234", "state": "SUCCESS",
                "start_time_in_millis": 1507638885,
                "end_time_in_millis": 1507639060},
            {
                "snapshot": "yavin_bkp_20171004-1153", "state": "SUCCESS",
                "start_time_in_millis": 1507118001,
                "end_time_in_millis": 1507118120}]

    def test_list_reverse(self):

        """Function:  test_list_reverse

        Description:  Test dump_list entries are reversed.

        Arguments:

        """

        self.assertEqual(elastic_libs.get_latest_dump(self.list3),
                         ("yavin_bkp_20171011-1142"))

    def test_list_multi(self):

        """Function:  test_list_multi

        Description:  Test dump_list has multiple entry.

        Arguments:

        """

        self.assertEqual(elastic_libs.get_latest_dump(self.list2),
                         ("yavin_bkp_20171011-1142"))

    def test_list_one(self):

        """Function:  test_list_one

        Description:  Test dump_list has one entry.

        Arguments:

        """

        self.assertEqual(elastic_libs.get_latest_dump(self.list1),
                         ("yavin_bkp_20171004-1153"))

    def test_empty_list(self):

        """Function:  test_empty_list

        Description:  Test dump_list is empty.

        Arguments:

        """

        self.assertEqual(elastic_libs.get_latest_dump(self.list),
                         (None))


if __name__ == "__main__":
    unittest.main()
