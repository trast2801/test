data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]
summa = 0
flag = True
def calculate_structure_sum(element):
    global  flag
    if not element: # возвращает пустой набор если список закончился
        return []
    elif isinstance(element[0], int):  # если элемент целое число,
          # то оно присваивется к переменно)
        global summa
        summa += element[0]

        return  [element[0]] + calculate_structure_sum(element[1:])  # возврщает сумму этого числа и предыдущего

    elif isinstance(element[0], str):
        summa += len(element[0])
        return calculate_structure_sum(element[1:])

    elif isinstance(element[0], list):

        calculate_structure_sum(element[0]) # Передает элемент вложенного списка в рекурсию
        return calculate_structure_sum(element[1:]) # возвращает последующий элеиент исходного списка

    elif isinstance(element[0], dict):
        for i in element[0]:
            summa += (element[0].get(i)) # нужно ли проверять что в
        return calculate_structure_sum(element[1:])   # значениях словаря толкьо цифры?

    elif isinstance(element[0], tuple):

        calculate_structure_sum(element[0])
        return calculate_structure_sum(element[1:])


#result = calculate_structure_sum(data_structure)
#print(result)

test_list = ['gfg', 1, 2, 'is', 'best']
'''
data_structure = [

                  (
                      [
                          {
                              (2, 'Urban',
                                 (
                                     'Urban2', 35
                                 )
                              )
                          }
                      ]
                  )
                ]

'''
result = calculate_structure_sum(data_structure)
print("Summa ", summa)

