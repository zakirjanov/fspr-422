















# is и ==
a = (2,3,4)
b = (2,3,4)
print(a is b, a== b) # false | true

b = [2,3,4]
b.append(23) # [2,3,4,23]
a = [2,3,4]
print(a is b , a == b)

# a  Это b. b это  a
a = [2,3,4]
b = a
b.append(43)
print("a =", a, "b =", b)

#  с копированием
a = [2, 3, 4, ]
b = a.copy()
b.append(43)
print("a =", a, "b=", b)

#  с копированием
a = [2,3,4[2,3]]
b = a.copy()
b[2]
b[3][1] = 12 # 0 1 3
print("a =", a, "b =", b)

# модуль для глубокого копирования
import copy

a =[2,3,4, [2,3]]
b = copy.deepcopy
b[2]
b[3][1] = 12 
print("a =", a, "b =", b)

a =[2,3,4, [2,3]]
b = copy.deepcopy
b[2]
b[3][1] = 12 
print("a =", a, "b =", b)

print(type("qwerty"),str,"qwerty"==str)

val = (input)
if type(val)==int or type(val)==str:
   print(True)
else:
   print(False)


print("list")
numbers = [1,2,3,4,5,6,7]
for num in numbers:
    print(num + 2)

print("tuple")
numbers = (1,2,3,4,5,6,7)
for num in numbers:
    print(num + 2)

print("set")
numbers = (1,2,3,4,5,6,7)
for num in numbers:
    print(num + 2)

print("dict")
user = {
    "name": "George",
    "age": 25,
    "skill": "swim",
}
for key in user:
    print(key)

print("dict vals")
for val in user.values():
    print(val)

print("\ndict items")
for key, val in user.values():
    print("key =", key, "val =", val)
#       0                  1            2
# [("name": "George"),("age": 25,"skill") ("swim",)]
print(user.item())
a, b = 2, 4
print(a,b)

a, b = [20, 40]
print(a, b)