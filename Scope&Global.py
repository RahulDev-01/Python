# Global variable
x='Rahul'
def func(name):
    # Local variable
    x=name
    print(x)
print(x)
func('Changed')
# print(x)

