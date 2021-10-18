#!/usr/bin/python
# Classification (U)

"""Program:  elasticsearchrepo_create_repo.py

    Description:  Unit testing of create_repo in
        elastic_class.ElasticSearchRepo class.

    Usage:
        test/unit/elastic_class/elasticsearchrepo_create_repo.py

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
        __init__

    """

    def __init__(self, host_list, port=9200):

        """Method:  __init__

        Description:  Initialization instance of the class.

        Arguments:

        """

        self.hosts = host_list
        self.port = port
        self.info_status = {"cluster_name": "ClusterName",
                            "name": "servername"}


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_not_created_repo
        test_not_detected_repo
        test_missing_repo_name
        test_no_repo_dir
        test_no_repo_name
        test_default

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.host_list = ["host1", "host2"]
        self.repo = "reponame"
        self.repo2 = "reponame2"
        self.repo3 = "reponame3"
        self.els = Elasticsearch(self.host_list)
        self.repo_dir = "/dir/path/dump2"
        self.nodes_data = {"serverid1": {"name": "hostname1", "settings":
                                         {"path": {"data": ["/dir/data1"],
                                                   "logs": ["/dir/logs1"]}}},
                           "serverid2": {"name": "hostname2", "settings":
                                         {"path": {"data": ["/dir/data2"],
                                                   "logs": ["/dir/logs2"]}}}}
        self.health_data = {"status": "green", "cluster_name": "ClusterName"}
        self.dump = "/dir/path/dump"
        self.repo_list = {"reponame": {"type": "dbdump", "settings":
                                       {"location": self.dump}}}
        self.repo_dict = {"reponame": {"type": "dbdump", "settings":
                                       {"location": self.dump}}}
        self.repo_dict2 = {"reponame": {"type": "dbdump", "settings":
                                        {"location": self.dump}},
                           "reponame2": {"type": "dbdump", "settings":
                                         {"location": "/dir/path/dump2"}}}

    @mock.patch("elastic_class.create_snapshot_repo",
                mock.Mock(return_value={"acknowledged": False}))
    @mock.patch("elastic_class.ElasticSearch.update_status",
                mock.Mock(return_value=True))
    @mock.patch("elastic_class.is_active", mock.Mock(return_value=True))
    @mock.patch("elastic_class.get_repo_list")
    @mock.patch("elastic_class.elasticsearch.Elasticsearch")
    def test_not_created_repo(self, mock_es, mock_repo):

        """Function:  test_not_created_repo

        Description:  Test with repository not created.

        Arguments:

        """

        mock_es.return_value = self.els
        mock_repo.side_effect = [self.repo_dict, self.repo_dict2]

        els = elastic_class.ElasticSearchRepo(self.host_list, repo=self.repo,
                                              repo_dir=self.repo_dir)
        els.repo_name = None
        self.assertEqual(
            els.create_repo(self.repo3, self.repo_dir),
            (True,
             "ERROR:  Repository creation failure: " +
             " reponame3, /dir/path/dump2"))

    @mock.patch("elastic_class.create_snapshot_repo",
                mock.Mock(return_value={"acknowledged": True}))
    @mock.patch("elastic_class.ElasticSearch.update_status",
                mock.Mock(return_value=True))
    @mock.patch("elastic_class.is_active", mock.Mock(return_value=True))
    @mock.patch("elastic_class.get_repo_list")
    @mock.patch("elastic_class.elasticsearch.Elasticsearch")
    def test_not_detected_repo(self, mock_es, mock_repo):

        """Function:  test_not_detected_repo

        Description:  Test with repository not detected.

        Arguments:

        """

        mock_es.return_value = self.els
        mock_repo.side_effect = [self.repo_dict, self.repo_dict2]

        els = elastic_class.ElasticSearchRepo(self.host_list, repo=self.repo,
                                              repo_dir=self.repo_dir)
        els.repo_name = None
        self.assertEqual(
            els.create_repo(self.repo3, self.repo_dir),
            (True,
             "ERROR:  Repository not detected:  reponame3, /dir/path/dump2"))

    @mock.patch("elastic_class.create_snapshot_repo",
                mock.Mock(return_value={"acknowledged": False}))
    @mock.patch("elastic_class.ElasticSearch.update_status",
                mock.Mock(return_value=True))
    @mock.patch("elastic_class.is_active", mock.Mock(return_value=True))
    @mock.patch("elastic_class.get_repo_list")
    @mock.patch("elastic_class.elasticsearch.Elasticsearch")
    def test_missing_repo_name(self, mock_es, mock_repo):

        """Function:  test_missing_repo_name

        Description:  Test with missing repo named.

        Arguments:

        """

        mock_es.return_value = self.els
        mock_repo.side_effect = [self.repo_dict, self.repo_dict2]

        els = elastic_class.ElasticSearchRepo(self.host_list, repo=self.repo,
                                              repo_dir=self.repo_dir)
        els.repo = None
        self.assertEqual(
            els.create_repo(repo_dir=self.repo_dir),
            (True,
             "ERROR: Missing repo name or" +
             " directory: 'None', '/dir/path/dump2'"))

    @mock.patch("elastic_class.create_snapshot_repo",
                mock.Mock(return_value={"acknowledged": True}))
    @mock.patch("elastic_class.ElasticSearch.update_status",
                mock.Mock(return_value=True))
    @mock.patch("elastic_class.is_active", mock.Mock(return_value=True))
    @mock.patch("elastic_class.get_repo_list")
    @mock.patch("elastic_class.elasticsearch.Elasticsearch")
    def test_no_repo_dir(self, mock_es, mock_repo):

        """Function:  test_no_repo_dir

        Description:  Test with no repo directory passed.

        Arguments:

        """

        mock_es.return_value = self.els
        mock_repo.side_effect = [self.repo_dict, self.repo_dict2]

        els = elastic_class.ElasticSearchRepo(self.host_list, repo=self.repo,
                                              repo_dir=self.repo_dir)
        self.assertEqual(els.create_repo(self.repo), (False, None))
        self.assertEqual(els.repo_dict, self.repo_dict2)

    @mock.patch("elastic_class.create_snapshot_repo",
                mock.Mock(return_value={"acknowledged": True}))
    @mock.patch("elastic_class.ElasticSearch.update_status",
                mock.Mock(return_value=True))
    @mock.patch("elastic_class.is_active", mock.Mock(return_value=True))
    @mock.patch("elastic_class.get_repo_list")
    @mock.patch("elastic_class.elasticsearch.Elasticsearch")
    def test_no_repo_name(self, mock_es, mock_repo):

        """Function:  test_no_repo_name

        Description:  Test with no repo named passed.

        Arguments:

        """

        mock_es.return_value = self.els
        mock_repo.side_effect = [self.repo_dict, self.repo_dict2]

        els = elastic_class.ElasticSearchRepo(self.host_list, repo=self.repo2,
                                              repo_dir=self.repo_dir)
        self.assertEqual(els.create_repo(repo_dir=self.repo_dir),
                         (False, None))
        self.assertEqual(els.repo_dict, self.repo_dict2)

    @mock.patch("elastic_class.create_snapshot_repo",
                mock.Mock(return_value={"acknowledged": True}))
    @mock.patch("elastic_class.ElasticSearch.update_status",
                mock.Mock(return_value=True))
    @mock.patch("elastic_class.is_active", mock.Mock(return_value=True))
    @mock.patch("elastic_class.get_repo_list")
    @mock.patch("elastic_class.elasticsearch.Elasticsearch")
    def test_default(self, mock_es, mock_repo):

        """Function:  test_default

        Description:  Test with default settings.

        Arguments:

        """

        mock_es.return_value = self.els
        mock_repo.side_effect = [self.repo_dict, self.repo_dict2]

        els = elastic_class.ElasticSearchRepo(self.host_list, repo=self.repo,
                                              repo_dir=self.repo_dir)
        self.assertEqual(els.create_repo(self.repo2, self.repo_dir),
                         (False, None))
        self.assertEqual(els.repo_dict, self.repo_dict2)


if __name__ == "__main__":
    unittest.main()
