
n=0
while n<15:
  n=n+1
  if n % 3==0 :
      print("FOO") 
  elif n % 5==0:
      print("BAR")
  elif n % 3==0 and   n % 5==0 :
      print("FOOBAR")
  else:
      print(n)