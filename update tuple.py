# change the tuple values
x=("apple","mango","banana","kiwi")
y=list(x)
y[1]="cherry"
x=tuple(y)

print(x)

# example2
fruits=("apple","mango","banana","kiwi")
copyfruits=list(fruits)
copyfruits[1]="cherry"
fruits=tuple(copyfruits)

print(fruits)