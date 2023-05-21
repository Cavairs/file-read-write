import os
from pprint import pprint

file_path = os.getcwd()
# folder = 'OOP-file'
file_name = "recept.txt"
full_path = os.path.join(file_path, file_name)

with open (full_path, 'rt', encoding='utf-8') as recept:
    cook_book = {}
    for line in recept:
        recept_name = line.strip()
        quantity_count = int(recept.readline())
        ingredients = []
        for i in range(quantity_count):
             rec = recept.readline()
             split_result = rec.strip().split(' | ')
             ingredient_name, quantity, measure = split_result
             book = {
                 'ingredient_name': ingredient_name,
                 'quantity': quantity,
                 'measure': measure
             }
             ingredients.append(book)
        recept.readline()
        cook_book[recept_name] = ingredients
pprint(cook_book, sort_dicts=False)
print()
print()    


def get_shop_list_by_dishes(dishes, person_count):
    list = {}
    for dish in dishes:
        if dish in cook_book:
            ingredients = cook_book[dish]
            for ingredient in ingredients:
                   ingredient_name = ingredient['ingredient_name']
                   quantity = int(ingredient['quantity']) * person_count
                   measure = ingredient['measure']
                   if ingredient_name not in list:
                       list[ingredient_name] = {
                        'quantity': quantity,
                        'measure': measure
                    }                            
    return list

pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет', 'Утка по-пекински' ], 4))
