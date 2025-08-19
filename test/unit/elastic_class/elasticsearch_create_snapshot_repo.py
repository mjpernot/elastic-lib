# Classification (U)

"""Program:  elasticsearch_create_snapshot_repo.py

    Description:  Unit testing of create_snapshot_repo in
        elastic_class.ElasticSearch class.

    Usage:
        test/unit/elastic_class/elasticsearch_create_snapshot_repo.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import unittest
import mock
import elasticsearch

# Local
sys.path.append(os.getcwd())
import elastic_class                            # pylint:disable=E0401,C0413
import version                                  # pylint:disable=E0401,C0413

__version__ = version.__version__


class Repo():                                           # pylint:disable=R0903

    """Class:  Repo

    Description:  Class representation of the snapshot class.

    Methods:
        __init__
        create_repository

    """

    def __init__(self):

        """Method:  __init__

        Description:  Initialization of class.

        Arguments:

        """

        self.name = None
        self.body = None
        self.verify = None
        self.settings = None
        self.type = None

    def create_repository(self, name, verify, **body):

        """Method:  create_repository

        Description:  Stub for snapshot.create_repository method.

        Arguments:

        """

        self.name = name
        self.type = body["type"]
        self.settings = body["settings"]
        self.verify = verify

        return {"acknowledged": True}


class Repo2():                                          # pylint:disable=R0903

    """Class:  Repo2

    Description:  Class representation of the snapshot class.

    Methods:
        __init__
        create_repository

    """

    def __init__(self):

        """Method:  __init__

        Description:  Initialization of class.

        Arguments:

        """

        self.repository = None
        self.body = None
        self.verify = None

    def create_repository(self, repository, body, verify):

        """Method:  create_repository

        Description:  Stub for snapshot.create_repository method.

        Arguments:

        """

        self.repository = repository
        self.body = body
        self.verify = verify

        return {"acknowledged": True}


class Elasticsearch():                                  # pylint:disable=R0903

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

        if elasticsearch.__version__ >= (8, 0, 0):
            self.snapshot = Repo()

        else:
            self.snapshot = Repo2()

        self.results = {"acknowledged": True}


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_default

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.host_list = ["host1", "host2"]
        self.repo_name = "reponame"
        self.body = {
            "type": "fs", "settings": {
                "location": "repo_dir", "compress": True}}
        self.els = Elasticsearch(self.host_list)
        self.results = {"acknowledged": True}

    @mock.patch("elastic_class.is_active", mock.Mock(return_value=False))
    @mock.patch("elastic_class.ElasticSearch.update_status",
                mock.Mock(return_value=True))
    @mock.patch("elastic_class.elasticsearch.Elasticsearch")
    def test_default(self, mock_es):

        """Function:  test_default

        Description:  Test with default settings.

        Arguments:

        """

        mock_es.return_value = self.els
        els = elastic_class.ElasticSearch(self.host_list)
        els.connect()

        self.assertEqual(
            els.create_snapshot_repo(
                self.repo_name, self.body, True), self.results)


if __name__ == "__main__":
    unittest.main()
