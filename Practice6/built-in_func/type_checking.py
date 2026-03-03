

value = "123"

# Type checking
print("Type before:", type(value))

if isinstance(value, str):
    number = int(value)

print("Converted value:", number)
print("Type after:", type(number))

# More conversions
float_value = float(number)
str_value = str(float_value)

print("Float:", float_value)
print("String again:", str_value)
