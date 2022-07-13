"""Slicing"""

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# All numbers
print(nums)

# First 5
print(nums[:5])

# Index 2 to 7
print(nums[2:8])

# Last 3 (using len)
# fmt: off
print(nums[len(nums) - 3:])
# fmt: on

# Last 3 (Pythonic)
print(nums[-3:])
