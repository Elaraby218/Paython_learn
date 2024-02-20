# return statement = Functions send python values objects back to the caller.
#                    these values/objects are known as the function's return value

def summation(n):
    return (n*(n+1))/2

#print(int(summation(10)))

# Factorial using recursion
def fact(n):
    if n==1 :
        return 1
    return n*fact(n-1)
