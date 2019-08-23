#!/usr/bin/python
# Classification (U)

"""Program:  ElasticSearchRepo_create_repo.py

    Description:  Unit testing of create_repo in
        elastic_class.ElasticSearchRepo class.

    Usage:
        test/unit/elastic_class/ElasticSearchRepo_create_repo.py

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


class Repo(object):

    """Class:  Repo

    Description:  Class representation of the snapshot class.

    Super-Class:  object

    Sub-Classes:

    Methods:
        get_repository -> Stub holder for snapshot.get_repository method.
        create_repository -> Stub holder for snapshot.create_repository method.

    """

    def create_repository(self, repository, body, verify):

        """Method:  create_repository

        Description:  Stub holder for snapshot.create_repository method.

        Arguments:
            (input) repository -> Name of repository to create.
            (input) body -> Command for create.
            (input) verify -> True|False - Validate creation.

        """

        return {"acknowledged": True}

    def get_repository(self):

        """Method:  get_repository

        Description:  Stub holder for snapshot.get_repository method.

        Arguments:

        """

        return {"reponame": {"type": "dbdump", "settings":
                             {"location": "/dir/path/dump"}}}


class Elasticsearch(object):

    """Class:  ElasticSearch

    Description:  Class representation of the Elasticsearch class.

    Super-Class:  object

    Sub-Classes:

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

    Super-Class:  unittest.TestCase

    Sub-Classes:

    Methods:
        setUp -> Initialization for unit testing.
        test_not_created_repo -> Test with repository not created.
        test_missing_repo_name -> Test with missing repo named.
        test_no_repo_dir -> Test with no repo directory passed.
        test_no_repo_name -> Test with no repo named passed.
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
        self.repo_dir = "/dir/path/repo"

    @mock.patch("elastic_class.elasticsearch.Elasticsearch")
    def test_not_created_repo(self, mock_es):

        """Function:  test_not_created_repo

        Description:  Test with repository not created.

        Arguments:

        """

        mock_es.return_value = self.es

        es = elastic_class.ElasticSearchRepo(self.host_list, repo=self.repo,
                                             repo_dir=self.repo_dir)
        es.repo_name = None

        self.assertEqual(es.create_repo(self.repo2, self.repo_dir),
            (True,
            "ERROR:  Repository not detected:  reponame2, '/dir/path/repo'"))

    @mock.patch("elastic_class.elasticsearch.Elasticsearch")
    def test_missing_repo_name(self, mock_es):

        """Function:  test_missing_repo_name

        Description:  Test with missing repo named.

        Arguments:

        """

        mock_es.return_value = self.es

        es = elastic_class.ElasticSearchRepo(self.host_list, repo=self.repo,
                                             repo_dir=self.repo_dir)
        es.repo_name = None

        self.assertEqual(es.create_repo(repo_dir=self.repo_dir),
            (True,
            "ERROR: Missing repo name or directory: None, '/dir/path/repo'"))

    @mock.patch("elastic_class.elasticsearch.Elasticsearch")
    def test_no_repo_dir(self, mock_es):

        """Function:  test_no_repo_dir

        Description:  Test with no repo directory passed.

        Arguments:

        """

        mock_es.return_value = self.es

        es = elastic_class.ElasticSearchRepo(self.host_list, repo=self.repo,
                                             repo_dir=self.repo_dir)

        self.assertEqual(es.create_repo(self.repo), (False, None))

    @mock.patch("elastic_class.elasticsearch.Elasticsearch")
    def test_no_repo_name(self, mock_es):

        """Function:  test_no_repo_name

        Description:  Test with no repo named passed.

        Arguments:

        """

        mock_es.return_value = self.es

        es = elastic_class.ElasticSearchRepo(self.host_list, repo=self.repo,
                                             repo_dir=self.repo_dir)

        self.assertEqual(es.create_repo(repo_dir=self.repo_dir),
                         (False, None))

    @mock.patch("elastic_class.elasticsearch.Elasticsearch")
    def test_default(self, mock_es):

        """Function:  test_default

        Description:  Test with default settings.

        Arguments:

        """

        mock_es.return_value = self.es

        es = elastic_class.ElasticSearchRepo(self.host_list, repo=self.repo,
                                             repo_dir=self.repo_dir)

        self.assertEqual(es.create_repo(self.repo, self.repo_dir),
                         (False, None))


if __name__ == "__main__":
    unittest.main()
