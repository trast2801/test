

def is_prime(func):
    def wrapper(*args, **kwargs):
        s = func(*args, **kwargs)
        #print(s)
        if s == -1:
            print(f'ожидались числа > 0')
            return 0
        marker = 0
        for i in range(2, s // 2 + 1):
            if (s % i == 0):
                marker += 1
        if marker <= 0:
            print(f'{s} простое')
            return s
        else:
            print(f'{s} составное')
            return s
    return wrapper

@is_prime
def sum_three(one, two, three):
    if one < 0 or two < 0 or three < 0:
        return -1
    return one + two + three


result = sum_three(2, 3, 6)
print(result)

