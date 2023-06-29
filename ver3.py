from math import pow as power
from math import sqrt as squareroot
from random import randint as randomint
from random import shuffle as shuffleitems
from random import choice as choose

result_1 = power(2,4)
print("result 1 is", result_1)

result_2 = squareroot(16)
print("result 2 is", result_2)

result_3 = randomint(0, 100)
print("result 3 is", result_3)

names = ["Emma", "Minghao", "Tianyao", "Yanhui", "Xiaosheng"]
print("Original names: ", names)

shuffleitems(names)
print("names after shuffling: ", names)

result_4 = choose(names)
print("Chosen name is: ", result_4)