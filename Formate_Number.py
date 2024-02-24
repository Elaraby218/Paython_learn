
# Hoe to control the number of digits of the float number
# just use format wiht .:numbers(f)
number = 3.14659
print("The pi is equal to : {:.2f} ".format(number))


# to print the binary representation
number = 10
print("The binary {:b}".format(number))
# to print octal
print("Tho Octal {:o}".format(number))
# to print dexadicimal
print("The hexa {:X}".format(number))
# to print thausands
number = 1000000000
print("{:,}".format(number))
#print nuber in scientific notation
print("this is the {:e}".format(number))