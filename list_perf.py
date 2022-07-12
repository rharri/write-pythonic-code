import collections
import cProfile
import random
from pprint import pprint as pp

DataPoint = collections.namedtuple("DataPoint", "id x y temp quality")


# Make data points with random data
def _make_data_points():
    random.seed(0)
    data_points = []
    for d_id in range(500_000):
        data_point = DataPoint(
            id=d_id,
            x=random.randint(0, 1000),
            y=random.randint(0, 1000),
            temp=random.randint(-10, 50),
            quality=random.random(),
        )
        data_points.append(data_point)
    return data_points


# Reorder data because we are using auto-incrementing id's
def _shuffle_data_points(data_points):
    random.shuffle(data_points)


# Generate a set of 100 random id's
def _generate_interesting_ids(data_points):
    return {random.randint(0, len(data_points)) for _ in range(0, 100)}


# Locate the interesting id's in the data list
def _locate_interesting_ids(data_points):
    interesting_ids = _generate_interesting_ids(data_points)
    interesting_data_points = []
    for id in interesting_ids:
        for data_point in data_points:
            if id == data_point.id:
                interesting_data_points.append(data_point)
                break
    return interesting_data_points


# Pretty print results
def _print_results(interesting_data_points):
    pp(interesting_data_points)


# Do not include the making of data points in the profile
data_points = _make_data_points()


def main():
    _shuffle_data_points(data_points)
    interesting_data_points = _locate_interesting_ids(data_points)
    _print_results(interesting_data_points)


cProfile.run("main()")
