Side1 = int(input("Enter Length of 1st Side"))
Side2 = int(input("Enter Length of 2nd Side"))
Side3 = int(input("Enter Length of 3rd Side"))
if Side1<=0 or Side2<=0 or Side3<=0:
    print("The Triangle is Not Valid")
elif Side1 + Side2 > Side3 and Side1 + Side3 > Side3 and Side2 + Side3 > Side1:
    print("The Triangle is Valid")
else:
    print("The Triangle is not Valid")