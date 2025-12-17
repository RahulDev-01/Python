# Map and Filter functions in Python
# Map function applies a given function to all items in an input list
# Filter function constructs a list from those elements of the input list for which a function returns true
x=[1,2,3,4,5,6,7,8,9,10]
# Using map and filter with lambda function
mp = map(lambda a:a*2 , x)
#  Using filter to get even numbers
ft = filter(lambda a:a%2==0 , x)

print(list(mp))
print(list(ft))
