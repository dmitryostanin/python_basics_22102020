def fact_gen(n):
    if n == 0:
        yield 1
    else:
        result = 1
        for num in range(1, n + 1):
            result *= num
            yield result


for index, item in enumerate(fact_gen(15), 1):
    print(f'{index}! = {item}')
