# read line string
name = input("name : ")
print("hi %s" % name)
# read int from input()
age = int(input("your age :"))
print("%s is aged %d" % (name, age))
# read float from input()
weight = float(input("your weight :"))
print("%s at age %d is weighed at %f pounds" % (name, age, weight))

# read array as a string and split based on a delimitter
array_of_weights = input("enter weights : ").split(" ")
# we needed a list of integers but we are seeing list of strings
print(array_of_weights)
array_of_weights = list(map(int, input("Enter weights :").split(" ")))
print(array_of_weights)
# read Line from string
