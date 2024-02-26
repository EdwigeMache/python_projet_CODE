
#number_0_50= list(range(51))

for i in range (1, 15):
   if i % 3==0 :
      print("FOO") 
   elif i % 5==0:
      print("BAR")
   elif i % 3==0 and   i % 5==0 :
      print("FOOBAR")
   else:
      print(i)




