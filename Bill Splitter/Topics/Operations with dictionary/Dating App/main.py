def select_dates(potential_dates):
    date_list = ""
    for person in potential_dates:
        if person["age"] > 30 and person["city"] == "Berlin" and "art" in person["hobbies"]:
            date_list += person["name"] + ", "
    date_list = date_list[:-2]
    return date_list



potential_dates = [{"name": "Julia", "gender": "female", "age": 29,
                    "hobbies": ["jogging", "music"], "city": "Hamburg"},
                   {"name": "Sasha", "gender": "male", "age": 18,
                    "hobbies": ["rock music", "art"], "city": "Berlin"},
                   {"name": "Maria", "gender": "female", "age": 35,
                    "hobbies": ["art"], "city": "Berlin"},
                   {"name": "Daniel", "gender": "non-conforming", "age": 50,
                    "hobbies": ["boxing", "reading", "art"], "city": "Berlin"},
                   {"name": "John", "gender": "male", "age": 41,
                    "hobbies": ["reading", "alpinism", "museums"], "city": "Munich"},
                   {"name": "Kaka", "gender": "male", "age": 41,
                    "hobbies": ["reading", "alpinism", "museums", "art"], "city": "Berlin"}]
# print(select_dates(potential_dates))
# age > 30, art, berlin