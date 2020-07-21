#name1 = input ("What is your first name?")
#name2 = input ("What is your last name?")
#print("Hello " + name2 + " " + name1 )

counter = 0
for i in range(3):
  counter += 1
  print(counter)

  for x in range(20):
    if x > 10:
      print("greater than", x)
    elif x == 10:
      print("x is 10", x)
    else:
      print("less than 10", x)