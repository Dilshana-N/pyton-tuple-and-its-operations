# print specified item in tuple
flowers=("sunflower","jasmin","lilly","lotus")
print(flowers[2])

# -ve indexing
flowers=("sunflower","jasmin","lilly","lotus")
print(flowers[-4])

# range of indexes
flowers=("sunflower","jasmin","lilly","lotus")
print(flowers[1:4])

# example 2
flowers=("sunflower","jasmin","lilly","lotus")
print(flowers[:4])

#example 3
flowers=("sunflower","jasmin","lilly","lotus")
print(flowers[2:])

# negative indexes
flowers=("sunflower","jasmin","lilly","lotus")
print(flowers[-4:-1])

# check if item exists
flowers=("sunflower","jasmin","lilly","lotus")
if "sunflower" in flowers:
    print("yes,'sunflower' is in the tuple")

