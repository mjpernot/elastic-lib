# Classification (U)

"""Program:  elastic_libs.py

    Description:  A library program that contains a number of modules for
        general Elasticsearch database use.

    Functions:
        get_latest_dump
        list_dumps
        list_repos2

"""

# Libraries and Global Variables

# Standard

# Local
import requests_lib.requests_libs as requests_libs
import version

__version__ = version.__version__


def get_latest_dump(dump_list, **kwargs):

    """Function:  get_latest_dump

    Description:  Return latest dump from a list of dumps based on epoch date.

    Arguments:
        (input) dump_list -> List of dumps from a repository.
        (output) Name of latest dump.

    """

    if dump_list:
        search = max([x[4] for x in dump_list])

        for x in dump_list:
            if x[4] == search:
                return x[0]

    else:
        return None


def list_dumps(dump_list, **kwargs):

    """Function:  list_dumps

    Description:  Lists the dumps under the current repository.

    Arguments:
        (input) dump_list -> List of database dumps.

    """

    print("{0:25} {1:15} {2:10} {3:10} {4:10} {5:5} {6:5}"
          .format("Database Dump Name", "Status", "Time", "Number",
                  "Shard Information", "", ""))
    print("{0:25} {1:15} {2:10} {3:10} {4:10} {5:5} {6:5}"
          .format("", "", "", "Indexes", "Success", "Fail", "Total"))

    for x in dump_list:
        print("{0:25} {1:15} {2:10} {3:10} {4:10} {5:5} {6:5}"
              .format(x[0], x[1], x[6], x[7], x[8], x[9], x[10]))


def list_repos2(repo_list, **kwargs):

    """Function:  list_repos2

    Description:  Lists the repositories in the Elasticsearch cluster.

    Arguments:
        (input) repo_list -> List of repositories.

    """

    repo_list = list(repo_list)

    print("{0:30} {1}".format("Repository Name", "Location"))

    for repo in repo_list:
        print("{0:30} {1}".format(repo,
                                  repo_list[repo]["settings"]["location"]))
