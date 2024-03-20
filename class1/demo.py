# movies = []
# movie1 = input("enter a movie1:")
# movie2 = input("enter a movie2:")
# movie3 = input("enter a movie3:")
# movies.append(movie1)
# movies.append(movie2)
# movies.append(movie3)
# print(movies)

# list  = [3,3,3] 
# copied_list = list.copy()
# revese_list = copied_list.reverse()

# if(copied_list == list):
#     print("palindrome")
# else:
#     print("non palindrome")

# students = ["c","d","a","a","b","b","a"]
# print(students.count("a"))

# students = ["c","d","a","a","b","b","a"]
# students.sort()
# print(students)

lst = [0,1,1,1,0,0]
result = []

for i in lst:
    if i == 0:
        lst.append(i)
print(result)