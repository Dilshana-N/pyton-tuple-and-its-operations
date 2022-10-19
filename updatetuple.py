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

# add items
fruits=("apple","mango","banana","kiwi")
fruits2=list(fruits)
fruits2.append("orange")
fruits=tuple(fruits2)
print(fruits)

# add tuple to a tuple
fruits=("apple","mango","banana","kiwi")
fruits2=("orange",)
fruits += fruits2

print(fruits)

# exaple 2
fruits=("apple","mango","banana","kiwi")
fruits2=("orange",)
fruits2 += fruits

print(fruits2)



