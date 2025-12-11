def greet():
    print("Hello Rahul")
greet()

def add(x,y):
    z=  x+y
    # print(z)
add(5,5)

def sub(x,y):
    return x-y
result = sub(10,5)
print(result)


def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n * factorial(n-1)
# print(factorial(5))

