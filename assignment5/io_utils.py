"""
Contains a function for opening files for reading and writing.
This is meant to be imported as a module.
"""

import os
from assignment5 import config


def get_filehandle(file=None, mode=None):
    """
    Creates a filehandle using the two arguments-the file to be opened and the mode in
    which to open it.
    :param file: the file to be opened
    :param mode: the mode in which the file should be opened
    :return: filehandle
    """
    try:
        fh = open(file, mode)
        return fh
    except OSError:
        config.get_error_opening_file_OSError(file=file, mode=mode)
        raise
    except ValueError:
        config.get_error_ValueError()
        raise


def is_gene_file_valid(file):
    """
   Check to see if gene file for host exists
   :param file: file path to gene name
   :return: True or False
   """
    if os.path.exists(file):
        return True
    else:
        return False
