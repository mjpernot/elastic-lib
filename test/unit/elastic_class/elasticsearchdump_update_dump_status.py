# Classification (U)

"""Program:  elasticsearchdump_update_dump_status.py

    Description:  Unit testing of update_dump_status in
        elastic_class.ElasticSearchDump.

    Usage:
        test/unit/elastic_class/elasticsearchdump_update_dump_status.py

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


class Repo2():                                          # pylint:disable=R0903

    """Class:  Repo2

    Description:  Class representation of the snapshot class.

    Methods:
        get_repository

    """

    def get_repository(self):

        """Method:  get_repository

        Description:  Stub holder for snapshot.get_repository method.

        Arguments:

        """

        return {"reponame": {"type": "dbdump", "settings":
                             {"location": "/dir/path/dump"}},
                "reponame2": {"type": "dbdump2", "settings":
                              {"location": "/dir/path/dump2"}}}


class Repo():                                           # pylint:disable=R0903

    """Class:  Repo

    Description:  Class representation of the snapshot class.

    Methods:
        get_repository

    """

    def get_repository(self):

        """Method:  get_repository

        Description:  Stub holder for snapshot.get_repository method.

        Arguments:

        """

        return {"reponame": {"type": "dbdump", "settings":
                             {"location": "/dir/path/dump"}}}


class Elasticsearch():

    """Class:  ElasticSearch

    Description:  Class representation of the Elasticsearch class.

    Methods:
        __init__
        ping
        info

    """

    def __init__(self, host_list, port=9200):

        """Method:  __init__

        Description:  Initialization instance of the class.

        Arguments:

        """

        self.hosts = host_list
        self.port = port
        self.ping_status = True
        self.info_status = {"cluster_name": "ClusterName",
                            "name": "servername"}
        self.snapshot = Repo()

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
        setUp
        test_dupe_name
        test_repo_not_passed2
        test_repo_not_passed
        test_repo_not_present
        test_default

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.host_list = ["host1", "host2"]
        self.host_str = "host1, host2"
        self.repo = "reponame"
        self.repo2 = "reponame2"
        self.els = Elasticsearch(self.host_list)
        self.get_dump_list = (
            [{"snapshot": "dump1"}, {"snapshot": "dump2"}], True, None)
        self.dump_list = [{"snapshot": "dump1"}, {"snapshot": "dump2"}]
        self.nodes_data = {"serverid1": {"name": "hostname1", "settings":
                                         {"path": {"data": ["/dir/data1"],
                                                   "logs": ["/dir/logs1"]}}},
                           "serverid2": {"name": "hostname2", "settings":
                                         {"path": {"data": ["/dir/data2"],
                                                   "logs": ["/dir/logs2"]}}}}
        self.health_data = {"status": "green", "cluster_name": "ClusterName"}
        self.last_dump = "dump2"

    @mock.patch("elastic_class.get_cluster_nodes",
                mock.Mock(return_value={"_nodes": {"total": 3}}))
    @mock.patch("elastic_class.get_master_name",
                mock.Mock(return_value="MasterName"))
    @mock.patch("elastic_class.get_info",
                mock.Mock(return_value={"name": "localservername"}))
    @mock.patch("elastic_class.elastic_libs.get_latest_dump",
                mock.Mock(return_value="dump2"))
    @mock.patch("elastic_class.ElasticSearchDump.chk_status",
                mock.Mock(return_value=(False, None, True)))
    @mock.patch("elastic_class.get_cluster_health")
    @mock.patch("elastic_class.get_nodes")
    @mock.patch("elastic_class.datetime.datetime")
    @mock.patch("elastic_class.get_dump_list")
    @mock.patch("elastic_class.elasticsearch.Elasticsearch")
    def test_dupe_name(                         # pylint:disable=R0913,R0917
            self, mock_es, mock_list, mock_date, mock_nodes, mock_health):

        """Function:  test_dupe_name

        Description:  Test with duplicate dump name.

        Arguments:

        """

        mock_es.return_value = self.els
        mock_list.return_value = self.get_dump_list
        mock_date.strftime.side_effect = ["dump2", "dump3"]
        mock_nodes.return_value = self.nodes_data
        mock_health.return_value = self.health_data

        els = elastic_class.ElasticSearchDump(self.host_list, repo=self.repo)
        els.connect()
        self.assertEqual(
            (els.hosts, els.dump_list, els.repo_name, els.last_dump_name),
            (self.host_list, self.dump_list, self.repo, self.last_dump))

    @mock.patch("elastic_class.get_cluster_nodes",
                mock.Mock(return_value={"_nodes": {"total": 3}}))
    @mock.patch("elastic_class.get_master_name",
                mock.Mock(return_value="MasterName"))
    @mock.patch("elastic_class.get_info",
                mock.Mock(return_value={"name": "localservername"}))
    @mock.patch("elastic_class.elastic_libs.get_latest_dump",
                mock.Mock(return_value="dump2"))
    @mock.patch("elastic_class.get_cluster_health")
    @mock.patch("elastic_class.get_nodes")
    @mock.patch("elastic_class.get_dump_list")
    @mock.patch("elastic_class.elasticsearch.Elasticsearch")
    def test_repo_not_passed2(self, mock_es, mock_list, mock_nodes,
                              mock_health):

        """Function:  test_repo_not_passed2

        Description:  Test with repo not passed and multiple repos.

        Arguments:

        """

        self.els.snapshot = Repo2()

        mock_es.return_value = self.els
        mock_list.return_value = self.get_dump_list
        mock_nodes.return_value = self.nodes_data
        mock_health.return_value = self.health_data

        els = elastic_class.ElasticSearchDump(self.host_list)
        els.connect()
        self.assertEqual(
            (els.hosts, els.dump_list, els.repo_name, els.last_dump_name),
            (self.host_list, [], None, None))

    @mock.patch("elastic_class.get_cluster_nodes",
                mock.Mock(return_value={"_nodes": {"total": 3}}))
    @mock.patch("elastic_class.get_master_name",
                mock.Mock(return_value="MasterName"))
    @mock.patch("elastic_class.get_info",
                mock.Mock(return_value={"name": "localservername"}))
    @mock.patch("elastic_class.elastic_libs.get_latest_dump",
                mock.Mock(return_value="dump2"))
    @mock.patch("elastic_class.get_cluster_health")
    @mock.patch("elastic_class.get_nodes")
    @mock.patch("elastic_class.get_dump_list")
    @mock.patch("elastic_class.elasticsearch.Elasticsearch")
    def test_repo_not_passed(self, mock_es, mock_list, mock_nodes,
                             mock_health):

        """Function:  test_repo_not_passed

        Description:  Test with repo not passed as argument.

        Arguments:

        """

        mock_es.return_value = self.els
        mock_list.return_value = self.get_dump_list
        mock_nodes.return_value = self.nodes_data
        mock_health.return_value = self.health_data

        els = elastic_class.ElasticSearchDump(self.host_list)
        els.connect()
        self.assertEqual(
            (els.hosts, els.dump_list, els.repo_name, els.last_dump_name),
            (self.host_list, self.dump_list, self.repo, self.last_dump))

    @mock.patch("elastic_class.get_cluster_nodes",
                mock.Mock(return_value={"_nodes": {"total": 3}}))
    @mock.patch("elastic_class.get_master_name",
                mock.Mock(return_value="MasterName"))
    @mock.patch("elastic_class.get_info",
                mock.Mock(return_value={"name": "localservername"}))
    @mock.patch("elastic_class.elastic_libs.get_latest_dump",
                mock.Mock(return_value="dump2"))
    @mock.patch("elastic_class.get_cluster_health")
    @mock.patch("elastic_class.get_nodes")
    @mock.patch("elastic_class.get_dump_list")
    @mock.patch("elastic_class.elasticsearch.Elasticsearch")
    def test_repo_not_present(self, mock_es, mock_list, mock_nodes,
                              mock_health):

        """Function:  test_repo_not_present

        Description:  Test with repo not present.

        Arguments:

        """

        mock_es.return_value = self.els
        mock_list.return_value = self.get_dump_list
        mock_nodes.return_value = self.nodes_data
        mock_health.return_value = self.health_data

        els = elastic_class.ElasticSearchDump(self.host_list, repo=self.repo2)
        els.connect()
        self.assertEqual(
            (els.hosts, els.dump_list, els.repo_name, els.last_dump_name),
            (self.host_list, [], None, None))

    @mock.patch("elastic_class.elastic_libs.get_latest_dump",
                mock.Mock(return_value="dump2"))
    @mock.patch("elastic_class.get_master_name",
                mock.Mock(return_value="MasterName"))
    @mock.patch("elastic_class.get_cluster_nodes",
                mock.Mock(return_value={"_nodes": {"total": 3}}))
    @mock.patch("elastic_class.get_info",
                mock.Mock(return_value={"name": "localservername"}))
    @mock.patch("elastic_class.get_cluster_health")
    @mock.patch("elastic_class.get_nodes")
    @mock.patch("elastic_class.get_dump_list")
    @mock.patch("elastic_class.elasticsearch.Elasticsearch")
    def test_default(self, mock_es, mock_list, mock_nodes, mock_health):

        """Function:  test_default

        Description:  Test with default settings.

        Arguments:

        """

        mock_es.return_value = self.els
        mock_list.return_value = self.get_dump_list
        mock_nodes.return_value = self.nodes_data
        mock_health.return_value = self.health_data

        els = elastic_class.ElasticSearchDump(self.host_list, repo=self.repo)
        els.connect()
        self.assertEqual((els.hosts, els.dump_list, els.repo_name,
                          els.last_dump_name),
                         (self.host_list, self.dump_list, self.repo,
                          self.last_dump))


if __name__ == "__main__":
    unittest.main()
