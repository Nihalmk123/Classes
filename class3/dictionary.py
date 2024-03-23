person = {
  "name": "nihal",
  "age": 23,
  "hobby": "cricket"
}

result = person.get("name") #print the element of key "name"
result1 = person.items() #Returns a list containing a tuple for each key value pair
result2 = person.keys() #Returns a list containing the dictionary's keys
result3 = person.values() #	Returns a list of all the values in the dictionary

print(result)
print(result1)
print(result2)
print(result3)


#update the dectionary
students = {
  "name": "nihal",
  "age": 23,
  "hobby": "cricket"
}

students.update({"age": 53})
students.update({"name": "mohammadnihal"})
print(students)


#pop delete the the element and key model and mustang
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.pop("model")
print(car)

#popitem pop the last elemt from dictionary
laptop = {
  "brand": "Asus",
  "model": "Asus Tuff dash",
  "Ram" : "8gb"
}

laptop.popitem()
print(laptop)