from http import cookies


stuff = {"food": 15, "energy": 100, "enemies": 3}

"""
print(stuff.get("food")) #shows value of the key searched for
print(stuff.items()) #key/value pairs
print(stuff.keys()) #just key elements 

print(stuff.popitem()) #removes last key item
print(stuff)

print(stuff.setdefault("food"))
print(stuff)
print(stuff.setdefault("friends", 123))
print(stuff)"""

new_items = {"rocks": 4, "arrows": 18}
stuff.update(new_items)
print(stuff)

up_new = {"food": 3, "webs": 2}
stuff.update(up_new)
print(stuff)

stuff.update(food = 450, cookies = 6)
print(stuff)