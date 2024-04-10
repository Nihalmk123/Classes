lst = ["jack", "peeter", "james"]
enum = enumerate(lst) #to get an enumerate objectt
print(type(enum))
print(enum)


# Iterate over each element of the list along with its index and print
my_list = ['apple', 'banana', 'mango']
for index, item in enumerate(my_list):
    print(index)
    print(item)


# Iterate over each string in the list 
# and then iterate over each character in the string
#and convert them to uppercase
my_list1 = ["jhon", "peeter", "Devid"]
for s in my_list1:
    for i in s.upper():
        print(i)


# Iterate over each string in the list 
# and then iterate over each character in the string
#and convert them to lowercase
my_list1 = ["JHON", "PEETER", "DEVID"]
for s in my_list1:
    for i in s.lower():
        print(i)


# List comprehension
# Iterate over each string in the list 
# and then iterate over each character in the string
#and convert them to lowercase
my_list3 = ["JHON", "PEETER", "DEVID"]
lowercase_chars = [i for s in my_list3 for i in s.lower()]
print(lowercase_chars)


# List comprehension
# Iterate over each string in the list 
# and then iterate over each character in the string
#and convert them to uppercase
my_list4 = ["harry", "traver", "michle"]
lowercase_chars = [i for s in my_list3 for i in s.upper()]
print(lowercase_chars)

