#Loop through each argument passed to the function and Print each argument
def myFun(*argv):
	for arg in argv:
		print(arg)

myFun('Hello', 'Welcome', 'to', 'pune')

# Print the first argument arg1, 
# Loop through the remaining arguments *arg and print them
def myFun(arg1, *arg):
	print("First argument :", arg1)
	for b in arg:
		print(b)

myFun('Nihal', 'Welcome', 'to', 'hubli')

# Print the first argument arg1, 
# Loop through the remaining arguments *arg and print them
def print_info(name, *details):
    print("Name:", name)
    print("-----details-----")
    for detail in details:
        print("-", detail)

print_info("Nihal", "Age: 22", "Occupation: Engineer", "Location: Pune")
