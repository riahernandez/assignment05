"""Module used for configuration:
defines global variables and error messages"""
# pylint: disable=invalid-name

# define global variables
_DIRECTORY_FOR_UNIGENE = "/BINF6200/assignment5/data"
_FILE_ENDING_FOR_UNIGENE = "unigene"

"""Functions for retrieving error messages"""


def get_error_ValueError():
    """Print invalid argument message for the ValueError"""  # error for invalid r/w in get_filehandle
    print("Invalid argument value for fh_in for reading or writing file")


def get_error_TypeError():
    """Print invalid argument message for TypeError """  # error for invalid argument for get_filehandle (fh_in)
    print("Invalid argument Type passed in:")


def get_error_opening_file_OSError(file: str, mode: str):
    """
    Print invalid argument message for OSError
    :param file: fh_in name
    :param mode: The mode to open the fh_in
    """
    print(f"Could not open the fh_in (OS Error): {file} with mode {mode}")


def get_directory_for_unigene():
    """
    Return global variable for directory
    :return: location to directory where data is stored
    """
    return _DIRECTORY_FOR_UNIGENE


def get_extension_for_unigene():
    """
    Return global variable for file extensions
    :return: file extension
    """
    return _FILE_ENDING_FOR_UNIGENE


def get_keywords_for_hosts():
    """
    Returns dictionary of host names for mapping
    :return: host names
    """
    bos = "Bos_taurus"
    homo = "Homo_sapien"
    equus = "Equus_caballus"
    mus = "Mus_musculus"
    ovis = "Ovis_aries"
    rattus = "Rattus_norvegicus"

    host_keywords = {
        "bos taurus": bos,
        "bos_taurus": bos,
        "cow": bos,
        "cows": bos,
        "moo": bos,
        "homo sapien": homo,
        "homo_sapien": homo,
        "human": homo,
        "man": homo,
        "woman": homo,
        "child": homo,
        "equus_caballus": equus,
        "equus caballus"
        "horse": equus,
        "pony": equus,
        "neigh": equus,
        "mouse": mus,
        "mus_musculus": mus,
        "mus musculus": mus,
        "mice": mus,
        "squeak": mus,
        "ovis_aries": ovis,
        "ovis aries": ovis,
        "sheep": ovis,
        "sheeps": ovis,
        "baa": ovis,
        "ewe": ovis,
        "rattus_norvegicus": rattus,
        "rattus norvegicus": rattus,
        "rat": rattus,
        "rats": rattus,
        "big squeak": rattus,
    }
    return host_keywords


