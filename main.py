import os
def read_cook_book():
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
    return cook_book


def get_shop_list_by_dishes(cook_book,dishes:list,person_count:int):
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
    print(shop_list)
cook_book = read_cook_book()
get_shop_list_by_dishes(cook_book,['Фахитос', 'Запеченный картофель'], 4)
            

def process_files(directory, output_file):
    file_data = {}
    
    for file_name in os.listdir(directory):
        file_path = os.path.join(directory, file_name)
        if os.path.isfile(file_path):
            with open(file_path, encoding='utf-8') as file:
                line_length = sum(1 for _ in file)
                file_data[line_length] = [file_name, line_length]
    
    sorted_data = dict(sorted(file_data.items()))
    
    with open(output_file, 'a', encoding='utf-8') as result_file:
        for value in sorted_data.values():
            result_file.write(f'{value[0]}\n')
            result_file.write(f'Строка номер {value[1]} файла номер {value[0]}\n')
    
    with open(output_file, encoding='utf-8') as result_file:
        print(result_file.read())

directory = 'C:/Users/CUCUBERPETYA/Desktop/rw_files'  
output_file = 'result.txt'
process_files(directory, output_file)
