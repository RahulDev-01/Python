# raise Exception("This is an error message")

try:
    x=7/0
except Exception as e:
    print(e)
finally:
    print("It will always execute")