# One import per line

# Favour from module import name style imports
# E.g. from os import chmod, chdir

# Avoid wildcard imports
# E.g. from os import *

# Order:
# 1. Standard library imports
# 2. 3rd party imports
# 3. Local imports

from typing import Final

# Constants are UPPERCASE, convention -> please don't change
LOG_FUNCTION_ENTRY: Final[bool] = True


# Classes are CamelCase
class SpamMenu:
    pass


# Two blank lines between module-level functions
# Docstrings for all public modules, functions, classes, and methods.
def max(comparable1, comparable2):
    """Returns the larger of two comparable objects.

    :param comparable1: First object to compare.
    :param comparable2: Second object to compare.
    :return: The larger item.
    """
    if comparable1 > comparable2:  # Indent 4 spaces, no tabs
        return comparable1
    else:
        return comparable2


# function and variable names use snake_case
def some_function():
    pass
