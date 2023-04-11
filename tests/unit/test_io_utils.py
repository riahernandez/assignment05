"""Test suite for io_utils.py"""

import os
import pytest
# ignore all "Missing function or method docstring" since this is a unit test
# pylint: disable=C0116
# ignore all "Function name "test_get_error_opening_file_OSError" doesn't conform to snake_case naming style"
# pylint: disable=C0103
# Usage: --cov-branch --cov-report html --cov --cov-config=.coveragearc

from assignment5.io_utils import get_filehandle, is_gene_file_valid

FILE_TO_TEST = "test_file.txt"
DIRECTORY_TO_TEST = "fake/fake/"

def test_get_filehandle_for_reading():
    # does it open the file for reading
    # create a test file
    _create_file_for_testing(FILE_TO_TEST)
    # test
    test = get_filehandle(FILE_TO_TEST, 'r')
    # make sure that the readline can work on the test file
    assert hasattr(test, 'readline') is True, "Unable to open and read"
    test.close()
    os.remove(FILE_TO_TEST)


def test_get_filehandle_for_writing():
    # does it open the file for reading
    # create test file
    _create_file_for_testing(FILE_TO_TEST)
    # test
    test = get_filehandle(FILE_TO_TEST, 'w')
    # make sure that the readline can work on the test file
    assert hasattr(test, 'write') is True, "Unable to open writing"
    test.close()
    os.remove(FILE_TO_TEST)


def test_get_filehandle_for_OSError():
    # Des it raise OSError
    # Should exit
    with pytest.raises(OSError):
        get_filehandle("does_not_exist.txt", "r")


def test_get_filehandle_for_ValueError():
    # does it raise Value Error
    # this should exit
    _create_file_for_testing(FILE_TO_TEST)
    with pytest.raises(ValueError):
        get_filehandle("does_not_exist.txt", "rrr")
    os.remove(FILE_TO_TEST)


def test_is_gene_file_valid():
    # does it return true when file path is valid
    # create a directory to test
    # test

   _create_directory_for_testing(DIRECTORY_TO_TEST)
   assert is_gene_file_valid(DIRECTORY_TO_TEST) is True, "Not able to identify directory"
   os.rmdir(DIRECTORY_TO_TEST)

def test_is_gene_file_valid_error():
     # will function return False if path
    # does not exist?
    # test
     directory = 'fake.txt'
     assert is_gene_file_valid(directory) is False, "Unable to determine a directory does not exist"



def _create_file_for_testing(file):
    # helper function for testing
    # create a test file
    open(file, 'w').close()

def _create_directory_for_testing(directory):
   os.makedirs(directory)

