#!/usr/bin/python
# Classification (U)

"""Program:  ElasticStatus_init.py

    Description:  Unit testing of __init__ in elastic_class.ElasticStatus
        class.

    Usage:
        test/unit/elastic_class/ElasticStatus_init.py

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
        test_disk_arg -> Test passing disk argument.
        test_cpu_arg -> Test passing cpu argument.
        test_mem_arg -> Test passing memory argument.
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
        self.get_data2 = {"cluster_name": "clustername",
                          "nodes": {"id1": {"name": "node1"}},
                          "_nodes": {"total": 1}}
        self.get_data3 = {"status": "green"}
        self.get_data4 = "id1 ip_address ip_address hostname\n"
        self.get_data5 = {"reponame1": {"settings": {"location": "/dir/data"}}}
        self.get_data6 = {"unassigned_shards": 1,
                          "active_shards_percent_as_number": 90,
                          "number_of_pending_tasks": 0,
                          "active_shards": 9,
                          "active_primary_shards": 5}
        self.get_data7 = \
            "shard1 d1 d2 STARTED host\nshard1 d1 d2 UNASSIGNED host\n"
        self.get_data8 = {"_nodes": {"failed": 0},
                          "nodes": {"process": {"cpu": {"percent": 75}},
                                    "jvm": {"max_uptime_in_millis": 100},
                                    "os": {"mem": {"used_percent": 55,
                                                   "total_in_bytes": 1234567,
                                                   "used_in_bytes": 123456,
                                                   "free_in_bytes": 120000},
                                           "allocated_processors": 2}}}
        self.get_data9 = "995 69mb 16gb 53gb 69gb 23 ip1 ip2 hostname\n"

    @mock.patch("elastic_class.requests_libs.get_query")
    def test_disk_arg(self, mock_get):

        """Function:  test_disk_arg

        Description:  Test passing disk argument.

        Arguments:

        """

        mock_get.side_effect = [self.get_data, self.get_data2, self.get_data3,
                                self.get_data4, self.get_data5, self.get_data6,
                                self.get_data7, self.get_data8, self.get_data9]

        es = elastic_class.ElasticStatus(self.host_name, cutoff_disk=30)
        self.assertEqual((es.num_shards, es.failed_nodes, es.alloc_cpu,
                          es.cpu_active, es.pending_tasks, es.cutoff_disk),
                         (9, 0, 2, 75, 0, 30))

    @mock.patch("elastic_class.requests_libs.get_query")
    def test_cpu_arg(self, mock_get):

        """Function:  test_cpu_arg

        Description:  Test passing cpu argument.

        Arguments:

        """

        mock_get.side_effect = [self.get_data, self.get_data2, self.get_data3,
                                self.get_data4, self.get_data5, self.get_data6,
                                self.get_data7, self.get_data8, self.get_data9]

        es = elastic_class.ElasticStatus(self.host_name, cutoff_cpu=20)
        self.assertEqual((es.num_shards, es.failed_nodes, es.alloc_cpu,
                          es.cpu_active, es.pending_tasks, es.cutoff_cpu),
                         (9, 0, 2, 75, 0, 20))

    @mock.patch("elastic_class.requests_libs.get_query")
    def test_mem_arg(self, mock_get):

        """Function:  test_mem_arg

        Description:  Test passing memory argument.

        Arguments:

        """

        mock_get.side_effect = [self.get_data, self.get_data2, self.get_data3,
                                self.get_data4, self.get_data5, self.get_data6,
                                self.get_data7, self.get_data8, self.get_data9]

        es = elastic_class.ElasticStatus(self.host_name, cutoff_mem=10)
        self.assertEqual((es.num_shards, es.failed_nodes, es.alloc_cpu,
                          es.cpu_active, es.pending_tasks, es.cutoff_mem),
                         (9, 0, 2, 75, 0, 10))

    @mock.patch("elastic_class.requests_libs.get_query")
    def test_default(self, mock_get):

        """Function:  test_default

        Description:  Test with default settings.

        Arguments:

        """

        mock_get.side_effect = [self.get_data, self.get_data2, self.get_data3,
                                self.get_data4, self.get_data5, self.get_data6,
                                self.get_data7, self.get_data8, self.get_data9]

        es = elastic_class.ElasticStatus(self.host_name)
        self.assertEqual((es.num_shards, es.failed_nodes, es.alloc_cpu,
                          es.cpu_active, es.pending_tasks),
                         (9, 0, 2, 75, 0))


if __name__ == "__main__":
    unittest.main()
