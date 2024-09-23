def apply_all_func(int_list, *functions):
    results = {}
    for function in functions:
        results[function.__name__] = function(int_list)
    return results


if __name__ == "__main__":
    print(apply_all_func([6, 20, 15, 9], max, min))
    print(apply_all_func([6, 20, 15, 9], len, sum, sorted))


    def squaring(int_list):
        result = map(lambda x: x ** 2, int_list)
        return list(result)


    def not_even(int_list):
        result = filter(lambda x: x % 2 != 0, int_list)
        return list(result)


    print(apply_all_func([6, 20, 15, 9], squaring, not_even))
