my_dict = {'Anzaur': 1992, 'Azamat': 1996, 'Khadira': 1997}
print(my_dict)
print(my_dict['Azamat'])
print(my_dict.get('Asker')) # - если писать код без "get", то выдает ошибку, поэтому добавил.
my_dict.update({'Dima': 1995, 'Anton': 1992})
my_dict.pop('Khadira')
print(my_dict)

my_set = {1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 'String', False, 'String', True, 'List', True, 'List'}
print(my_set)
my_set.add(6)
my_set.add('Apple')
my_set.remove(3)
print(my_set)