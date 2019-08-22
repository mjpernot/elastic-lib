#!/usr/bin/python
# Classification (U)

"""Program:  ElasticCluster_init.py

    Description:  Unit testing of __init__ in elastic_class.ElasticCluster
        class.

    Usage:
        test/unit/elastic_class/ElasticCluster_init.py

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
        self.get_data2 = {"cluster_name":  "clustername",
                          "nodes":  {"id1": {"name": "node1"}},
                          "_nodes": {"total": 1}}
        self.get_data3 = {"status": "green"}
        self.get_data4 = "id1 ip_address ip_address hostname\n"
        self.get_data5 = {"reponame1": {"settings": {"location": "/dir/data"}}}

    @mock.patch("elastic_class.requests_libs.get_query")
    def test_default(self, mock_get):

        """Function:  test_default

        Description:  Test with default settings.

        Arguments:

        """

        mock_get.side_effect = [self.get_data, self.get_data2, self.get_data3,
                                self.get_data4, self.get_data5]

        es = elastic_class.ElasticCluster(self.host_name)
        self.assertEqual((es.cluster, es.total_nodes, es.cluster_status,
                          es.master),
                         (clustername, 1, "green", "log_dir2", "hostname"))


if __name__ == "__main__":
    unittest.main()
