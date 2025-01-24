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
try:
    from .lib import gen_libs
    from . import version

except (ValueError, ImportError) as err:
    import lib.gen_libs as gen_libs                     # pylint:disable=R0402
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
        print(f'{"Status":15} {"Start Time":30} {"Shard Success":14}'
              f' {"Shard Fail":11} {"Shard Total":11}'
              f' {"Database Dump Name":100}')

        for item in dump_list:
            print(f'{item["state"]:15} {item["start_time"]:30}'
                  f' {item["shards"]["successful"]:13}'
                  f' {item["shards"]["failed"]:11}'
                  f' {item["shards"]["total"]:12} {item["snapshot"]:100}')


def list_repos2(repo_list):

    """Function:  list_repos2

    Description:  Lists the repositories in the Elasticsearch cluster.

    Arguments:
        (input) repo_list -> Dictionary of repositories

    """

    repo_list = dict(repo_list)

    print(f'{"Repository Name":30} {"Location"}')

    for repo in repo_list:
        print(f'{repo:30} {repo_list[repo]["settings"]["location"]}')
