cities = ["Lahore", "Multan"]
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

print("Type of 100 :",type(100),"\nType of 3.14 :",type(3.14),"\nType of Pakistan",type("Pakistan"),"\nType of True",type(True),"\nType of None",type(None));