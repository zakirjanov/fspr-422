# # Интерируемые - iterable. Исчисляемый. Это те перемменные,которые хранят больше одного значения 
# # ИНдексы
# #    0 1 2 3
# names = [1,3,4,5] # 3
# print( type(names),names[3])
# names = ()
# print(type(names))

# # Dictionary - словарь
# # ключом словарь могут быть только не изменяемый и не перемменый
# user_data = {
#      "ключ": "значения",
#      1:None,
#      2: 21,
#      3: 67,
#      4: [2,3,4],
#      5: [1,2,3],
#      6: {"key": "другой словарь"}
#      # [1]: 23, # error
#      # (2,3,[2,3]):"Error,# кортеж можно использовать как ключ, но не рекомендуется"
#      }
# print(type(user_data),user_data,user_data["ключ"],sep="\n" )
# # print(type(user_data),user_data,user_data["ключ"],sep="\21" )

user_data = {
    "username": "Gooby",
    "password": "2rtr123r",
    "age":18, # hash qwertyrfsdz1235tgfs
    "age": 22, #qwertyrfsdz1235tgfs
}

print(user_data["age"])

user_data_2 = {
    "username": "Gooby",
    "password": "2rtr123r",
    "age": 18, # hash qwertyrfsdz1235tgfs
    "age": 22, #qwertyrfsdz1235tgfs
}

user_data = [
   { "username": "Gooby",
    "password": "2rtr123r",
    "age":18, 
   },
   {"username": "apo",
    "password": "2rtr123r",
    "age":14, 
   }
]
print(user_data[0]["username"],user_data[0]["age"])

user_data["username"] = "Alabasta"
print(user_data.keys(), user_data.values, user_data.items(),sep="\n")



 #view
#  dict_keys(['username','password','age']) - ['username','password','age']
# dict_values(['alabasta','2rtr123r',22]) - ['alabasta','2rtr123r',22]
# dist_items([('username','alabasta'),('password','2rtr123r),('age',22)])
# [('username','alabasta'),('password','2rtr123r),('age',22)]

user_list = list(user_data.values())
print(user_list)

remove_duplicalec