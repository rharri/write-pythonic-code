"""Pythonic Functions"""

# ---------- Lambda expressions ----------


def is_odd(n):
    return n % 2 == 1


def find_special_numbers(special_selector, limit=10):
    found = []
    n = 0
    while len(found) < limit:
        if special_selector(n):
            found.append(n)
        n += 1
    return found


for n in find_special_numbers(is_odd, 50):
    print(n, end=", ")
print(end="\n")

for n in find_special_numbers(lambda n: n % 2 == 1, 50):
    print(n, end=", ")
print(end="\n")

# ---------- Avoid return values for error handling ----------
# Look Before You Leap (LBYL) is not Pythonic
#   - i.e. guard statements
# Easier to Ask for Forgiveness than for Permission (EAFP) is Pythonic
#   - i.e. try...except

# ---------- There is no method overloading in Python ----------

# ---------- Default values for overloads ----------


def print_greeting(name, greeting="Hello", times=1):
    times = max(1, times)
    for _ in range(times):
        print(f"{greeting} {name}")


print_greeting("Brian", "Good morning", 3)
print_greeting("John", "Good afternoon", 2)

# Possible because of default values
print_greeting("Brian")
print_greeting("John", "Good afternoon")
print_greeting(name="Brian", greeting="Good afternoon", times=2)
print_greeting("John", times=4)

# ---------- Passing variable number of arguments ----------


def print_words(word1, word2, word3):
    print(word1, word2, word3)


print_words("Why", "hello", "there")


# Redefine print_words function
def print_words(word, *words):  # type: ignore
    print(word, *words)  # words is a <class 'tuple'>


print_words("Why", "hello", "there")

# ---------- Unpacking dictionaries as named arguments ----------
# kwargs
# keyword arguments


def print_greeting(name, greeting="Hello", times=1):  # type: ignore
    times = max(1, times)
    for _ in range(times):
        print(f"{greeting} {name}")


data = {
    "name": "Tiger",
    "greeting": "What's up",
    "times": 5,
}

print_greeting(**data)


def print_greeting(name, **options):  # type: ignore
    greeting = options.get("greeting", "Hello")
    times = max(1, options.get("times", 0))
    for _ in range(times):
        print(f"{greeting} {name}")


print_greeting("John")
print_greeting("John", greeting="Good afternoon", times=2)
greet_options = {"greeting": "Goodnight", "times": 6}
print_greeting("John", **greet_options)

# ---------- The danger of mutable default arguments ----------


# Lists are mutable
# A new list object is created when the repeat_letter function is defined
# A new list object is not created each time the function is called!
def repeat_letter(letter, repeat, repeated=[]):
    for _ in range(repeat):
        repeated.append(letter)
    return repeated


a = repeat_letter("a", 3)
print(a)
b = repeat_letter("b", 2)
print(b)
assert id(a) == id(b)  # a and b point to the same list instance


# Fixed: Create a new list instance each time repeat_letter is called
def repeat_letter(letter, repeat, repeated=None):  # type: ignore
    if repeated is None:
        repeated = []
    for _ in range(repeat):
        repeated.append(letter)
    return repeated


a = repeat_letter("a", 3)
print(a)
b = repeat_letter("b", 2)
print(b)
# assert id(a) == id(b)  # AssertionError
