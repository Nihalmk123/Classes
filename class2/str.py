# Accessing individual characters in a string
str = "hello world"
print(str[0])   
print(str[1])   
print(str[-1])  
print(str[-3])  
print(str[-5:]) 
print(str[-5:-1]) 

# if string are lowercase
str1 = "learn python"
islower = str1.islower()  
print(islower)  

#  if string are uppercase
str2 = "LEARN PYTHON"
isupper = str2.isupper()  
print(isupper)  

# Slicing a string 
str3 = "welcome to python"
result = str3[0:7]  
print(result)  

# Joining characters 
str4 = "hello world"
result1 = "@".join(str4)  
print(result1)  

#  for range function 
for i in range(0, 5):  
    print(i)

for i in range(0, 10):  
    print(i)

# Stripping function to remove white space
str5 = "     python     "
result3 = str5.strip()  
print(str5)  
print(result3)  

# Using string formatting 
marks = 49
txt = "my marks are {}"
print(txt.format(marks)) 
