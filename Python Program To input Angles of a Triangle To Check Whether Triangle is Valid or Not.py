Angle1 = int(input("Enter first Angle"))
Angle2 = int(input("Enter Second Angle"))
Angle3 = int(input("Enter third Angle"))
if Angle1<=0 or Angle2<=0 or Angle3<=0:
    print("The Triangle is Not Valid")
elif Angle1 + Angle2 + Angle3==180:
    print("The Triangle is Valid")
else:
    print("The Triangle is Not Valid")