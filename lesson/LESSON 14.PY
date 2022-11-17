
def shades_of_grey(n):
    shades = []
    hex = "123456789abcdef"
    counter = 0
    for i  in range(n):
        if counter == 15:
            counter = 0
        gray = f"#0{hex[counter]}0{hex[counter]}0{hex[counter]}"
        if i >= 15: 
            gray = f"#0{hex[counter]}0{hex[counter]}0{hex[counter]}"
        shades.append(gray)
        counter += 1 
    return shades
print(shades_of_grey(50))    

def create_list(n, num):
    numbers = []
    for i in range(n):
        numbers.append(i * num)
 
def func(a, default="hi"):
     print(a,default)


def func(a,b, default="hi"):
     print("a=", a, "b=", b ,default)


def func(a, default="hi" *args):
    print(a,b, "default=", default,"args=",arga)

def ane_arg(*args):
    print("args =", args)
    for arg in args:
        print(arg)
any_arg(2, 3, 4, "goooooooo", "noooo",{1:1})