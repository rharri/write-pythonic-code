"""There is no numerical loop"""

data = [n for n in range(10)]

# Python does not have a 'fori' loop

# Not Pythonic!
i = 0
while i < len(data):
    print(data[i], end=", ")
    i += 1
print(end="\n")

# Pythonic
for item in data:
    print(item, end=", ")
print(end="\n")

# Need to loop through a sequence of numbers?
for n in range(1, 11):  # range returns a genarator
    print(n, end=", ")
print(end="\n")

# Need the item and index?
for index, item in enumerate(data):
    print(f"{{{index}: {item}}}")

# Python loops have an else block
# Else block only executes if the loop completes without interruption
# Don't use it!
count = 0
while count < 5:
    print(".", end="")
    count += 1
else:
    print("Else clause")

count = 0
while count < 5:
    print(".", end="")
    count += 1
    if count % 2 == 0:
        break
else:
    print("Else clause")
print(end="\n")
