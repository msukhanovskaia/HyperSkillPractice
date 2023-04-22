# put your code here
# number = input()
# print("-" + number + "\nThe number is negative" if int(number) > 0 else str(abs(int(number))) + "\nThe number is positive")

number = int(input())
print(-number, "The number is negative" if number > 0 else "The number is positive", sep="\n")
