def get_value_from_list(object_list, separator, key):
    """Функция находит значение ключа key из списка object_list
    по разделителю separator
    :param object_list: список строк
    :param separator: разделитель
    :param key: искомый ключ"""

    # Объявляем переменную для хранения найденного значения
    value = None
    for element in object_list:
        # Итерируемся по каждому элементу из переданного списка object_list.
        # Каждый элемент разделяем на части, используя разделитель separator.
        # В итоге получим, что первый элемент - это ключ, второй элемент - это значение.
        words = element.split(separator)
        if words[0] == key:
            # Если первый элемент равен искому ключу key, то обновляем значение value и выходим из цикла
            value = words[1]
            break

    # Возвращаем найденное значение
    return value


# Журнал регистрации
log = """name:Иван;gender:m;item:Часы;item_cost:9800
name:Иван;gender:m;item:Фитнес-браслет;item_cost:12300
name:Иван;gender:m;item:Кофемашина;item_cost:23500
name:Петр;gender:m;item:Часы;item_cost:9800
name:Петр;gender:m;item:Фитнес-браслет;item_cost:12300
name:Петр;gender:m;item:Айфон;item_cost:77900
name:Петр;gender:m;item:Чехол для телефона;item_cost:350
name:Петр;gender:m;item:Кофемашина;item_cost:23500
name:Дарья;gender:m;item:Айфон;item_cost:77900
name:Марья;gender:m;item:Кофемашина;item_cost:23500
name:Юлия;gender:m;item:Фитнес-браслет;item_cost:12300"""

# Делим журнал регистрации log на список строк по разделителю - перенос строки.
# Полученный результат сохраняем в список records
records = log.split('\n')

list_low_cost = {}
for el in records:
    elements = el.split(';')
    item_title = get_value_from_list(elements, ':', 'item')
    item_cost = int(get_value_from_list(elements, ':', 'item_cost'))

    if item_cost < 13000 and item_title not in list_low_cost.keys():
        list_low_cost[item_title] = item_cost

print('Список товаров с ценой < 13000')
for k, v in list_low_cost.items():
    print(f'{k}: {v}')