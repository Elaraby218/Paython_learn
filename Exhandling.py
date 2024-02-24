
try:
    n = int(input("input first number "))
    d = int(input("input the second number "))
    res = n/d
except ZeroDivisionError as e:
    print(e)
    print("you cant divide by zero idiot! ")
except ValueError as e:
    print(e)
    print("Enter only numbers")
except Exception as e :
    print(e)
    print("something went wrong :( ")
else :
    print("THe res is {} ".format(res))
finally: #here any thing will be executed
    print("Nice to meet you")