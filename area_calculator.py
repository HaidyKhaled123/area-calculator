str_length=input("please type length:\n")
str_width=input("please type wide:\n")
price=input("who much for 1 meter?;\n")
#convert type
length=float(str_length)
width=float(str_width)
price=float(price)
area=length*width
print("the total area is :",area)
print ("give the guy :$",(round(area,2)))
