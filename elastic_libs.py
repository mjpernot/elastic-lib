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
import version

__version__ = version.__version__


def get_latest_dump(dump_list, **kwargs):

    """Function:  get_latest_dump

    Description:  Return latest dump from a list of dumps based on epoch date.

    Arguments:
        (input) dump_list -> List of dumps from a repository.
        (output) Name of latest dump.

    """

    dump_list = list(dump_list)
    last_dump = None

    if dump_list:
        search = max([item[4] for item in dump_list])

        for item in dump_list:
            if item[4] == search:
                last_dump = item[0]
                break

    return last_dump


def list_dumps(dump_list, **kwargs):

    """Function:  list_dumps

    Description:  Lists the dumps under the current repository.

    Arguments:
        (input) dump_list -> List of database dumps.

    """

    dump_list = list(dump_list)

    print("{0:45} {1:15} {2:10} {3:10} {4:10} {5:5} {6:5}"
          .format("Database Dump Name", "Status", "Time", "Number",
                  "Shard Information", "", ""))
    print("{0:45} {1:15} {2:10} {3:10} {4:10} {5:5} {6:5}"
          .format("", "", "", "Indexes", "Success", "Fail", "Total"))

    for item in dump_list:
        print("{0:45} {1:15} {2:10} {3:10} {4:10} {5:5} {6:5}"
              .format(item[0], item[1], item[6], item[7], item[8], item[9],
                      item[10]))


def list_repos2(repo_list, **kwargs):

    """Function:  list_repos2

    Description:  Lists the repositories in the Elasticsearch cluster.

    Arguments:
        (input) repo_list -> Dictionary of repositories.

    """

    repo_list = dict(repo_list)

    print("{0:30} {1}".format("Repository Name", "Location"))

    for repo in repo_list:
        print("{0:30} {1}".format(repo,
                                  repo_list[repo]["settings"]["location"]))
