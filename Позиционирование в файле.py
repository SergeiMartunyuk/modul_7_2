import io
from  pprint import pprint

def custom_write(file_name, strings):
    strings_positions = {}
    str_number = 1
    file = open(file_name, 'w', encoding='utf-8')
    file.seek(0)
    for i in strings:
        str_byte = file.tell()
        file.write(f'{i}\n')
        strings_positions[(str_number, str_byte)] = i
        str_number += 1
    file.close()
    return strings_positions

info = [
        'Text for tell.',
        'Используйте кодировку utf-8.',
        'Because there are 2 languages!',
        'Спасибо!'
        ]
result = custom_write('test.txt', info)
for elem in result.items():
        print(elem)
