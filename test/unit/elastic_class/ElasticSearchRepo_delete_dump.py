#!/usr/bin/python
# Classification (U)

"""Program:  ElasticSearchRepo_delete_dump.py

    Description:  Unit testing of delete_dump in
        elastic_class.ElasticSearchRepo class.

    Usage:
        test/unit/elastic_class/ElasticSearchRepo_delete_dump.py

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
        self.info_status = {"cluster_name": "ClusterName",
                            "name": "servername"}


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Initialization for unit testing.
        test_repo_name_none -> Test with repo name set to None.
        test_no_dump -> Test with no dump to delete.
        test_dump_detected -> Test with dump detected after delete.
        test_delete_failed -> Test with delete of dump failing.
        test_no_repo_name -> Test with no repo name passed.
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
        self.es = Elasticsearch(self.host_list)
        self.dump_name = "dump3"
        self.repo_dict = {"reponame": {"type": "dbdump", "settings":
            {"location": "/dir/path/dump"}}}

    @mock.patch("elastic_class.delete_snapshot",
                mock.Mock(return_value={"acknowledged": False}))
    @mock.patch("elastic_class.ElasticSearch.update_status",
                mock.Mock(return_value=True))
    @mock.patch("elastic_class.is_active", mock.Mock(return_value=True))
    @mock.patch("elastic_class.get_repo_list")
    @mock.patch("elastic_class.get_dump_list")
    @mock.patch("elastic_class.elasticsearch.Elasticsearch")
    def test_repo_name_none(self, mock_es, mock_list, mock_repo):

        """Function:  test_repo_name_none

        Description:  Test with repo name set to None.

        Arguments:

        """

        mock_es.return_value = self.es
        mock_list.side_effect = [[["dump1"], ["dump2"], ["dump3"]],
                                 [["dump1"], ["dump2"]]]
        mock_repo.return_value = self.repo_dict

        es = elastic_class.ElasticSearchRepo(self.host_list, repo=self.repo)
        es.repo = None
        self.assertEqual(es.delete_dump(dump_name=self.dump_name),
            (True,
             "ERROR: Missing arg/repo not exist, Repo: None, Dump: dump3"))

    @mock.patch("elastic_class.delete_snapshot",
                mock.Mock(return_value={"acknowledged": False}))
    @mock.patch("elastic_class.ElasticSearch.update_status",
                mock.Mock(return_value=True))
    @mock.patch("elastic_class.is_active", mock.Mock(return_value=True))
    @mock.patch("elastic_class.get_repo_list")
    @mock.patch("elastic_class.get_dump_list")
    @mock.patch("elastic_class.elasticsearch.Elasticsearch")
    def test_no_dump(self, mock_es, mock_list, mock_repo):

        """Function:  test_no_dump

        Description:  Test with no dump to delete.

        Arguments:

        """

        mock_es.return_value = self.es
        mock_list.side_effect = [[["dump1"], ["dump2"]],
                                 [["dump1"], ["dump2"]]]
        mock_repo.return_value = self.repo_dict

        es = elastic_class.ElasticSearchRepo(self.host_list, repo=self.repo)
        self.assertEqual(es.delete_dump(self.repo, self.dump_name),
            (True, "ERROR: Dump: dump3 not in Repository: reponame"))

    @mock.patch("elastic_class.delete_snapshot",
                mock.Mock(return_value={"acknowledged": True}))
    @mock.patch("elastic_class.ElasticSearch.update_status",
                mock.Mock(return_value=True))
    @mock.patch("elastic_class.is_active", mock.Mock(return_value=True))
    @mock.patch("elastic_class.get_repo_list")
    @mock.patch("elastic_class.get_dump_list")
    @mock.patch("elastic_class.elasticsearch.Elasticsearch")
    def test_dump_detected(self, mock_es, mock_list, mock_repo):

        """Function:  test_dump_detected

        Description:  Test with dump detected after delete.

        Arguments:

        """

        mock_es.return_value = self.es
        mock_list.side_effect = [[["dump1"], ["dump2"], ["dump3"]],
                                 [["dump1"], ["dump2"], ["dump3"]]]
        mock_repo.return_value = self.repo_dict

        es = elastic_class.ElasticSearchRepo(self.host_list, repo=self.repo)
        self.assertEqual(es.delete_dump(self.repo, self.dump_name),
            (True, "ERROR: Dump still detected: reponame, dump3"))

    @mock.patch("elastic_class.delete_snapshot",
                mock.Mock(return_value={"acknowledged": False}))
    @mock.patch("elastic_class.ElasticSearch.update_status",
                mock.Mock(return_value=True))
    @mock.patch("elastic_class.is_active", mock.Mock(return_value=True))
    @mock.patch("elastic_class.get_repo_list")
    @mock.patch("elastic_class.get_dump_list")
    @mock.patch("elastic_class.elasticsearch.Elasticsearch")
    def test_delete_failed(self, mock_es, mock_list, mock_repo):

        """Function:  test_delete_failed

        Description:  Test with delete of dump failing.

        Arguments:

        """

        mock_es.return_value = self.es
        mock_list.side_effect = [[["dump1"], ["dump2"], ["dump3"]],
                                 [["dump1"], ["dump2"]]]
        mock_repo.return_value = self.repo_dict

        es = elastic_class.ElasticSearchRepo(self.host_list, repo=self.repo)
        es.repo_dict[self.repo2] = True
        self.assertEqual(es.delete_dump(self.repo2, self.dump_name),
            (True, "ERROR:  Dump deletion failed:  reponame2, dump3"))

    @mock.patch("elastic_class.delete_snapshot",
                mock.Mock(return_value={"acknowledged": True}))
    @mock.patch("elastic_class.ElasticSearch.update_status",
                mock.Mock(return_value=True))
    @mock.patch("elastic_class.is_active", mock.Mock(return_value=True))
    @mock.patch("elastic_class.get_repo_list")
    @mock.patch("elastic_class.get_dump_list")
    @mock.patch("elastic_class.elasticsearch.Elasticsearch")
    def test_no_repo_name(self, mock_es, mock_list, mock_repo):

        """Function:  test_no_repo_name

        Description:  Test with no repo name passed.

        Arguments:

        """

        mock_es.return_value = self.es
        mock_list.side_effect = [[["dump1"], ["dump2"], ["dump3"]],
                                 [["dump1"], ["dump2"]]]
        mock_repo.return_value = self.repo_dict

        es = elastic_class.ElasticSearchRepo(self.host_list, repo=self.repo)
        self.assertEqual(es.delete_dump(dump_name=self.dump_name),
                         (False, None))

    @mock.patch("elastic_class.delete_snapshot",
                mock.Mock(return_value={"acknowledged": True}))
    @mock.patch("elastic_class.ElasticSearch.update_status",
                mock.Mock(return_value=True))
    @mock.patch("elastic_class.is_active", mock.Mock(return_value=True))
    @mock.patch("elastic_class.get_repo_list")
    @mock.patch("elastic_class.get_dump_list")
    @mock.patch("elastic_class.elasticsearch.Elasticsearch")
    def test_default(self, mock_es, mock_list, mock_repo):

        """Function:  test_default

        Description:  Test with default settings.

        Arguments:

        """

        mock_es.return_value = self.es
        mock_list.side_effect = [[["dump1"], ["dump2"], ["dump3"]],
                                 [["dump1"], ["dump2"]]]
        mock_repo.return_value = self.repo_dict

        es = elastic_class.ElasticSearchRepo(self.host_list, repo=self.repo)
        self.assertEqual(es.delete_dump(self.repo, self.dump_name),
                         (False, None))


if __name__ == "__main__":
    unittest.main()
