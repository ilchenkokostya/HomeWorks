# Генераторы

def all_variants(text):
    length = len(text)
    for x in range(length):
        for y in range(length - x):
            yield text[y:y + x + 1]


if __name__ == '__main__':
    a = all_variants("abc")
    for i in a:
        print(i)
