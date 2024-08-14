def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')

    inner_function()


if __name__ == '__main__':
    test_function()

    try:
        inner_function()
    except Exception as Error:
        print(Error)
