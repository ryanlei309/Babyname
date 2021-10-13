"""
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
-----------------------
File: babynames.py
Name: Ryan Lei
-----------------------
DESCRIPTION: This program add all the baby name files to the name_data
dictionary, and let user able to search the name in case-insensitive way.
"""

import sys


def add_data_for_name(name_data, year, rank, name):
    """
    Adds the given year and rank to the associated name in the name_data dict.

    Input:
        name_data (dict): dict holding baby name data
        year (str): the year of the data entry to add
        rank (str): the rank of the data entry to add
        name (str): the name of the data entry to add

    Output:
        This function modifies the name_data dict to store the provided
        name, year, and rank. This function does not return any values.

    """
    # When no same name in name_data, add new name, year and rank.
    if name not in name_data:
        year_d = {}
        year_d[year] = rank
        name_data[name] = year_d

    # Discuss with TA Gibbs on 2021/3/9
    # When same name in the name_data, just add year and rank in name_data
    elif name in name_data and year not in name_data[name]:
        name_data[name][year] = rank

    # When there is same name and same year in name_data.
    elif name in name_data and year in name_data[name]:

        # Get the original data out to compare.
        org_rank = name_data[name][year]

        # When original ranking higher than new ranking, change to new ranking.
        if int(org_rank) > int(rank):
            name_data[name][year] = int(rank)

        else:
            pass


def add_file(name_data, filename):
    """
    Reads the information from the specified file and populates the name_data
    dict with the data found in the file.

    Input:
        name_data (dict): dict holding baby name data
        filename (str): name of the file holding baby name data

    Output:
        This function modifies the name_data dict to store information from
        the provided file name. This function does not return any value.

    """
    with open(filename, 'r') as f:
        for line in f:
            # Split the year, name and rank in comma.
            rank_name_lst = line.split(',')

            # Discuss with TA Gibbs on 2021/3/9
            # When the len of the list smaller than 1, that is year.
            if len(rank_name_lst) <= 1:

                # Clear the space and get year data.
                year = rank_name_lst[0].strip()

            # When the len of the list bigger than 1, that is rank and name.
            elif len(rank_name_lst) > 1:

                # Clear the space and get rank, boy name, girl name data then add to add_data_for_name dict.
                rank = rank_name_lst[0].strip()
                boy_name = rank_name_lst[1].strip()
                girl_name = rank_name_lst[2].strip()
                add_data_for_name(name_data, year, rank, boy_name)
                add_data_for_name(name_data, year, rank, girl_name)


def read_files(filenames):
    """
    Reads the data from all files specified in the provided list
    into a single name_data dict and then returns that dict.

    Input:
        filenames (List[str]): a list of filenames containing baby name data

    Returns:
        name_data (dict): the dict storing all baby name data in a structured manner
    """
    name_data = {}

    # Discuss with TA Gibbs on 2021/3/9
    # Loop all the files in the list of the filenames and add the file to the list then return name data dict.
    for file in filenames:
        add_file(name_data, file)
    return name_data


def search_names(name_data, target):
    """
    Given a name_data dict that stores baby name information and a target string,
    returns a list of all names in the dict that contain the target string. This
    function should be case-insensitive with respect to the target string.

    Input:
        name_data (dict): a dict containing baby name data organized by name
        target (str): a string to look for in the names contained within name_data

    Returns:
        matching_names (List[str]): a list of all names from name_data that contain
                                    the target string

    """
    # List to store the matching name.
    matching_names = []

    # Case-insensitive.
    target = target.lower()

    # Loop over the name in name_data dict.
    for name in name_data:
        # Case-insensitive.
        name = name.lower()

        # When the target is in the name, add the name in the matching_names.
        if target in name:
            org_name = ''
            org_name += name[0].upper()
            org_name += name[1:]
            matching_names.append(org_name)
    return matching_names


def print_names(name_data):
    """
    (provided, DO NOT MODIFY)
    Given a name_data dict, print out all its data, one name per line.
    The names are printed in alphabetical order,
    with the corresponding years data displayed in increasing order.

    Input:
        name_data (dict): a dict containing baby name data organized by name
    Returns:
        This function does not return anything
    """
    for key, value in sorted(name_data.items()):
        print(key, sorted(value.items()))


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # Two command line forms
    # 1. file1 file2 file3 ..
    # 2. -search target file1 file2 file3 ..

    # Assume no search, so list of filenames to read
    # is the args list
    filenames = args

    # Check if we are doing search, set target variable
    target = ''
    if len(args) >= 2 and args[0] == '-search':
        target = args[1]
        filenames = args[2:]  # Update filenames to skip first 2

    # Read in all the filenames: baby-1990.txt, baby-2000.txt, ...
    names = read_files(filenames)

    # Either we do a search or just print everything.
    if len(target) > 0:
        search_results = search_names(names, target)
        for name in search_results:
            print(name)
    else:
        print_names(names)


if __name__ == '__main__':
    main()
