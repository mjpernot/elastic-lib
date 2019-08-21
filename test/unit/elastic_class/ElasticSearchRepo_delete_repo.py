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


class Repo(object):

    """Class:  Repo

    Description:  Class representation of the snapshot class.

    Super-Class:  object

    Sub-Classes:

    Methods:
        get_repository -> Stub holder for snapshot.get_repository method.
        create_repository -> Stub holder for snapshot.create_repository method.
        delete_repository -> Stub holder for snapshot.delete_repository method.

    """

    def delete_repository(self, repository):

        """Method:  delete_repository

        Description:  Stub holder for snapshot.delete_repository method.

        Arguments:
            (input) repository -> Name of repository to delete.

        """

        return {"acknowledged": True}

    def create_repository(self):

        """Method:  create_repository

        Description:  Stub holder for snapshot.create_repository method.

        Arguments:

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
        self.es = Elasticsearch(self.host_list)
        self.err_msg = "ERROR:  Repository still detected:  reponame"

    @mock.patch("elastic_class.elasticsearch.Elasticsearch")
    def test_not_deleted(self, mock_es):

        """Function:  test_not_deleted

        Description:  Test with repository not being deleted.

        Arguments:

        """

        mock_es.return_value = self.es

        es = elastic_class.ElasticSearchRepo(self.host_list, repo=self.repo)

        self.assertEqual(es.delete_repo(self.repo), (True, self.err_msg))

    @mock.patch("elastic_class.elasticsearch.Elasticsearch")
    def test_default(self, mock_es):

        """Function:  test_default

        Description:  Test with default settings.

        Arguments:

        """

        mock_es.return_value = self.es

        es = elastic_class.ElasticSearchRepo(self.host_list, repo=self.repo)
        es.repo_dict = {"reponame":
                        {"type": "dbdump", "settings":
                         {"location": "/dir/path/dump"}},
                        "reponame2":
                        {"type": "dbdump", "settings":
                         {"location": "/dir/path/dump2"}}}

        self.assertEqual(es.delete_repo(self.repo2), (False, None))


if __name__ == "__main__":
    unittest.main()
