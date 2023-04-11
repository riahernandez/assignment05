"""Test suite for config.py"""

import os
import pytest
# ignore all "Missing function or method docstring" since this is a unit test
# pylint: disable=C0116
# ignore all "Function name "test_get_error_opening_file_OSError" doesn't conform to snake_case naming style"
# pylint: disable=C0103
# Usage: --cov-branch --cov-report html --cov --cov-config=.coveragearc


from assignment5.config import get_error_ValueError, get_error_TypeError, get_error_opening_file_OSError, \
    get_keywords_for_hosts, get_directory_for_unigene, get_extension_for_unigene
from assignment5.io_utils import get_filehandle

# Global Variables
_DIRECTORY_FOR_UNIGENE = "/BINF6200/assignment5/data"
_FILE_ENDING_FOR_UNIGENE = "unigene"


def test_get_error_ValueError():
    # does the value error message print
    # test
    
     get_filehandle("does_not_exist.txt", 'z')

def test_get_error_TypeError():
    # Does the type error message print
    # test
    get_filehandle("[]", "r")
    assert get_error_TypeError(), "Error message does not print"


def test_get_error_opening_file_OSError():
    # Does the OSError message print
    # test
    get_filehandle(file="does_not_exist.txt", mode="r")
    assert get_error_opening_file_OSError(), "Error message does not print"


def test_get_directory_for_unigene():
    # Does the variable for the directory print
    assert get_directory_for_unigene() == _DIRECTORY_FOR_UNIGENE, "Variable is not returned"


def test_get_extension_for_unigene():
    # Does the variable for the extension print
    # test
    assert get_extension_for_unigene() == _FILE_ENDING_FOR_UNIGENE, "Variable is not returned"


def test_get_keywords_for_hosts():
    # Is the dictionary of host names returned if a host
    # is passed in?
    # test
    host = 'cow'
    key = get_keywords_for_hosts()
    assert key.get(host), "Key, values not returned from dictionary"
