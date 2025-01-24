# Classification (U)

"""Program:  get_disks.py

    Description:  Unit testing of get_disks in elastic_class class.

    Usage:
        test/unit/elastic_class/get_disks.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import unittest

# Local
sys.path.append(os.getcwd())
import elastic_class                            # pylint:disable=E0401,C0413
import version                                  # pylint:disable=E0401,C0413

__version__ = version.__version__


class Repo():                                           # pylint:disable=R0903

    """Class:  Repo

    Description:  Class representation of the cat class.

    Methods:
        __init__
        allocation

    """

    def __init__(self):

        """Method:  __init__

        Description:  Initialization instance of the class.

        Arguments:

        """

        disk_tot = "disk.total"
        disk_avl = "disk.avail"
        disk_use = "disk.used"
        disk_per = "disk.percent"
        disk_ind = "disk.indices"

        self.format = None
        self.disks = [
            {"node": "nodename", disk_tot: "100gb", "shards": "101",
             disk_avl: "75gb", disk_use: "20gb", "host": "servername",
             disk_per: "21", "ip": "ip.addr", disk_ind: "15gb"},
            {"node": "nodename2", disk_tot: "110gb", "shards": "101",
             disk_avl: "65gb", disk_use: "30gb", "host": "servername2",
             disk_per: "31", "ip": "ip.addr2", disk_ind: "20gb"}]

    def allocation(self, **kwargs):

        """Method:  allocation

        Description:  Stub holder for cat.allocation method.

        Arguments:

        """

        self.format = kwargs.get("dataformat", None)

        return self.disks


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
        self.cat = Repo()


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

        disk_tot = "disk.total"
        disk_avl = "disk.avail"
        disk_use = "disk.used"
        disk_per = "disk.percent"
        disk_ind = "disk.indices"

        self.host_list = ["host1", "host2"]
        self.repo = "reponame"
        self.els = Elasticsearch(self.host_list)
        self.results = [
            {"node": "nodename", disk_tot: "100gb", "shards": "101",
             disk_avl: "75gb", disk_use: "20gb", "host": "servername",
             disk_per: "21", "ip": "ip.addr", disk_ind: "15gb"},
            {"node": "nodename2", disk_tot: "110gb", "shards": "101",
             disk_avl: "65gb", disk_use: "30gb", "host": "servername2",
             disk_per: "31", "ip": "ip.addr2", disk_ind: "20gb"}]

    def test_default(self):

        """Function:  test_default

        Description:  Test with default settings.

        Arguments:

        """

        self.assertEqual(elastic_class.get_disks(self.els), self.results)


if __name__ == "__main__":
    unittest.main()
