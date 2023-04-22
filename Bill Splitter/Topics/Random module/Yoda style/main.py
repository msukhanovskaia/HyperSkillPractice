import random

# your sentence is assigned to the variable
sentence = input().split()

# write your python code below
random.seed(43)
random.shuffle(sentence)

# shows the message
print(' '.join(sentence))


catalog = {'green table': 5000, 'brown chair': 1500, 'blue sofa': 15000, 'wardrobe': 10000}

import operator

catalog_sorted_by_key = dict(sorted(catalog.items(), key=operator.itemgetter(0)))
# {'blue sofa': 15000, 'brown chair': 1500, 'green table': 5000, 'wardrobe': 10000}

catalog_sorted_by_value = dict(sorted(catalog.items(), key=operator.itemgetter(1)))
# {'brown chair': 1500, 'green table': 5000, 'wardrobe': 10000, 'blue sofa': 15000}

catalog_sorted_by_value_reverse = dict(sorted(catalog.items(), key=operator.itemgetter(1), reverse=True))
# {'blue sofa': 15000, 'wardrobe': 10000, 'green table': 5000, 'brown chair': 1500}
