def my_function(): #def _name_ is a way to define a function
  print("Hello from a function")
my_function() #way to call functions

#---- example 2
def fahrenheit_to_celsius(fahrenheit):
  return (fahrenheit - 32) * 5 / 9

print(fahrenheit_to_celsius(77))
print(fahrenheit_to_celsius(95))
print(fahrenheit_to_celsius(50))

# example 3
def my_function():
  pass #function cannot be empty, so you can use pass 
