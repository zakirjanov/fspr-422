                                                               # ТЕОРИЯ
# 1)
# integer - целый числа     
# float - числа с плавающей точкой
# boolean - данные принимающий или FALSE или TRUE
# # string - строки


# 2)
#   dictionary
#    gender_dict
# 3)
    #   В Pyton еть атрибут называемый MRO или атрибут который разрешает порядок методов в классе
    # порядок можно получить с помщью этого атрибута _mro_ 
# 4)
# git help 
# git help
# git clone
# git status
# git branch
# git checkout
# git merge
# git remote
# git fetch
# git push
# git pull  
    # 5)
        # Функция - это возвращающие значение какое-операции
        #  Функция-это подпрограма

        # Метод - процедура принадлежащей экзампляру класса или самому классу





                                                #   ТЕОРИЯ И ЗАДАЧИ
# 1)
#  x == z равно                      
#  x! = z не равно
#  x > z больше
#  x < z меньше
#  x >= z больше или равно
#  x <= z меньше или равно
#                                            ПРИМЕР                     

print("10" > "20")
print("10" < "20")


TRUE and  FALSE
#                                             ПРИМЕР

def is_correct_password(password):
    length = len(password)
    return length > 8 and length < 20

print(is_correct_password('swiftkey'))                   # => False
print(is_correct_password('swiftkey2004'))               # => True
print(is_correct_password('dhdsgjhdpfugwijhvbdis'))


# 2)
    #  ПОЛИМОРФИЗМ - одна из трех основных ооп
    #  полиморфизм метод производного класса не существующий на момент создания базы
 
#                                             ПРИМЕР

product ("table")

# 4)
    # Локаленая видимость
    #  Глобальная видимость

#                                             ПРИМЕР
# Локаленая область видимости
   
x = 100

def my_func(a, b):
    print(x)
    print(z)

my_func(1, 2)

 #  Глобальная область видимость
def my_func(a, b):
    global x
    print(x)
    x = 9
    print(x)


if name == 'main':
    x = 18
    my_func(1, 2)
    print(x)


# 5) 
#    РЕКУРСИЯ - определения проццеса внутри самиого проццеса(структуры)
def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
 
 
print(fibonacci(8))

