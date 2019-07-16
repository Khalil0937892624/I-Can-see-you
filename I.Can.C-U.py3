from datetime import *
	
date = datetime.today()

d = date.day 

m = date.month

y = date.year

print (date)

print (d,m,y)

dob = int (input ("Enter your year when you born:"))

age = int (y) - int (dob)

print ("Your age is: ",age)