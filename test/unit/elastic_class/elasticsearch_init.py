#!/usr/bin/python
# Classification (U)

"""Program:  elasticsearch_init.py

    Description:  Unit testing of __init__ in elastic_class.ElasticSearch.

    Usage:
        test/unit/elastic_class/elasticsearch_init.py

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
import version

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_port_change
        test_host_list

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.host_list = ["host1", "host2"]

    def test_port_change(self):

        """Function:  test_port_change

        Description:  Test with change to port.

        Arguments:

        """

        els = elastic_class.ElasticSearch(self.host_list, port=9201)
        self.assertEqual((els.port, els.hosts), (9201, self.host_list))

    def test_host_list(self):

        """Function:  test_host_list

        Description:  Test host_list is a list.

        Arguments:

        """

        els = elastic_class.ElasticSearch(self.host_list)
        self.assertEqual((els.port, els.hosts), (9200, self.host_list))


if __name__ == "__main__":
    unittest.main()
