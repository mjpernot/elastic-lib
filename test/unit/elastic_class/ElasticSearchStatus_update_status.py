#!/usr/bin/python
# Classification (U)

"""Program:  ElasticSearchStatus_update_status.py

    Description:  Unit testing of update_status in
        elastic_class.ElasticSearchStatus.

    Usage:
        test/unit/elastic_class/ElasticSearchStatus_update_status.py

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


class Elasticsearch(object):

    """Class:  ElasticSearch

    Description:  Class representation of the Elasticsearch class.

    Methods:
        __init__ -> Initialize configuration environment.
        ping -> Stub holder for Elasticsearch.ping method.
        info -> Stub holder for Elasticsearch.info method.

    """

    def __init__(self, host_list, port=9200):

        """Method:  __init__

        Description:  Initialization instance of the class.

        Arguments:

        """

        self.hosts = host_list
        self.port = port
        self.ping_status = True
        self.info_status = {"cluster_name": "ClusterName", "name": "servername"}

    def ping(self):

        """Method:  ping

        Description:  Stub holder for Elasticsearch.ping method.

        Arguments:

        """

        return self.ping_status

    def info(self):

        """Method:  info

        Description:  Stub holder for Elasticsearch.info method.

        Arguments:

        """

        return self.info_status


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Initialization for unit testing.
        test_ping_false -> Test ping of Elasticsearch server is False.
        test_ping_true -> Test ping of Elasticsearch server is True.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.host_list = ["host1", "host2"]
        self.es = Elasticsearch(self.host_list)
        self.health_data = {"unassigned_shards": 10,
                            "active_shards_percent_as_number": 20,
                            "number_of_pending_tasks": 1,
                            "active_shards": 100,
                            "active_primary_shards": 50}
        self.shards_data = ["shard1", "shard2"]
        self.status_data = {"_nodes": {"failed": 0},
                            "nodes": {"process": {"cpu": {"percent": 75}},
                                      "jvm": {"max_uptime_in_millis": 100},
                                      "os": {"mem": {"used_percent": 55,
                                                     "total_in_bytes": 1234567,
                                                     "used_in_bytes": 123456,
                                                     "free_in_bytes": 120000},
                                             "allocated_processors": 2}}}
        self.disks_data = ["disk1", "disk2"]
        self.repo_data = {"repo1": "green", "repo2": "green"}

    @mock.patch("elastic_class.ElasticSearch.update_status",
                mock.Mock(return_value=True))
    @mock.patch("elastic_class.elasticsearch.Elasticsearch")
    def test_ping_false(self, mock_es):

        """Function:  test_ping_false

        Description:  Test ping of Elasticsearch server is False.

        Arguments:

        """

        self.es.ping_status = False
        mock_es.return_value = self.es

        es = elastic_class.ElasticSearchStatus(self.host_list)
        es.update_status()
        self.assertEqual((es.port, es.hosts, es.is_connected),
                         (9200, self.host_list, False))

    @mock.patch("elastic_class.get_repo_list")
    @mock.patch("elastic_class.get_disks")
    @mock.patch("elastic_class.get_cluster_status")
    @mock.patch("elastic_class.get_shards")
    @mock.patch("elastic_class.get_cluster_health")
    @mock.patch("elastic_class.ElasticSearch.update_status",
                mock.Mock(return_value=True))
    @mock.patch("elastic_class.elasticsearch.Elasticsearch")
    def test_ping_true(self, mock_es, mock_health, mock_shards, mock_status,
                       mock_disks, mock_repo):

        """Function:  test_ping_true

        Description:  Test ping of Elasticsearch server is True.

        Arguments:

        """

        mock_es.return_value = self.es
        mock_health.return_value = self.health_data
        mock_shards.return_value = self.shards_data
        mock_status.return_value = self.status_data
        mock_disks.return_value = self.disks_data
        mock_repo.return_value = self.repo_data

        es = elastic_class.ElasticSearchStatus(self.host_list)
        es.update_status()
        self.assertEqual((es.port, es.hosts, es.is_connected, es.shard_list),
                         (9200, self.host_list, True, self.shards_data))


if __name__ == "__main__":
    unittest.main()
