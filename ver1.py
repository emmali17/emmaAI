from math import pow
from math import sqrt
from random import randint
from random import shuffle
from random import choice

result_1 = pow(2,4)
print("result 1 is", result_1)

result_2 = sqrt(16)
print("result 2 is", result_2)

result_3 = randint(0, 100)
print("result 3 is", result_3)

names = ["Emma", "Minghao", "Tianyao", "Yanhui", "Xiaosheng"]
print("Original names: ", names)

shuffle(names)
print("names after shuffling: ", names)

result_4 = choice(names)
print("Chosen name is: ", result_4)