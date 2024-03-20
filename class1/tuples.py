tuple1 = (1,2,4,6,7,66,"hello","world")
print(tuple1)
print(type(tuple1))
print(len(tuple1))

tuple2 = (5,89,45,3,25,36)
print(tuple2[:4]) 
print(tuple2[5])
# tuple2[0]=5 #not possible because it is immmutable4
print(tuple2)

tup3 = (1,5,6,4,5)
print(tup3.index(6)) #get the index of the element
print(tup3.count(5))