# kokoko = {"man": 12}, {"woman": 9}  # tuple with 2 dicts
# kokoko2 = dict({"man": 12}, woman=9)
# kokoko3 = {"man": 12, "woman": 9}
# print(kokoko, "\n", kokoko2, "\n", kokoko3)
#
# pets = {"dog": {"name": "lilo", "breed": "no"},
#         "cat": {"age": 5, "name": "kokp"}}
# print(f'{pets["cat"]["name"]} is {pets["cat"]["age"]} years old')
# print('{name} is {age} years old'.format(name=pets["cat"]["name"], age=pets["cat"]["age"]))
# import random
#
# # satellites = ["moon", "io", "cat"]
# # planets = ["earth", "venus", "mars"]
# #
# # # planets_dict = dict.fromkeys(planets, [])
# # # planets_dict["earth"] = satellites[0]
# # planets_dict = {key: [] for key in planets}
# # planets_dict["mars"].append(planets)
# # print(planets_dict)
#
# # student = {'name': 'Kate', 'age': 20, 'specialty': 'biology'}
# # student.update(degree='bachelor')
# # print(student)
# # print(student.get('age'))
# # print(student.pop('specialty'))
# # print(student)
# # print(student.popitem())
# # print(student)
#
# dictt = {"ann": 0, "marc": 3, "sisi": 88}
# print(random.choice(list(dictt.keys())))
# try:
#     1/0
# except(ZeroDivisionError):
#     # 1/0
#     ...
# finally:
#     print("It's OK.")

numbers = [1, 2, 3]
for num in numbers:
    if num == 5:
        print("It's 5!")
        break
else:
    print('5 was not listed')