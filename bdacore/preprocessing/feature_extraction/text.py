__author__ = "VLE"
__copyright__ = "Copyright 2016, OCTO Technology"
__version__ = "0.1"
__email__ = "vlevorato@octo.com"


def shinglelize(text, shingle_size=3):
    """
    Transform an input string to a list of shingles (or n-grams) with a given size.

    Parameters
    ----------
    text : string
        Text to shinglelize
        
    shingle_size: int, optional, default 3
        Size of a shingle

    Returns
    -------
    shingles : list
        List of shingles
    """

    shingles = []
    i = 0
    while (i + (shingle_size - 1)) < len(text):
        shingles.append(text[i:(i + shingle_size)])
        i = i + 1

    return shingles
