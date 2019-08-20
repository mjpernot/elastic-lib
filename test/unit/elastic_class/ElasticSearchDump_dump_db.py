#!/usr/bin/python
# Classification (U)

"""Program:  ElasticSearchDump_dump_db.py

    Description:  Unit testing of dump_db in elastic_class.ElasticSearchDump.

    Usage:
        test/unit/elastic_class/ElasticSearchDump_dump_db.py

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
        create -> Stub holder for snapshot.create method.

    """

    def get_repository(self):

        """Method:  get_repository

        Description:  Stub holder for snapshot.get_repository method.

        Arguments:

        """

        return {"reponame": {"type": "dbdump", "settings":
                             {"location": "/dir/path/dump"}}}

    def create(self, repository, body, snapshot):

        """Method:  create

        Description:  Stub holder for snapshot.create method.

        Arguments:
            (input) repository -> Repository name.
            (input) body -> Database dump command.
            (input) snapshot -> Database dump respository information.

        """

        return True


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
        test_ping_true -> Test ping of Elasticsearch server is True.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.host_list = ["host1", "host2"]
        self.host_str = "host1, host2"
        self.repo = "reponame"
        self.es = Elasticsearch(self.host_list)
        self.dbs = "dbname"

    @mock.patch("elastic_class.ElasticSearchDump._chk_status")
    @mock.patch("elastic_libs.get_latest_dump")
    @mock.patch("elastic_class.get_dump_list")
    @mock.patch("elastic_class.elasticsearch.Elasticsearch")
    def test_ping_true(self, mock_es, mock_list, mock_latest, mock_chk):

        """Function:  test_ping_true

        Description:  Test ping of Elasticsearch server is True.

        Arguments:

        """

        mock_es.return_value = self.es
        mock_list.side_effect = [["dump1", "dump2"],
                                 ["dump1", "dump2", "dump3"]]
        mock_latest.side_effect = ["dump2", "dump3"]
        mock_chk.return_value = (False, None, True)

        es = elastic_class.ElasticSearchDump(self.host_list, repo=self.repo)
        self.assertEqual(es.dump_db(self.dbs), (False, None))

        #self.assertEqual((es.port, es.hosts), (9200, self.host_list))


if __name__ == "__main__":
    unittest.main()
