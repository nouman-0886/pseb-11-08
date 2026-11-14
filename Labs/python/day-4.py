cities = ["Lahore", "Multan", "Lahore", "Karachi", "BWP"]
# print(cities[1])
cities[1] = "Islamabad";
# print(cities)


(stuRoll,stuName, depart) = (123, "Kamran", "SE")
# print("Student Name :", stuName ,"\nSutdnet RollNO. :", stuRoll, "\nStudent Depart :", depart);
depart = "Cyber Security";
# print("Student Name :", stuName ,"\nSutdnet RollNO. :", stuRoll, "\nStudent Depart :", depart);



#**************Shallow Copy  Deep Copy
import copy
a = [[1, 2], [3, 4]]
b = copy.copy(a)
c = copy.deepcopy(a)
a[0][0] = 99
# print(a)
# print(b) # [[99, 2], [3, 4]]
# print(c) # [[1, 2], [3, 4]]


# **********type() of 100, 3.14, "Pakistan", True and None

# print("Type of 100 :",type(100),"\nType of 3.14 :",type(3.14),"\nType of Pakistan",type("Pakistan"),"\nType of True",type(True),"\nType of None",type(None));

# ************TYpe casting

x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2

pi = 3.14
# print(pi, type(pi))
newpi = int(pi)

# print(pi, type(newpi))



complexNum = 3+5j
# print(complexNum, type(complexNum)) 
real = int(complexNum.real)
# print(real)

newNum = str(real)  # Convert integer to string
# print(newNum, type(newNum))  # Output: 3 <class 'str' >

# *******Decimals

# print(0.1 + 0.2+ 0.3)
# print(round(3.14159, 2))
from decimal import Decimal
# print(Decimal("0.1") + Decimal("0.2")+ Decimal("0.3"))


# *********Random

import random

rndm = random.randint(1,10)
# print(rndm)

# chose = random.choice(cities)
# print(random.choice(cities))
print(random.uniform(1.5, 5.5))

