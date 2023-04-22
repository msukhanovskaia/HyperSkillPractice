first, second, third = input(), input(), input()
if int(first) + int(second) + int(third) == 180:
    print("The triangle is valid!")
else:
    print("The triangle is not valid!")
# angles = sum([int(input()) for _ in range(0, 3)])
# print("The triangle is valid" if angles == 180 else "The triangle is not valid!")
