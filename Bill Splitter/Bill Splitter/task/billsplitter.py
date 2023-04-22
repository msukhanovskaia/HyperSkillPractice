# write your code here
import random
friends_number = int(input("Enter the number of friends joining (including you):\n"))
if friends_number > 0:
    print("Enter the name of every friend (including you), each on a new line:")
    bill = {input(): 0 for _ in range(friends_number)}
    total_bill = float(input("Enter the total bill value:\n"))
    lucky = input('Do you want to use the "Who is lucky?" feature? Write Yes/No\n')
    if lucky == "Yes":
        lucky_one = random.choice(list(bill.keys()))  # bill.keys() is a class dict_keys type
        print('{name} is the lucky one!'.format(name=lucky_one))
        split_bill = round(total_bill / (friends_number - 1), 2)
        for key in bill:
            bill[key] = split_bill if key != lucky_one else 0  # type(key) = str
        print(bill)
    else:
        split_bill = round(total_bill / friends_number, 2)
        for key in bill:
            bill[key] = split_bill
        print("No one is going to be lucky\n", bill, sep="")
else:
    print("No one is joining for the party")
