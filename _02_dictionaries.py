"""Dictionaries

- Backing store for types, classes, and objects
- Isomorphic with JSON
- Keyword arguments in functions/methods (i.e. **kwargs)
- O(1) search
"""

# ---------- Stop using lists for everything! ----------
# - See list_perf.py and dict_perf.py
# - list_perf.py: 4.001 seconds
# - dict_perf.py: 0.687 seconds
# - dict_perf is 82.83% faster than list_perf
# - 5.82x speedup

# ---------- Merging dictionaries ----------
from collections import defaultdict
from enum import Enum
import json
import random


line_one = {"Alex": 32, "Brayden": 26, "Nikita": 29}
line_two = {"Brandon": 23, "Anthony": 24, "Steven": 32}

# Non-pythonic / imperative
team = {}
for player in line_one:
    team[player] = line_one[player]
for player in line_two:
    team[player] = line_two[player]
print(team)

# Classic pythonic
team.clear()
team = line_one.copy()
team.update(line_two)
print(team)

# Using comprehensions
team = {k: v for line in [line_one, line_two] for k, v in line.items()}
print(team)

# Python 3.5+ pythonic way
team = {**line_one, **line_two}
print(team)

# ---------- Hacking Python's memory with slots ----------
# - See slots_perf.py
# - Using slots saved 91.6 MiB memory vs not using slots
# - That's 2.49x memory savings
# - Using slots saved 7.6 MiB memory vs using tuples
# - Using slots doesn't save memory vs dataclasses (+7.6 MiB memory)
# - Slots can speedup attribute access as well
# - Do not use slots by default! (maintenance suffers)
# - https://tech.oyster.com/save-ram-with-python-slots/

# ---------- Safer dictionary item access ----------
movie_data = {
    "year": "1975",
    "country": "United States",
    "title": "Jaws",
    "duration": "124 min",
}

# Optmistic style
print(movie_data["year"])
# print(movie_data["rating"])  # KeyError: 'rating'

# Pessimistic style
try:
    print(movie_data["year"])
    print(movie_data["rating"])
except KeyError as e:
    print(f"Not found: {e}")

# Safety first style
if "year" in movie_data:
    print(movie_data["year"])
if "rating" in movie_data:
    print(movie_data["rating"])
else:
    print("No rating found")

# Accept None instead style
print(movie_data.get("year", None))
print(movie_data.get("rating", None))

# Explicit alternative value style
print(movie_data.get("year", 0))
print(movie_data.get("rating", "*"))

# Accept default value instead style
default_movie_data = defaultdict(lambda: "MISSING", movie_data)
print(default_movie_data["year"])
print(default_movie_data["rating"])

# ---------- Simulate switch statement ----------


class TrafficLight(Enum):
    RED = 1
    YELLOW = 2
    GREEN = 3
    NO_LIGHT = 4


light_codes = (1, 2, 3, 4)
light_colour = TrafficLight(random.choice(light_codes))

# Traditional 'if statement'
if light_colour == TrafficLight.RED:
    print("stop")
elif light_colour == TrafficLight.GREEN:
    print("go")
elif light_colour == TrafficLight.YELLOW:
    print(
        "do not enter intersection / proceed",
        "with caution if unable to",
        "safely stop",
    )
else:
    print("No signal, treat as 4-way stop.")

# Simulate a switch statement using 'dict'
switch_on_light_colour = {
    TrafficLight.RED: lambda: print("stop"),
    TrafficLight.GREEN: lambda: print("go"),
    TrafficLight.YELLOW: lambda: print(
        "do not enter intersection / proceed",
        "with caution if unable to",
        "safely stop",
    ),
}

meaning = switch_on_light_colour.get(
    light_colour, lambda: print("No signal, treat as 4-way stop.")
)
meaning()

# ---------- To and from JSON ----------

movie_json = """
{
    "year": "1975",
    "country": "United States",
    "title": "Jaws",
    "duration": "124 min"
}
"""

# Use the 'json' module

# json to dict
movie_data = json.loads(movie_json)
print(type(movie_data), movie_data)

# dict to json
back_to_json = json.dumps(movie_data)
print(type(back_to_json), back_to_json)
