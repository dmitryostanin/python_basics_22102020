from functools import reduce


def sum_func(el_prev, el):
    return el_prev + el


print(reduce(sum_func, [number for number in range(100, 1001) if number % 2 == 0]))
