# Classification (U)

"""Program:  elasticsearchdump_init.py

    Description:  Unit testing of __init__ in elastic_class.ElasticSearchDump.

    Usage:
        test/unit/elastic_class/elasticsearchdump_init.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import unittest
import mock

# Local
sys.path.append(os.getcwd())
import elastic_class                            # pylint:disable=E0401,C0413
import version                                  # pylint:disable=E0401,C0413

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_default

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
    def test_default(self):

        """Function:  test_default

        Description:  Test with default settings.

        Arguments:

        """

        els = elastic_class.ElasticSearchDump(self.host_list, repo=self.repo)
        self.assertEqual((els.hosts, els.dump_list, els.repo_name,
                          els.last_dump_name),
                         (self.host_list, self.dump_list, self.repo,
                          self.last_dump))


if __name__ == "__main__":
    unittest.main()
