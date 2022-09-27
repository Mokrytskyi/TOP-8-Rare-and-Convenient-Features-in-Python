#9 INTERESTING FEATURES IN PYTHON


# 1:
def func(* , a , b):
	pass
# you must to call function with keys becoarse in (def func) first argument is *
func(a = 1, b = 2)


# 2:
import jmespath # we can compare it wirh JSON object when we have big dictionary with big nesting (or something with .json)

people = {'people': [
					{'name': 'john', 'age':23},
					{'name': 'john', 'age':25},
					{'name': 'john', 'age':38}
	]
}
res = jmespath.search('people[*].age',people) # you can use it in parse
print(res) #[23,25,38]


# 3:
many people say that you can't add something to dict besides values, but we can :)
a = {'test' : {'a':True}, 'execute': lambda x: print(x)}

text = "Hello World"
a['execute'](text)


4: #this fir me cool too :) work with dict.

class Test:
	def __init__(self):
		print("Helo World")

a = {'test' : {'a':False}, 'execute': Test()}
b = {'test' : {'a':False}, 'execute': Test}

res = b['execute']()


# 5:
from collections import Counter

mylist = [1, 1, 2, 3 ,4 ,5 ,5 ,6 ,6] # how many times uses every value in list
c = Counter(mylist)
print(c)
#Counter ({1: 2, 5: 2, 6: 2, 2: 1, 3: 1, 4: 1})

print(Counter("AAAAnnnnooooo")) # here too
#Counter ({'o': 5, 'A': 4, 'n': 4})


# 6: #execution chain 
x = 10
if x > 5 and x < 15:
	print("work")

if 5 < x < 15:
	print("work")


# 7: #log parse
from dateutil.parser import parse

logline = 'INFO 2021-1-01T00:00:01 Happy New Year, Human!'
timestamp = parse(logline, fuzzy=True)
print(timestamp)

# 8: #if in one line
x = 10

num = 1 if x == 10 else 2
print(num)  







