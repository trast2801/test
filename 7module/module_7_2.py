def custom_write(file_name, strings):
    strings_positions = {}
    ind = ()
    with open(file_name, 'w+', encoding='utf8') as fs:
        count_str = 1

        for i in strings:
            ind = count_str, fs.tell()
            fs.write(i+'\n')
            strings_positions[ind]= i
            count_str += 1
    return strings_positions
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

ss = {}
ss = custom_write('text.txt',info)
for key, value in ss.items():
    print(key, value)