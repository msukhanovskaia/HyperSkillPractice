# the list "meals" is already defined
# your code here
# meals = [
#         {"title": "Oatmeal pancakes with apple and cinnamon", "kcal": 370},
#         {"title": "Italian salad with fusilli and ham", "kcal": 320},
#         {"title": "Bulgur with vegetables", "kcal": 350},
#         {"title": "Curd souffle with lingonberries and ginger", "kcal": 225},
#         {"title": "Oatmeal with honey and peanuts", "kcal": 440}]

sum_result = 0
for meal in meals:
    sum_result += meal.get('kcal')

# {"kcal": sum_result}
print(sum_result)
# sum([value.popitem()[1] for value in meals])
# kcal_sum = sum(meals[i]["kcal"] for i in range(0, (len(meals))))
# kcal_sum = sum([value.get('kcal') for value in meals])
# kcal_sum = sum([value['kcal'] for value in meals])
# print(kcal_sum)
