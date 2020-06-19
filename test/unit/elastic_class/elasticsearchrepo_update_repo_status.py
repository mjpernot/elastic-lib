#!/usr/bin/python
# Classification (U)

"""Program:  elasticsearchrepo_update_repo_status.py

    Description:  Unit testing of update_repo_status in
        elastic_class.ElasticSearchDump.

    Usage:
        test/unit/elastic_class/elasticsearchrepo_update_repo_status.py

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
        test_repo_not_active -> Test with Elasticsearch not active.
        test_default -> Test with default settings.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.host_list = ["host1", "host2"]
        self.host_str = "host1, host2"
        self.repo = "reponame"
        self.els = Elasticsearch(self.host_list)
        self.repo_dict = {"reponame": {"type": "dbdump", "settings":
                                       {"location": "/dir/path/dump"}}}

    @mock.patch("elastic_class.ElasticSearch.update_status",
                mock.Mock(return_value=True))
    @mock.patch("elastic_class.is_active", mock.Mock(return_value=False))
    @mock.patch("elastic_class.elasticsearch.Elasticsearch")
    def test_repo_not_active(self, mock_es):

        """Function:  test_repo_not_active

        Description:  Test with Elasticsearch not active.

        Arguments:

        """

        mock_es.return_value = self.els

        els = elastic_class.ElasticSearchRepo(self.host_list, repo=self.repo)
        self.assertEqual((els.hosts, els.repo, els.repo_dict),
                         (self.host_list, self.repo, {}))

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
        mock_repo.return_value = self.repo_dict

        els = elastic_class.ElasticSearchRepo(self.host_list, repo=self.repo)
        self.assertEqual((els.hosts, els.repo, els.repo_dict),
                         (self.host_list, self.repo, self.repo_dict))


if __name__ == "__main__":
    unittest.main()
