
import os
import time

directory = 'd:\\44444' # Замените на путь к вашему каталогу
count_of_dir = 0
count_of_files = 0
count_of_all = []
for root, dirs, files in os.walk(directory):
  count_of_dir += 1
  count_of_local_files = 0
  for file in files:
    count_of_files += 1
    count_of_local_files += 1
    filepath = os.path.join(root, file)
    filetime = os.path.getmtime(filepath)
    formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
    filesize = os.path.getsize(filepath)
    parent_dir = os.path.dirname(filepath)
    print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт,'
          f' Время изменения: {formatted_time}, Родительская директория: {parent_dir}')
  count_of_all.append(f' в директории {root} содержится {count_of_local_files}')
print('\n')
for content in count_of_all:
    print(content)
print(f' \n Всего кол-во Директорий {count_of_dir}\n Общее кол-во файлов {count_of_files}')
