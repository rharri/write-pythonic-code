from dataclasses import dataclass
import tracemalloc

# TODO: Cleanup


class NoSlots:
    """This class does not use dunder slots.

    A dict will be used to store attributes.
    """

    def __init__(self, a, b, c) -> None:
        self.a = a
        self.b = b
        self.c = c


class Slots:
    """This class uses dunder slots.

    A dict will not be created for instances of this class.
    No additional attributes can be associated with this type.
    """

    # Python 3.8+ __slots__ can be defined with dicts
    # key (attribute name), value (docstring)
    __slots__ = {
        "a": "Attribute A",
        "b": "Attribute B",
        "c": "Attribute C",
    }

    def __init__(self, a, b, c) -> None:
        self.a = a
        self.b = b
        self.c = c


@dataclass
class DataClass:
    a: int
    b: int
    c: int


# We need to do something with our objects or else they will be gc'd
# at the end of the loop
keep = []

# Make 1M objects
count = 1_000_000

# Start the trace of 'no slots'
tracemalloc.start()

for n in range(count):
    no_slots = NoSlots(1 + n, 2 + n, 3 + n)
    keep.append(no_slots)

# End the trace of 'no slots'
snapshot_no_slots = tracemalloc.take_snapshot()
tracemalloc.stop()

# Clear the keep for the next trace
keep.clear()

# Start the trace of 'using slots'
tracemalloc.start()

for n in range(count):
    slots = Slots(1 + n, 2 + n, 3 + n)
    keep.append(slots)  # type: ignore

# End the trace of 'using slots'
snapshot_using_slots = tracemalloc.take_snapshot()
tracemalloc.stop()

# Clear the keep for the next trace
keep.clear()

# Start the trace of 'tuples'
tracemalloc.start()

for n in range(count):
    tup = (
        1 + n,
        2 + n,
        3 + n,
    )
    keep.append(tup)  # type: ignore

# End the trace of 'tuples'
snapshot_using_tuples = tracemalloc.take_snapshot()
tracemalloc.stop()

# Clear the keep for the next trace
keep.clear()

# Start the trace of 'dataclass'
tracemalloc.start()

for n in range(count):
    d = DataClass(1 + n, 2 + n, 3 + n)
    keep.append(d)  # type: ignore

# End the trace of 'dataclass'
snapshot_dataclass = tracemalloc.take_snapshot()
tracemalloc.stop()

# Filter out tracemalloc traces
# fmt: off
snapshot_no_slots = snapshot_no_slots.filter_traces((
    tracemalloc.Filter(False, tracemalloc.__file__),
))
snapshot_using_slots = snapshot_using_slots.filter_traces((
    tracemalloc.Filter(False, tracemalloc.__file__),
))
# fmt: on

# Compare snapshots and print the differences
snapshot_diffs = snapshot_using_slots.compare_to(snapshot_no_slots, "filename")
for diff in snapshot_diffs:
    print(diff)

# Filter out tracemalloc traces
# fmt: off
snapshot_using_tuples = snapshot_using_tuples.filter_traces((
    tracemalloc.Filter(False, tracemalloc.__file__),
))

# Compare snapshots and print the differences
snapshot_diffs = \
    snapshot_using_slots.compare_to(snapshot_using_tuples, "filename")
# fmt: on
for diff in snapshot_diffs:
    print(diff)

# Filter out tracemalloc traces
# fmt: off
snapshot_dataclass = snapshot_dataclass.filter_traces((
    tracemalloc.Filter(False, tracemalloc.__file__),
    tracemalloc.Filter(False, "<string>"),
))

# Compare snapshots and print the differences
snapshot_diffs = \
    snapshot_using_slots.compare_to(snapshot_dataclass, "filename")
# fmt: on
for diff in snapshot_diffs:
    print(diff)
