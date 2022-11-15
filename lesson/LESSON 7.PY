# матрица

[2,3,4,5,6] # вектор
matrix = [[2,3,4],[5,6,7]] #матрица 3 столбца и 2 строки
print( matrix[1][1]) # 0 1 | 1 1 |

# 2  3   4
# 5   6  7
# random = list(1) # error
# random = list(true) # error

random = list("random  !)(*&^%$#") # error
splitted_string = "Split me ! ramdom".split("me !") # ' '
print(random, splitted_string,  ''.join(random),sep="\n")

    #    tuple  - кортеж
numbers = (2,3,4,5,6)
print(numbers,numbers[3])

# numbers[1] = "changief"
# читать создавать
numbers = (2, 3, 4, 5, [4, 5])
numbers[3][0] = 24
print(numbers[1])
