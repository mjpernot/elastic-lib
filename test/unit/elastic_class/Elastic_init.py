#!/usr/bin/python
# Classification (U)

"""Program:  Elastic_init.py

    Description:  Unit testing of __init__ in elastic_class.Elastic class.

    Usage:
        test/unit/elastic_class/Elastic_init.py

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
import mock

# Local
sys.path.append(os.getcwd())
import elastic_class
import lib.gen_libs as gen_libs
import version

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Initialization for unit testing.
        test_default -> Test with default settings.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.host_name = "host1"
        self.get_data = {"nodes":
                         {"first":
                          {"settings":
                           {"path":
                            {"data": "data_dir", "logs": "log_dir"}}},
                          "second":
                          {"settings":
                           {"path":
                            {"data": "data_dir2", "logs": "log_dir2"}}}}}

    @mock.patch("elastic_class.requests_libs.get_query")
    def test_default(self, mock_get):

        """Function:  test_default

        Description:  Test with default settings.

        Arguments:

        """

        mock_get.return_value = self.get_data

        es = elastic_class.Elastic(self.host_name)
        self.assertEqual((es.port, es.node, es.data, es.logs),
                         (9200, self.host_name, "data_dir2", "log_dir2"))


if __name__ == "__main__":
    unittest.main()
