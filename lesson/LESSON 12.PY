# info = []
# for i in range(2):
#     name = input("input name:")
#     age = int(input("input age:"))
#     info.append(
#         {
#             "age": age,
#             "name" : name
#         }
#     )


# result = []
# faranheits = [20, 140, 19, 24, 45]
# for far in faranheits:
#      celsius = (far - 32) * 5 / 9
#      if celsius >= 50:
#         print("Слишком горячо")
#         break
#      elif celsius  <= 5:
#          print("Жить можно")
#      result.append(celsius)

# print(result)


# **** 
# *  * 
# *  * 
# **** 
square_line = 4 
star = "*" 
star_width = star * square_line 
print(star_width) 
print(f"{star}  {star}") 
print(f"{star}  {star}") 
print(star_width) 
for i in range(square_line): 
    # print(star, end="") 
    if i > 0 and i < (square_line - 1):
        empty_space = "" * (square_line - 2)
         #          "*   *"
         #          "*   *"
         #          "*   *"
         #          "*   *"
        print(f"{star}{empty_space}{star}")
    else:
        print(star * square_line)   

i = 0
while True:
    i += 1
    print("i =", i)
    if i == 100:
        break

names = [1,2,3,4,5,6]
i = 0
while i < len(names):
    print(names[i])
    i += 1            



    