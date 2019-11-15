#!/usr/bin/python
# Classification (U)

"""Program:  ElasticSearchRepo_delete_repo.py

    Description:  Unit testing of delete_repo in
        elastic_class.ElasticSearchRepo class.

    Usage:
        test/unit/elastic_class/ElasticSearchRepo_delete_repo.py

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


class Elasticsearch(object):

    """Class:  ElasticSearch

    Description:  Class representation of the Elasticsearch class.

    Methods:
        __init__ -> Initialize configuration environment.

    """

    def __init__(self, host_list, port=9200):

        """Method:  __init__

        Description:  Initialization instance of the class.

        Arguments:

        """

        self.hosts = host_list
        self.port = port
        self.ping_status = True
        self.info_status = {"cluster_name":
                            "ClusterName", "name": "servername"}


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Initialization for unit testing.
        test_repo_name_failed -> Test with repo name failed to delete.
        test_repo_name_none -> Test with repo name set to None.
        test_no_repo_name -> Test with no repo name passed.
        test_not_deleted -> Test with repository not being deleted.
        test_default -> Test with default settings.

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
        self.es = Elasticsearch(self.host_list)
        self.err_msg = "ERROR:  Repository still detected:  reponame"
        self.repo_dict = {"reponame": {"type": "dbdump", "settings":
                                       {"location": "/dir/path/dump"}},
                          "reponame2": {"type": "dbdump", "settings":
                                        {"location": "/dir/path/dump2"}}}
        self.repo_dict2 = {"reponame": {"type": "dbdump", "settings":
                                        {"location": "/dir/path/dump"}}}
        self.repo_dict3 = {"reponame2": {"type": "dbdump", "settings":
                                         {"location": "/dir/path/dump2"}}}

    @mock.patch("elastic_class.ElasticSearch.update_status",
                mock.Mock(return_value=True))
    @mock.patch("elastic_class.is_active", mock.Mock(return_value=True))
    @mock.patch("elastic_class.delete_snapshot_repo",
                mock.Mock(return_value={"acknowledged": False}))
    @mock.patch("elastic_class.get_repo_list")
    @mock.patch("elastic_class.elasticsearch.Elasticsearch")
    def test_repo_name_failed(self, mock_es, mock_repo):

        """Function:  test_repo_name_failed

        Description:  Test with repo name failed to delete.

        Arguments:

        """

        mock_es.return_value = self.es
        mock_repo.side_effect = [self.repo_dict, self.repo_dict]

        es = elastic_class.ElasticSearchRepo(self.host_list, repo=self.repo)
        es.repo_dict[self.repo] = True

        self.assertEqual(
            es.delete_repo(self.repo),
            (True, "ERROR:  Repository deletion failed:  reponame"))

    @mock.patch("elastic_class.ElasticSearch.update_status",
                mock.Mock(return_value=True))
    @mock.patch("elastic_class.is_active", mock.Mock(return_value=True))
    @mock.patch("elastic_class.delete_snapshot_repo",
                mock.Mock(return_value={"acknowledged": True}))
    @mock.patch("elastic_class.get_repo_list")
    @mock.patch("elastic_class.elasticsearch.Elasticsearch")
    def test_repo_name_none(self, mock_es, mock_repo):

        """Function:  test_repo_name_none

        Description:  Test with repo name set to None.

        Arguments:

        """

        mock_es.return_value = self.es
        mock_repo.side_effect = [self.repo_dict, self.repo_dict3]

        es = elastic_class.ElasticSearchRepo(self.host_list, repo=self.repo)
        es.repo = None

        self.assertEqual(
            es.delete_repo(),
            (True, "ERROR: Missing repo or does not exist: None"))

    @mock.patch("elastic_class.ElasticSearch.update_status",
                mock.Mock(return_value=True))
    @mock.patch("elastic_class.is_active", mock.Mock(return_value=True))
    @mock.patch("elastic_class.delete_snapshot_repo",
                mock.Mock(return_value={"acknowledged": True}))
    @mock.patch("elastic_class.get_repo_list")
    @mock.patch("elastic_class.elasticsearch.Elasticsearch")
    def test_no_repo_name(self, mock_es, mock_repo):

        """Function:  test_no_repo_name

        Description:  Test with no repo name passed.

        Arguments:

        """

        mock_es.return_value = self.es
        mock_repo.side_effect = [self.repo_dict, self.repo_dict3]

        es = elastic_class.ElasticSearchRepo(self.host_list, repo=self.repo)

        self.assertEqual(es.delete_repo(), (False, None))
        self.assertEqual(es.repo_dict, self.repo_dict3)

    @mock.patch("elastic_class.ElasticSearch.update_status",
                mock.Mock(return_value=True))
    @mock.patch("elastic_class.is_active", mock.Mock(return_value=True))
    @mock.patch("elastic_class.delete_snapshot_repo",
                mock.Mock(return_value={"acknowledged": True}))
    @mock.patch("elastic_class.get_repo_list")
    @mock.patch("elastic_class.elasticsearch.Elasticsearch")
    def test_not_deleted(self, mock_es, mock_repo):

        """Function:  test_not_deleted

        Description:  Test with repository not being deleted.

        Arguments:

        """

        mock_es.return_value = self.es
        mock_repo.side_effect = [self.repo_dict, self.repo_dict]

        es = elastic_class.ElasticSearchRepo(self.host_list, repo=self.repo)

        self.assertEqual(es.delete_repo(self.repo), (True, self.err_msg))
        self.assertEqual(es.repo_dict, self.repo_dict)

    @mock.patch("elastic_class.ElasticSearch.update_status",
                mock.Mock(return_value=True))
    @mock.patch("elastic_class.is_active", mock.Mock(return_value=True))
    @mock.patch("elastic_class.delete_snapshot_repo",
                mock.Mock(return_value={"acknowledged": True}))
    @mock.patch("elastic_class.get_repo_list")
    @mock.patch("elastic_class.elasticsearch.Elasticsearch")
    def test_default(self, mock_es, mock_repo):

        """Function:  test_default

        Description:  Test with default settings.

        Arguments:

        """

        mock_es.return_value = self.es
        mock_repo.side_effect = [self.repo_dict, self.repo_dict2]

        es = elastic_class.ElasticSearchRepo(self.host_list, repo=self.repo)

        self.assertEqual(es.delete_repo(self.repo2), (False, None))
        self.assertEqual(es.repo_dict, self.repo_dict2)


if __name__ == "__main__":
    unittest.main()
