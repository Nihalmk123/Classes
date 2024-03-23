tuple = ("apple", "banana", "cherry")
print(len(tuple))
print(tuple)

tuple1 = ("apple")
print(type(tuple1)) 

tuple2 = ("apple",)
print(type(tuple2)) 

tuple3 = (3,5,45,78)
print(tuple3[:4]) 
print(tuple3[2])

tuple4 = (3,"apple",5,"mango", 66 , "orange", "mango" )
print(tuple4.index("apple"))
print(tuple4.count("mango"))

tuple4[0]=5 #it is not possible since it is immutable
