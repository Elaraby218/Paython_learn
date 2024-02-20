# Function : a block of code which is executed only when it is called

def hello():
    for i in range(1,10):
        print("hello")


def hello(name):
    print("Hello " + name)

def hello(name , t):
    for i in range(1,t):
        print("Hello " + name)

def hello(fname , lname , age):
    print("Hello " + fname + " " + lname)
    print("you are " , age , " Years old")

fname,lname,age = input("Please insert your first name") , input("please insert your second name") , int(input("please insert your name"))
hello(fname,lname,age)
