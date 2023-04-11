"""
File: get_gene_level_information.py

This program takes a host name and gene name
and retrieves the gene information and print to
STDERR.

Usage: get_gene_level_information -h host -g gene
"""
import argparse
import sys
import os
import re
from assignment5 import config
from assignment5 import io_utils


def main():
    """Business Logic"""
    args = get_cli_args()
    host = args.HOST
    gene = args.GENE


def update_host_name(host):
    """
    Checks that host name entered in command line is valid.
    returns host name, or prints a directory if not valid.
    :param host: name passed in through command line
    :return: host name or directory of hosts
    """
    host = host.lower()
    keys = config.get_keywords_for_hosts()
    host_ = keys.get(host)
    if host_ is True:
        return host_
    else:
        _print_directories_for_hosts()
        sys.exit(1)


def get_file_path(host_, gene):
    """
    Returns file path to host name and gene name
    provided in the command line.
    :param host_: host name
    :param gene: gene name
    :return: file path to gene
    """
    file = os.path.join(config.get_directory_for_unigene(), host_, gene + "." + config.get_extension_for_unigene())
    return file


def find_gene_file(file, gene, host_):
    """
 Checks to make sure that gene file is found by
 validating file path.
 :param file: file path to gene
 :param gene: gene name
 :param host_: host name retrieved from dictionary of hosts
 """
    if io_utils.is_gene_file_valid(file):
        print(f'\nFound Gene {gene} for {host_} ')
    else:
        print("Not Found")
        print(f'Gene {gene} does not exist for {host_}. exiting now...', file=sys.stderr)
        sys.exit(1)


def get_data_for_gene(file):
    """
    Opens file for host and gene and returns a sorted
    list of the tissues where the gene is expressed.
    :param file: file path to host and gene
    :return: sorted tissue list
    """
    data = io_utils.get_filehandle(file, 'r')

    for line in data:
        line = line.rstrip()
        match = re.search(r'^EXPRESS\s.*$', line)
        if match:
            tissue_string = match.group(1)
            tissues = tissue_string.split('|')
            tissues_list = tissues.sort()
            return tissues_list


def _print_directories_for_hosts():
    """Helper function to print host directories"""
    dict_ = config.get_keywords_for_hosts()
    vals = set(dict_.values())
    values = list(vals)
    keys = dict_.keys()
    fmt = '2:<30'

    print(""" '\n'
   Either the Host Name you are searching for is not in the database
    '\n' 
    or if you are trying to use the scientific name please put the name in double quotes
    '\n'
    '\"Scientific name\"
    '\n'
    Here is a (non-case sensitive) list of available Hosts by scientific name
    '\n'""", file=sys.stderr)

    for val in values:
        print(f'{values.index(val)}.{val:{fmt}}', file=sys.stderr)

    print(""""'\n' Here is a (non-case sensitive) list of available Hosts by common name
         '\n''""", file=sys.stderr)

    for k in keys:
        print(f'{values}.index(k).{k:{fmt}}', file=sys.stderr)


def get_cli_args():
    """Get command line arguments
      :return: Instance of argparse arguments"""

    parser = argparse.ArgumentParser(
        description="Give the Host and Gene name")
    parser.add_argument('-h', '--host', dest='HOST',
                        type=str, help='Name of Host', required=True, default='Human')
    parser.add_argument('-g', '--gene', dest='GENE',
                        type=str, help='Name of Gene', required=True, default='TGM1')

    return parser.parse_args()


if __name__ == '__main__':
    main()
