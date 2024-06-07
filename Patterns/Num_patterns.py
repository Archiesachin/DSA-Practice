n = 5

#First Pattern
for i in range(n):
  for j in range(1, i+2):
    print(j, end=" ")
  print()

#Second Pattern
for i in range(n):
  for j in range(1, i+2):
    print(i+1, end=" ")
  print()


#Third Pattern

for i in range(n):
  for j in range(n-i):
    print(j+1, end=" ")
  print()