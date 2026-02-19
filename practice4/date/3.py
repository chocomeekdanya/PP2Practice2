import math

n = 4
s = 25

area = (n * s**2) / (4 * math.tan(math.pi / n))

print("Input number of sides:", n)
print("Input the length of a side:", s)
print("The area of the polygon is:", int(area))
