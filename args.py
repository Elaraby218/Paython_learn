# *args = parameter that will bpack all arguments into a tuple
        # useful so that a function can accept a barying amount of arguments

def add(*args):
    sum = 0
    for i in args:
        sum+= i
    return sum

print(add(1,2,3,4,5,6,7,8,9,10))