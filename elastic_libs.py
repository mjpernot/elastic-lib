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
import lib.gen_libs as gen_libs
import version

__version__ = version.__version__


def get_latest_dump(dump_list):

    """Function:  get_latest_dump

    Description:  Return latest dump from a list of dumps based on epoch date.

    Arguments:
        (input) dump_list -> List of dumps from a repository
        (output) last_dump -> Name of latest dump

    """

    dump_list = list(dump_list)
    last_dump = None

    if dump_list:
        last_time = max([item['end_time_in_millis'] for item in dump_list])

        for dump in dump_list:
            if dump['end_time_in_millis'] == last_time:
                last_dump = dump['snapshot']
                break

    return last_dump


def list_dumps(dump_list, **kwargs):

    """Function:  list_dumps

    Description:  Lists the dumps under the current repository.

    Arguments:
        (input) dump_list -> List of database dumps
        (input) kwargs:
            raw -> True|False - Print raw data in JSON format

    """

    dump_list = list(dump_list)

    if kwargs.get("raw", False):

        for item in dump_list:
            gen_libs.print_dict(item, json_fmt=True)

    else:
        print("{0:15} {1:25} {2:14} {3:11} {4:12} {5:100}".
              format("Status", "Start Time", "Shard Success", "Shard Fail",
                     "Shard Total", "Database Dump Name"))

        for item in dump_list:
            print("{0:15} {1:25} {2:14} {3:11} {4:12} {5:100}".
                  format(
                      item["state"], item["start_time"],
                      item["shards"]["successful"], item["shards"]["failed"],
                      item["shards"]["total"], item["snapshot"]))


def list_repos2(repo_list):

    """Function:  list_repos2

    Description:  Lists the repositories in the Elasticsearch cluster.

    Arguments:
        (input) repo_list -> Dictionary of repositories

    """

    repo_list = dict(repo_list)

    print("{0:30} {1}".format("Repository Name", "Location"))

    for repo in repo_list:
        print("{0:30} {1}".format(repo,
                                  repo_list[repo]["settings"]["location"]))
