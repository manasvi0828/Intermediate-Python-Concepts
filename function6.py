#variable length arguments
def myfunc1(*argv):
    for arg in argv:
        print(arg)

def myfunc2(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" %(key,value))

myfunc1("hello" , "welcome" , "to" , "geeksforgeeks")
myfunc2(first="geeks" , mid="for" , last="geeks")