initial_quantity = int(input())
final_quantity = int(input())
# hl_periods = initial_quantity // final_quantity
# days = hl_periods * 12
# print(days)
hl_periods = 0
while initial_quantity >= final_quantity:
    hl_periods += 1
    initial_quantity /= 2

print(hl_periods * 12)
