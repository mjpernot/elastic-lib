# Classification (U)

"""Program:  elasticsearch_get_dump_list.py

    Description:  Unit testing of get_dump_list in elastic_class.ElasticSearch
        class.

    Usage:
        test/unit/elastic_class/elasticsearch_get_dump_list.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import unittest
import elasticsearch
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
        __init__
        get

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.repository = None
        self.ignore_unavailable = None
        self.snapshot = None

    def get(self, repository, snapshot, ignore_unavailable):

        """Method:  get

        Description:  Stub holder for snapshot.get method.

        Arguments:

        """

        self.repository = repository
        self.snapshot = snapshot
        self.ignore_unavailable = ignore_unavailable

        raise elasticsearch.exceptions.NotFoundError(   # pylint:disable=E1120
            'holder', 'holder')


class Elasticsearch2():                                 # pylint:disable=R0903

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
        self.snapshot = Repo2()


class Repo():                                           # pylint:disable=R0903

    """Class:  Repo

    Description:  Class representation of the snapshot class.

    Methods:
        __init__
        get

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.repository = None
        self.ignore_unavailable = None
        self.snapshots = {"snapshots": [{"repo": "repo1"}]}
        self.snapshots2 = {"snapshots": [{"repo": "repo1"}, {"repo": "repo2"}]}

    def get(self, repository, snapshot, ignore_unavailable):

        """Method:  get

        Description:  Stub holder for snapshot.get method.

        Arguments:

        """

        self.repository = repository
        self.ignore_unavailable = ignore_unavailable

        if snapshot == "_all":
            return self.snapshots2

        return self.snapshots


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
        self.snapshot = Repo()


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_raise_error2
        test_raise_error
        test_without_name2
        test_without_name
        test_with_name2
        test_with_name

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.host_list = ["host1", "host2"]
        self.repo = "reponame"
        self.els = Elasticsearch(self.host_list)
        self.results = [{"repo": "repo1"}]
        self.results2 = [{"repo": "repo1"}, {"repo": "repo2"}]
        self.name = "repo1"
        self.els2 = Elasticsearch2(self.host_list)
        self.err = "Failed to find snapshot: '_all' in repository: 'reponame'"

    @unittest.skip("Error:  Unable to raise exception.  Need to investigate.")
    @mock.patch("elastic_class.is_active", mock.Mock(return_value=False))
    @mock.patch("elastic_class.ElasticSearch.update_status",
                mock.Mock(return_value=True))
    @mock.patch("elastic_class.elasticsearch.Elasticsearch")
    def test_raise_error2(self, mock_es):

        """Function:  test_raise_error2

        Description:  Test with exception raised.

        Arguments:

        """

        mock_es.return_value = self.els
        els = elastic_class.ElasticSearch(self.host_list)
        els.connect()
        data = els2.get_dump_list(repo=self.repo)

        self.assertEqual((data[1], data[2]), (False, self.err))

    @unittest.skip("Error:  Unable to raise exception.  Need to investigate.")
    @mock.patch("elastic_class.is_active", mock.Mock(return_value=False))
    @mock.patch("elastic_class.ElasticSearch.update_status",
                mock.Mock(return_value=True))
    @mock.patch("elastic_class.elasticsearch.Elasticsearch")
    def test_raise_error(self, mock_es):

        """Function:  test_raise_error

        Description:  Test with exception raised.

        Arguments:

        """

        mock_es.return_value = self.els
        els = elastic_class.ElasticSearch(self.host_list)
        els.connect()
        data = els2.get_dump_list(repo=self.repo)

        self.assertEqual(data[0], [])

    @mock.patch("elastic_class.is_active", mock.Mock(return_value=False))
    @mock.patch("elastic_class.ElasticSearch.update_status",
                mock.Mock(return_value=True))
    @mock.patch("elastic_class.elasticsearch.Elasticsearch")
    def test_without_name2(self, mock_es):

        """Function:  test_without_name2

        Description:  Test with no snapshot name passed.

        Arguments:

        """

        mock_es.return_value = self.els
        els = elastic_class.ElasticSearch(self.host_list)
        els.connect()
        data = els.get_dump_list(repo=self.repo)

        self.assertEqual((data[1], data[2]), (True, None))

    @mock.patch("elastic_class.is_active", mock.Mock(return_value=False))
    @mock.patch("elastic_class.ElasticSearch.update_status",
                mock.Mock(return_value=True))
    @mock.patch("elastic_class.elasticsearch.Elasticsearch")
    def test_without_name(self, mock_es):

        """Function:  test_without_name

        Description:  Test with no snapshot name passed.

        Arguments:

        """

        mock_es.return_value = self.els
        els = elastic_class.ElasticSearch(self.host_list)
        els.connect()
        data = els.get_dump_list(repo=self.repo)[0]

        self.assertEqual(data, self.results2)

    @mock.patch("elastic_class.is_active", mock.Mock(return_value=False))
    @mock.patch("elastic_class.ElasticSearch.update_status",
                mock.Mock(return_value=True))
    @mock.patch("elastic_class.elasticsearch.Elasticsearch")
    def test_with_name2(self, mock_es):

        """Function:  test_with_name2

        Description:  Test with snapshot name passed.

        Arguments:

        """

        mock_es.return_value = self.els
        els = elastic_class.ElasticSearch(self.host_list)
        els.connect()
        data = els.get_dump_list(repo=self.repo, snapshot=self.name)

        self.assertEqual((data[1], data[2]), (True, None))

    @mock.patch("elastic_class.is_active", mock.Mock(return_value=False))
    @mock.patch("elastic_class.ElasticSearch.update_status",
                mock.Mock(return_value=True))
    @mock.patch("elastic_class.elasticsearch.Elasticsearch")
    def test_with_name(self, mock_es):

        """Function:  test_with_name

        Description:  Test with snapshot name passed.

        Arguments:

        """

        mock_es.return_value = self.els
        els = elastic_class.ElasticSearch(self.host_list)
        els.connect()
        data = els.get_dump_list(repo=self.repo, snapshot=self.name)[0]

        self.assertEqual(data, self.results)


if __name__ == "__main__":
    unittest.main()
