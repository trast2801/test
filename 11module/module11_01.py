import requests
# Конечная точка API
url = "https://jsonplaceholder.typicode.com/posts/1"
# GET-запрос к API
response = requests.get(url)
# Выводим ответ в консоль
response_json = response.json()
print(response_json)
#---------------------------------------------------------------------------
import pandas as pd

df = pd.read_excel('1.xlsx')
print(df.head(5),'\n')# вывод первых 5 строк
print(f'\n {df.info}')
print(f'\n {df.describe()}') #статистика

#---------------------------------------------------------------------------

import numpy as np

arr1 = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]]) # создание трехмерного массива
print(arr1)

#перебор одномерного массива
print('\n---------------')
arr1 = np.array([1, 2, 3])
for i in arr1:
    print(i * 6, end=' ')
print('\n---------------')
#перебор двухмерного массива
array2 = np.array([[1, 2, 3], [4, 5, 6]])
for x in array2:
    for y in x:
        print( y - 1, end=' ')
print('\n---------------')
#из многомерного в одномерный
newarr1 = array2.reshape(-1)
print(newarr1)
print('\n---------------')
#объединение массивов
finalarr = np.concatenate((arr1, newarr1))
print(finalarr)


import  matplotlib.pyplot as plt
#---------------------------------------------------------------------------
x = [1, 2, 3, 4, 5]
y = [25, 32, 34, 20, 25]

plt.plot(x, y)
plt.xlabel('Ось х') #Подпись для оси х
plt.ylabel('Ось y') #Подпись для оси y
plt.title('Первый график') #Название
plt.show()


vals = [24, 17, 53, 21, 35]
labels = ["Ford", "Toyota", "BMW", "Audi", "Jaguar"]

plt.pie(vals, labels=labels, autopct='%1.1f%%')
plt.title("Распределение марок автомобилей на дороге")
plt.show()

#---------------------------------------------------------------------------
from PIL import Image
import os

os.makedirs('watermarked_images')
logo_image = Image.open('watermark_logo.png')
logo_image = logo_image.resize((50, 50))
logo_width, logo_height = logo_image.size
for image in os.listdir('./images'):

    # Separting the filepath from the image's name
       path, filename = os.path.split(image)
       filename = os.path.splitext(filename)[0]
       with  Image.open('./images/' + image) as image:
           # Resizing the image to a set size.
           edited_image = image.resize((300, 300))
           # Setting the position for the placement
           width = edited_image.width
           height = edited_image.height
           edited_image.paste(logo_image, (width - logo_width, height - logo_height), logo_image)
           edited_image.save('./watermarked_Images/' + filename + ".jpg")



