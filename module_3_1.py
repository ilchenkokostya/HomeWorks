calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    result = (len(string), string.upper(), string.lower())
    return result


def is_contains(string, lst):
    count_calls()
    for i in lst:
        if str(i).lower().count(string.lower()):
            result = True
            break
        else:
            result = False
    return result


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)
