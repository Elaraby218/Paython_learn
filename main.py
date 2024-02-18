#print("helloklxc")

# strings

#first_name = "mohamed"
#last_name = "code"
#full_name = first_name + " " + last_name
#print(full_name)

# intgers

#age = 21
#age += 1
#print("your age is " +str(age))   # str(datatype) -- > casting to string
#print(type(age))

## Floats
#height = 250.234456456456456456456456456456456546456456456356746758456743758
#print("your height is " + str(height))
#print(type(height))

## Boolean data type
#human = True
#print(human)

## assign varuables
#name , age , attractive = "mohamed" , 21 , True
#print(name)
#print(age)
#print(attractive)

#a = b = c = d = 30
#print(a)
#print(b)
#print(c)
#print(d)


## string functinos

#name = "mohamed"
#print(len(name)) # --> str.size()
#print(name.find("hamed")) # ---> find substring or find char , return first idx of the finded str , char
#print(name.capitalize())  # --- > #capital anything
#print(name.upper())   # --- > #capital anything
#print(name.lower())    # --- > ! capital anything
#digitt = "024345653465674567678"
#print(digitt.isdigit()) # return true if the string consisting of digits
#print(digitt.isalpha())
#print(digitt.count('6'))
#print(digitt.replace('6','7'))

# Display string more than one time
#print(name*3)


# Type casting
#x,y,z = 1,2.0,"3"

#x=float(x)
#y=int(y)

#z=int(z)

#print(x)
#print(y)
#print(z*3)


### User Input
#x = input("What is your name?: ") # note that input will be string always
                                   # you need to cast it to your need
#age = int(input("What is your name:? "))
#tall= float(input("How tall are you:? "))

#print("Hello ",x, " Your age is ",age," years old , you are " , tall , " CM tall !")


# Math Functions
#import math
#pi = 3.14
#print(round(pi))
#print(math.ceil(pi))
#print(math.floor(pi))
#print(abs(pi))
#print(math.pow(pi,2))
#print(math.sqrt(pi))
#print(max(1,2,3,4,4,5,6,6,5,4,3,4,5))
#print(min(1,2,3,4,4,5,6,6,5,4,3,4,5))


# String slicing
# slicing = create a substring by extraction elements from another string
#          indexing[] or slice()
#          [start(inclusive):stop(exclusive):step]

#       01234567890123456789012345678
name = "mohamed ramadan elaraby ahmed"
second_name = name[8:15]
n = name[:10]  # start from idx 0 and end with idx 11
nn= name[10:]  # start from idx 10 and end with last idx
print(name)
print(n)
print(nn)
print("Your second name is " + second_name)

#reverse string using slicing
reversed_name = name[::-1]
print(reversed_name)

# Slice Function
# negative index is like indexing but from end to start

#           -7  -6  -5  -4   -3  -2  -1
# string =   M   o   h   a   m   e   d

website = "http://google.com"
slice = slice(7,-4)
print(website[slice])


