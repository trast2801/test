
def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    if first == 0: #убирает последний значимый 0, если число зканчивается на 0, то произведение = 0
        first = 1
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first

print (get_multiplied_digits('40203050'))

