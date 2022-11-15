"""









"""
# is, ==
# is - сравнивает id двух значений
# id()
a = 1
b = 1
print(id(a), id(b))

t_1 = ()
t_2 = ()
#print( id(t_1), id(t_2))
print( t_1 == t_2)
print( "tuple", t_1 is t_2) # False
# print("1 == 1", 1 == 1, 1 is 1)

# изменяймые типы данных
# [] []
l_1 = [1, 2] #1234567
l_2 = [1, 2] #8765432
print(1_1 == 1_2)
print(1_1 is 1_2)

d_1 = {1: 1}
d_2 = {1: 2}

print("dict", d_1 == d_2)
print("dict", d_1 == d_2)

# print(1_1, id(1_1), 1_2, id(1_2) )







name = "Jamshid"
skill = "b1"
age = "17"
surname = "Zakirjanov"

if name == "sardor" and skill == "D2": # AND - и
      print(name, skill)
else:
    print("AND")
    
if name == "sardor" and skill == "D2": # or - или
      print(name, skill)
else:
    print("Or")

# not - не
if not age: # not -> False - true
    print(age)
else:
    print("Age is False")


# не писать
#                   TRUE                      FALSE
#         TRUE            FALSE
if(name == "Jamshid" and age > 17) or skill == "B1":
    print(name,age,skill)
else:
    print("Inavlid name, age, skill")

if(name == "Jamshid" and age > 17) or skill == "B1":
    print(name,age,skill,"second output")
else:
    print("Inavlid name, age, skill")

# bool
# TRUE | FALSE
# любой числочто не ноль - это правда(TRUE)
# если переменная путсая - то оно ложь(FALSE)

# TRUE = 1 False = 0

print(False * 3)
x = 10
y = 20
if x > y:
     print(True)
else:
    print(False)

"name surname".split() # ['name', 'surname']
# a if condition else b
print( True if x > y  else False)

# ==, !=, >, >=, <, <=, is, is not, in, not in, not, and, or

# [], {}, ()  ""  0

if[]: #True
    print(True)

if -19: #True
    print(True)





