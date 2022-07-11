"""
Truthiness

False   # false is false
[]      # empty lists are false
{}      # empty dicts are false
""      # emptry strings are false
0       # zero ints are false
0.0     # zero floats are false
None    # None is false
Custom  # Custom __bool__ (__nonzero__ Python 2.x)

Everything else is true!
"""


from enum import Enum
import random
import sys


def print_truthiness_of(exp):
    out = f"{exp} is TRUE" if exp else f"{exp} is FALSE"
    print(out)


class UserDefinedClass:
    def __bool__(self) -> bool:
        """
        Tell Python how this class should behave in a boolean context.
        """
        return False

    def __repr__(self) -> str:
        return "UserDefinedClass"


print_truthiness_of(True)
print_truthiness_of(False)
print_truthiness_of([])
print_truthiness_of([1, 2, 3])
print_truthiness_of({})
print_truthiness_of({1: "a", 2: "b", 3: "c"})
print_truthiness_of("")  # empty string
print_truthiness_of("python")
print_truthiness_of(0)
print_truthiness_of(0.0)
print_truthiness_of(None)
print_truthiness_of(UserDefinedClass())

# Prefer 'if val' over 'if val is True'

"""
Testing for None
"""
val = None

# Comparing singletons, use 'is'
if val is None:
    print("val")

# Comparing singletons, use 'is not'
if val is not None:
    print("no val")


"""
Avoid multiple tests against a single variable
"""


class Moves(Enum):
    West = 1
    North = 2
    East = 3
    South = 4


our_move = Moves.East

# Not so Pythonic
if (
    our_move == Moves.North
    or our_move == Moves.South
    or our_move == Moves.East
    or our_move == Moves.West
):
    print("We are on the move.")

# Pythonic (slower, but more readable)
if our_move in {Moves.North, Moves.South, Moves.East, Moves.West}:
    print("We are on the move.")

# In a loop, performance is slower
# Move the set creation outside of the loop

"""
Choosing a random item
"""

letters = "abcdefghijklmnopqrstuvwxyz1234567890"

# C-style
index = random.randint(0, len(letters) - 1)
print(letters[index])

# Pythonic
print(random.choice(letters))

# Prefer declarative over procedural/imperative

"""
String formatting
"""

name, creation = "Guido", "Python"

# Not Pythonic (breaks if the variable is not a string, no implicit conversion)
print("Hi, I'm " + name + " and I created " + creation)

# Pythonic, but could break if the argument does not match the placeholder type
print("Hi, I'm %s and I created %s" % (name, creation))

# More Pythonic and safer
print("Hi, I'm {} and I created {}".format(name, creation))

# Even more Pythonic (f-strings, string iterpolation)
print(f"Hi, I'm {name} and I created {creation}")

"""
Flat is better than nested
"""


def test_conditions_nested(condition1, condition2, condition3):
    if condition1:
        if condition2:
            if condition3:
                print("Success")
            else:
                print("Failed: Condition 3")
        else:
            print("Failed: Condition 2")
    else:
        print("Failed: Condition 1")


def test_conditions_flat(condition1, condition2, condition3):
    if not condition1:
        print("Failed: Condition 1")
        return

    if not condition2:
        print("Failed: Condition 2")
        return

    if not condition3:
        print("Failed: Condition 3")
        return

    print("Success")


test_conditions_nested(True, True, False)
test_conditions_flat(True, True, False)

""""
Use exit codes if your script or program will be used by other scripts or
programs. Allows others to make decisions based on the success or failure
of your script/program.
"""


def main(success):
    if success:
        sys.exit(0)
    else:
        sys.exit(1)


main(success=False)

# Bash:
# $ echo $?
# 1
