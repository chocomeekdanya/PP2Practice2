def myfunc():
  x = 300
  print(x)

myfunc()
#--------- example 2
def myfunc2():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc2()
