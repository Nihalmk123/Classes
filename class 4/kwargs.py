# keyword arguments kwargs

def myFun(**kwargs):
	for key, value in kwargs.items():
		print(key, value)

myFun(firstName='jhone', midName='dev', LastName='michle')

# keyword arguments kwargs

def my_function(**kwargs):
  print(kwargs["firstname"])
  print(kwargs["lastname"])

my_function(firstname = "nihal", lastname = "Mk")