calls = 0

def count_calls():
    global calls
    calls += 1
    return

def string_info(stroka):
    count_calls()
    ss = []
    ss.append(str(len(stroka)))
    ss.append(stroka.upper())
    ss.append(stroka.lower())
    return tuple(ss)
def is_contains( string, list_to_search):
    count_calls()
    for i in list_to_search:
        if string.lower() == i.lower():
            return True
    return False

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)
