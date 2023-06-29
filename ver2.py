import math as math1
import random as random1

result_1 = math1.pow(2,4)
print("result 1 is", result_1)

result_2 = math1.sqrt(16)
print("result 2 is", result_2)

result_3 = random1.randint(0, 100)
print("result 3 is", result_3)

names = ["Emma", "Minghao", "Tianyao", "Yanhui", "Xiaosheng"]
print("Original names: ", names)

random1.shuffle(names)
print("names after shuffling: ", names)

result_4 = random1.choice(names)
print("Chosen name is: ", result_4)