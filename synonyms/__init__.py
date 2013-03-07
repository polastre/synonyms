"""Synonyms Python API"""

__version__ = "0.1"
__author__ = [
    "Joe Polastre <joe@polastre.com>"
]
__license__ = "public domain"
__contributors__ = "see AUTHORS"

from syn import Synonyms

def load(f, ignoreCase=True):
    return Synonyms.load(f, ignoreCase)
             
