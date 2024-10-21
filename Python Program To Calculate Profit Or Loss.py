Cp = int(input("Enter Cost Price"))
Sp = int(input("Enter Selling Price"))
if Sp > Cp:
    profit = Sp-Cp 
    print(profit,"profit ")
elif Sp < Cp:
    loss = Cp-Sp 
    print(loss,"loss")
else:
    print("No Loss or Profit")