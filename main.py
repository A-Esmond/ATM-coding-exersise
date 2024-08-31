def withdraw():
  print("1: £10")
  print(" ")
  print("2: £20")
  print(" ")
  print("3: £50")
  print(" ")
  print("4: OTHER AMMOUNT")
  print(" ")

  option = int(input("ENTER OPTION:"))
  print(" ")
  print(" ")
  while bool is True:
    if option == 1:
      print("WITHDRAWING £10")
      print(" ")
      print("COLLECT CARD")
      # here would be balance = balance - ammount
      bool = False
    elif option == 2:
      print("WITHDRAWING £20")
      print(" ")
      print("COLLECT CARD")
      # here would be balance = balance - ammount
      bool = False
    elif option == 3:
      print("WITHDRAWING £50")
      print(" ")
      print("COLLECT CARD")
      # here would be balance = balance - ammount
      bool = False
    elif option == 4:
      ammount= int(input("ENTER AMMOUNT"))
      if ammount%5 == 0:
        print("WITHDRAWING", ammount)
        print(" ")
        print("COLLECT CARD")
        # here would be balance = balance - ammount
        bool = False
    else:
      print("INVALID OPTION")
      
    

balance = "you are broke, my friend..."
bool = False
while bool is False:
  pin = int(input("ENTER PIN:"))
  print(" ")
  print(" ")

  if pin == 1234:
    print("1: CASH AND BALANCE")
    print(" ")
    print("2: DISPLAY BALACNE")
    print(" ")
    print("3: WITDRAW")
    print(" ")
    print(" ")
    bool = True
  else:
    print("INVALID PIN")
    print(" ")
    print(" ")

while bool is True:
  option = int(input("ENTER OPTION:"))
  if option == 1:
    print(" ")
    print(" ")
    print(balance)
    print(" ")
    print(" ")
    withdraw()
  elif option == 2:
    print(balance)
    print("COLLECT CARD")
  elif option == 3:
    withdraw()
  else:
      print("INVALID OPTION")




