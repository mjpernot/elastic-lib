#!/usr/bin/python
# Classification (U)

"""Program:  ElasticSearchDump_init.py

    Description:  Unit testing of __init__ in elastic_class.ElasticSearchDump.

    Usage:
        test/unit/elastic_class/ElasticSearchDump_init.py

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

        self.host_list = ["host1", "host2"]
        self.repo = None
        self.dump_list = []
        self.last_dump = None

    @mock.patch("elastic_class.ElasticSearch.update_status",
                mock.Mock(return_value=True))
    @mock.patch("elastic_class.ElasticSearchDump.update_dump_status",
                mock.Mock(return_value=True))
    def test_default(self):

        """Function:  test_default

        Description:  Test with default settings.

        Arguments:

        """

        es = elastic_class.ElasticSearchDump(self.host_list, repo=self.repo)
        self.assertEqual((es.hosts, es.dump_list, es.repo_name,
                          es.last_dump_name),
                         (self.host_list, self.dump_list, self.repo,
                          self.last_dump))


if __name__ == "__main__":
    unittest.main()
