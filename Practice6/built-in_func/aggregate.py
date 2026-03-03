

from functools import reduce

numbers = [1, 2, 3, 4, 5]

# Sum of numbers
total = reduce(lambda x, y: x + y, numbers)

print("Sum using reduce:", total)
