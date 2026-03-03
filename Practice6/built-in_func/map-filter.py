

numbers = [1, 2, 3, 4, 5, 6]

# map() – square numbers
squared = list(map(lambda x: x**2, numbers))

# filter() – keep even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))

print("Squared:", squared)
print("Even numbers:", evens)
