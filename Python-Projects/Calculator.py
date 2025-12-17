def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    if y==0:
        print("Division Cannot Proceed")
    return x/y

def get_number():
    x= int(input("Enter First Number : "))
    y= int(input("Enter Second Number : "))
    return x,y
 