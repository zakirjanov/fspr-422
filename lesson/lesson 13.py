# вызов функции 
if 1 == 1:
   print(True)

def greet():
   print("Hello")

print("вызов функция",greet())

def greet():
   return"hello" 

result = greet()
print(result)

def greet(name):
   print(f"Hello(name)")

greet("Behruz")
s = "Bekzod"
greet(s)
greet(input("Input name: "))

def greet():
    return f"Hello (name)"