with open('recipes.txt',  encoding='utf-8') as f:
    cook_book = {}
    for i in f:
        name = i.strip()
        name_count = f.readline()
        ingredients = []
        for ing in range(int(name_count)):
            i1,i2,i3 = f.readline().strip().split('|')
            ingredients.append({'ingredient_name':i1, 'quantity':i2,'measure':i3})
        f.readline()
        cook_book[name] = ingredients
#print(cook_book)


def get_shop_list_by_dishes(dishes:list,person_count:int):
    shop_list = {}
    for dish in dishes:
        if dish in cook_book:
            for i in cook_book[dish]:
                if i['ingredient_name'] in shop_list:
                    shop_list[i['ingredient_name']]['quantity'] += int(i['quantity']) * person_count
                else:
                    shop_list[i['ingredient_name']] = {'measure':i['measure'],'quantity': int(i['quantity'])* person_count}
        else:
            print('Данного блюда нет:')
    #print(shop_list)
get_shop_list_by_dishes(['Утка по-пекински', 'Запеченный картофель'], 4)
            


new_dict = {}
with open('1.txt', encoding='utf-8') as file_1:
    file_name1 = '1.txt'
    count_name1 = len(file_1.readline())
    with open('2.txt', encoding='utf-8') as file_2:
        file_name2 = '2.txt'
        count_name2 = len(file_2.readline())
        with open('3.txt', encoding='utf-8') as file_3:
            file_name3 = '3.txt'
            count_name3 = len(file_3.readline())
            new_dict = {count_name1:[file_name1,count_name1],count_name2:[file_name2,count_name2],count_name3:[file_name3,count_name3]}
sort_dict = dict(sorted(new_dict.items()))
with open('result.txt', 'a', encoding='utf-8') as file_final:
    for value in sort_dict.values():
        for i in value:
            file_final.write(f'{i}\n')
            file_final.write(f'Строка номер {value[1]} файла номер {value[0]}\n')
with open('result.txt',encoding='utf-8') as file_result:
    print(file_result.read())
        
        
