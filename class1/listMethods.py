list = [1,2,5,8,65]
list.append("nihal") #insert new value at the end of the list
print(list)

list2 = [55,542,697,3214,5,8,6]
sorted_list = list2.sort() #sort list in ascending order
print(list2)
sorted_list = list2.sort(reverse=True) #sort list in descending order
print(list2)

list3 = ["a","b",4,2.5,100]
list3.insert(0, "n") #insert new value at index 0
list3.reverse() #reverse the list
print(list3)

list4 = [2,5,2,1]
list4.pop(0) #remove element of index 0
list4.remove(5) #remove element of 5 from the index
print(list4)