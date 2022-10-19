# unpacking a tuple
fruits=("apple","mango","banana")
(a,b,c)=fruits

print(a)
print(b)
print(c)

# asterisk*
fruits=("apple","mango","banana","cherry")
(a,b,*c)=fruits

print(a)
print(b)
print(c)

# example 2
fruits=("apple","mango","banana","cherry","jackfruit")
(a,*b,c)=fruits

print(a)
print(b)
print(c)





