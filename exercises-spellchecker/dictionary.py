"""
We represent an English dictionary by using a python set
(don't confuse our English definition of dictionary
with a python dictionary here--anytime you see the word
"dictionary", we mean English dictionary).
"""

def load(dictionary_name):
    """
    Opens the file called `dictionary_name` and returns
    the set of words in that file.

    Hint: call the strip() method on a word to trim surrounding
    whitespace and newlines.

    Each line in the file contains exactly one word.
    """
    # TODO: remove the pass line and write your own code
    lines = set([line.strip() for line in open(dictionary_name)])
    return lines

def check(dictionary, word):
    """
    Returns True if `word` is in the English `dictionary`.
    """
    if word in dictionary:
	return True
    else:
	return False

def size(dictionary):
    """
    Returns the number of words in the English `dictionary`.
    """
    return len(dictionary)

def unload(dictionary):
    """
    Removes everything from the English `dictionary`.
    """
    dictionary=set([])
