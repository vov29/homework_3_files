def get_shop_list_by_dishes(dishes, person_count):
    new_menu = {}
    for i in dishes:
        for key in cook_book:
            if key == i:
                for j in cook_book[key]:
                    if j['ingredient_name'] in new_menu:
                        new_menu[j['ingredient_name']]['quantity'] += int(j['quantity']) * person_count
                    else:
                        new_menu[j['ingredient_name']] = {'measure': j['measure'],
                                                          'quantity': int(j['quantity']) * person_count}
    sorted_menu = dict(sorted(new_menu.items()))
    return sorted_menu


cook_book = {}
lst = []
with open('recipes.txt', 'r', encoding='utf-8') as file:
    for line in file:
        elements = line.strip().split('|')
        lst.append(elements)

for i in range(len(lst)):
    if len(lst[i]) == 1 and not lst[i][0].isdigit() and lst[i][0] != '':
        key = lst[i][0]
        cook_book[key] = []
    if len(lst[i]) == 3:
        cook_book[key].append({'ingredient_name': lst[i][0], 'quantity': lst[i][1], 'measure': lst[i][2]})

# print()
# for key in cook_book:
#     print(key, cook_book[key])
#     print()

print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
