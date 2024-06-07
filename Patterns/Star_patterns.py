#First Patter
#Time complexity : n^2

n = 5
for i in range(n):
  for j in range(n):
    print("*" , end=" ")
  print()


#Second Pattern
for i in range(n):
  for j in range(i+1):
    print("*", end=" ")
  print()



#Third Pattern
for i in range(n):
  for j in range(n-i):
    print("*", end=" ")
  print()



  