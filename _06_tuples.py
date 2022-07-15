"""Tuples"""

from random import randint

# Multiple value assignment
t = (7, 11, "cat", [1, 2, 3])
print(t)

# Single value assignment
s = (7,)
print(s)

# Tuples can be unpacked

# Unpack multiple values
x, y, pet, nums = t
print(x, y, pet, nums)

# Unpack some values
x, y, _, _ = t  # type: ignore
print(x, y)

# Unpack a single value
(x,) = s
print(x)

# Tuples provide single line assignment
x, y = 1, 2
print(x, y)

# Swap two values using tuple unpacking
x = 5
y = 4
print(x, y)
x, y = y, x  # Tuple unpacking
print(x, y)


# Return multiple values
def get_coordinate():
    x = randint(1, 10)
    y = randint(1, 10)
    return x, y


x, y = get_coordinate()
print(x, y)
