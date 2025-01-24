# Classification (U)

"""Program:  elasticsearchrepo_init.py

    Description:  Unit testing of __init__ in elastic_class.ElasticSearchRepo
        class.

    Usage:
        test/unit/elastic_class/elasticsearchrepo_init.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import unittest
import mock

# Local
sys.path.append(os.getcwd())
import elastic_class                            # pylint:disable=E0401,C0413
import version                                  # pylint:disable=E0401,C0413

__version__ = version.__version__


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
        self.ping_status = True
        self.info_status = {"cluster_name":
                            "ClusterName", "name": "servername"}


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
        self.repo = "reponame"
        self.els = Elasticsearch(self.host_list)
        self.repo_dir = "/dir/path/repo"

    @mock.patch("elastic_class.ElasticSearch.update_status",
                mock.Mock(return_value=True))
    def test_default(self):

        """Function:  test_default

        Description:  Test with default settings.

        Arguments:

        """

        els = elastic_class.ElasticSearchRepo(self.host_list, repo=self.repo,
                                              repo_dir=self.repo_dir)

        self.assertEqual((els.hosts, els.repo, els.repo_dir),
                         (self.host_list, self.repo, self.repo_dir))


if __name__ == "__main__":
    unittest.main()
