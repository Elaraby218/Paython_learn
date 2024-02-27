# **kwargs = paramerter that will pack all arguments into a dictionary
            # useful so that a function can accept a varying amount of keyword argument


def hello(**kwargs):
    print(kwargs['title'])
    print("hello" , end=" ")
    for key,value in kwargs.items():
        print(value,end=" ")

hello(title="mr.",first="bro",middle="dude",last="code")