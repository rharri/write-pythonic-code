"""Testing for containment"""

even_numbers_list = [n for n in range(51) if n % 2 == 0]
even_numbers_set = {n for n in range(51) if n % 2 == 0}
even_numbers_dict = {n: n for n in range(51) if n % 2 == 0}

n = int(input("Provide a number: "))

print("{} in list".format(n) if n in even_numbers_list else "not in list")
print("{} in set".format(n) if n in even_numbers_set else "not in set")
print("{} in dict".format(n) if n in even_numbers_dict else "not in dict")

# ---------- Containment with text ----------
word = input("Quote from yoda: ")

text = "Do or do not, there is no try."
if word in text:
    print("Wise words from grandmaster yoda")
else:
    print("At an end your rule is, and not short enough it was!")
