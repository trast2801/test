

def is_prime(func):
    def wrapper(*args, **kwargs):
        s = func(*args, **kwargs)
        #print(s)
        marker = 0
        for i in range(2, s // 2 + 1):
            if (s % i == 0):
                marker += 1
        if marker <= 0:
            return f'{s} простое'
        else:
            return f'{s} составное'
    return wrapper

@is_prime
def sum_three(one, two, three):
    return one + two + three


result = sum_three(2, 3, 6)
print(result)

