Side1 = int(input("Enter Length of 1st Side"))
Side2 = int(input("Enter Length of 2nd Side"))
Side3 = int(input("Enter Length of 3rd Side"))
if Side1<=0 or Side2<=0 or Side3<=0:
    print("The Triangle is Not Valid")
elif Side1 + Side2 <= Side3 or Side1 + Side3 <= Side2 or Side2 + Side3 <= Side1:
    print("The Triangle is Not Valid")
else : 
    if Side1 == Side2 == Side3 :
        print("The triangle is Equilateral")
    elif Side1 == Side2 or Side1 == Side3 or Side1 == Side3:
        print("The Triangle is isosceles")
    else : 
        print("The Triangle is Scalene")