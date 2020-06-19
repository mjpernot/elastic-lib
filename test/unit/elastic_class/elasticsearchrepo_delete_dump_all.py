#!/usr/bin/python
# Classification (U)

"""Program:  elasticsearchrepo_delete_dump_all.py

    Description:  Unit testing of delete_dump_all in
        elastic_class.ElasticSearchRepo class.

    Usage:
        test/unit/elastic_class/elasticsearchrepo_delete_dump_all.py

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
        test_delete_dump_fails -> Test with delete dumps fails.
        test_repo_name_none -> Test with repo name set to none.
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
        self.els = Elasticsearch(self.host_list)
        self.repo_dict = {"reponame": {"type": "dbdump", "settings":
                                       {"location": "/dir/path/dump"}}}

    @mock.patch("elastic_class.ElasticSearch.update_status",
                mock.Mock(return_value=True))
    @mock.patch("elastic_class.is_active", mock.Mock(return_value=True))
    @mock.patch("elastic_class.ElasticSearchRepo.delete_dump",
                mock.Mock(return_value=(True, "Error Message")))
    @mock.patch("elastic_class.get_repo_list")
    @mock.patch("elastic_class.get_dump_list")
    @mock.patch("elastic_class.elasticsearch.Elasticsearch")
    def test_delete_dump_fails(self, mock_es, mock_list, mock_repo):

        """Function:  test_delete_dump_fails

        Description:  Test with delete dumps fails.

        Arguments:

        """

        mock_es.return_value = self.els
        mock_list.side_effect = [["dump1", "dump2", "dump3"],
                                 ["dump1", "dump2"]]
        mock_repo.return_value = self.repo_dict

        els = elastic_class.ElasticSearchRepo(self.host_list, repo=self.repo)

        self.assertEqual(els.delete_dump_all(self.repo),
                         (True, "Error Message"))

    @mock.patch("elastic_class.ElasticSearch.update_status",
                mock.Mock(return_value=True))
    @mock.patch("elastic_class.is_active", mock.Mock(return_value=True))
    @mock.patch("elastic_class.ElasticSearchRepo.delete_dump",
                mock.Mock(return_value=(True, "Error Message")))
    @mock.patch("elastic_class.get_repo_list")
    @mock.patch("elastic_class.get_dump_list")
    @mock.patch("elastic_class.elasticsearch.Elasticsearch")
    def test_repo_name_none(self, mock_es, mock_list, mock_repo):

        """Function:  test_repo_name_none

        Description:  Test with repo name set to none.

        Arguments:

        """

        mock_es.return_value = self.els
        mock_list.side_effect = [["dump1", "dump2", "dump3"],
                                 ["dump1", "dump2"]]
        mock_repo.return_value = self.repo_dict

        els = elastic_class.ElasticSearchRepo(self.host_list, repo=self.repo)
        els.repo = None

        self.assertEqual(
            els.delete_dump_all(),
            (True, "ERROR:  Repo:  None is not present or missing argument."))

    @mock.patch("elastic_class.ElasticSearch.update_status",
                mock.Mock(return_value=True))
    @mock.patch("elastic_class.is_active", mock.Mock(return_value=True))
    @mock.patch("elastic_class.ElasticSearchRepo.delete_dump",
                mock.Mock(return_value=(False, None)))
    @mock.patch("elastic_class.get_repo_list")
    @mock.patch("elastic_class.get_dump_list")
    @mock.patch("elastic_class.elasticsearch.Elasticsearch")
    def test_no_repo_name(self, mock_es, mock_list, mock_repo):

        """Function:  test_no_repo_name

        Description:  Test with no repo name passed.

        Arguments:

        """

        mock_es.return_value = self.els
        mock_list.side_effect = [["dump1", "dump2", "dump3"],
                                 ["dump1", "dump2"]]
        mock_repo.return_value = self.repo_dict

        els = elastic_class.ElasticSearchRepo(self.host_list, repo=self.repo)

        self.assertEqual(els.delete_dump_all(), (False, None))

    @mock.patch("elastic_class.ElasticSearch.update_status",
                mock.Mock(return_value=True))
    @mock.patch("elastic_class.is_active", mock.Mock(return_value=True))
    @mock.patch("elastic_class.ElasticSearchRepo.delete_dump",
                mock.Mock(return_value=(False, None)))
    @mock.patch("elastic_class.get_repo_list")
    @mock.patch("elastic_class.get_dump_list")
    @mock.patch("elastic_class.elasticsearch.Elasticsearch")
    def test_default(self, mock_es, mock_list, mock_repo):

        """Function:  test_default

        Description:  Test with default settings.

        Arguments:

        """

        mock_es.return_value = self.els
        mock_list.side_effect = [["dump1", "dump2", "dump3"],
                                 ["dump1", "dump2"]]
        mock_repo.return_value = self.repo_dict

        els = elastic_class.ElasticSearchRepo(self.host_list, repo=self.repo)

        self.assertEqual(els.delete_dump_all(self.repo), (False, None))


if __name__ == "__main__":
    unittest.main()
