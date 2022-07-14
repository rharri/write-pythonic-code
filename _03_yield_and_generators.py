"""Yield and generators"""


import collections
import uuid


def classic_fibonacci(limit):
    fib_seq = []
    current, next = 0, 1

    while current < limit:
        current, next = next, next + current
        fib_seq.append(current)
    return fib_seq


def generator_fibonacci():
    current, next = 0, 1

    while True:
        current, next = next, next + current
        yield current


if __name__ == "__main__":
    # Classic
    for m in classic_fibonacci(100):
        print(m, end=", ")
    print(end="\n")

    # Generator
    for m in generator_fibonacci():
        print(m, end=", ")
        if m > 100:
            break
    print(end="\n")

# ---------- Recursive generators with yield from ---------
# https://peps.python.org/pep-0380/


class _Node:
    def __init__(self, data: object) -> None:
        self.data: object = data
        self.next: _Node | None = None


n1 = _Node(1)
n2 = _Node(2)
n3 = _Node(3)

n1.next = n2
n2.next = n3


# Use 'yield from' to delegate to another generator. The second generator
# yields generator objects that are 'joined' with the delegating generator,
# producing a single stream of values. In this example, the second generator
# is used to yield values that result from recursively traversing all nodes
# in a linked list.
def next(node: _Node | None):
    if node:
        yield node
        yield from next(node.next)

        # Replaced by 'yield from' introduced in Python 3.3
        # for next_node in next(node.next):
        #     yield next_node


# Recursive yield version
for node in next(n1):
    print(node.data, end=" -> ")
print(end="\n")


# Iterative version using just 'yield'
def next_iter(node: _Node | None):
    while node:
        yield node
        node = node.next


# Iterative version
for node in next_iter(n1):
    print(node.data, end=" -> ")
print(end="\n")

# ---------- Inline generators via generator expressions ----------

Measurement = collections.namedtuple("Measurement", "id x y value")

measurements = [
    Measurement(str(uuid.uuid4()), 1, 1, 72),
    Measurement(str(uuid.uuid4()), 1, 2, 40),
    Measurement(str(uuid.uuid4()), 1, 3, 11),
    Measurement(str(uuid.uuid4()), 2, 1, 90),
    Measurement(str(uuid.uuid4()), 2, 2, 60),
    Measurement(str(uuid.uuid4()), 2, 3, 73),
    Measurement(str(uuid.uuid4()), 3, 1, 40),
    Measurement(str(uuid.uuid4()), 3, 2, 90),
    Measurement(str(uuid.uuid4()), 3, 3, 90),
]

# Imperative style
high_measurements1 = []
for m in measurements:
    if m.value >= 70:
        high_measurements1.append(m.value)
print(high_measurements1)

# List of high measurements via list comprehensions
high_measurements2 = [m.value for m in measurements if m.value >= 70]
print(high_measurements2)

# ... via generator expression
high_measurements3 = (m.value for m in measurements if m.value >= 70)
print(list(high_measurements3))

# High measurements with their ID
high_measurements4 = {m.id: m.value for m in measurements if m.value >= 70}
print(high_measurements4)

# Distict high measurements with a set comprehension
high_measurements5 = {m.value for m in measurements if m.value >= 70}
print(high_measurements5)

# ---------- Counting generators ----------

# Generators are exhausted after each use, i.e. cannot reuse high_measurements3
high_values = (m.value for m in measurements if m.value >= 70)

# Values of a generator object are not in memory, can't count them
# Values of a generator object may be infinite, counting is not practical
# Compose generators in order to count
# The generator expression being 'counted' should be filtered in some way
count = sum(1 for _ in high_values)

# Print the count
print(f"We have {count} measurements")
