def add(*args):
    return sum(element for element in args if isinstance(element, int) or isinstance(element, float))


print(add(1, 2, 3, 'hello'))

"""
X               y_hat       y               y - y_hat       |y - y_hat|         (y - y_hat) ^ 2
3 4 300         10_000      20_000          10_0000         10_000              10 ^ 8
2 4 150         5_000       4_000           -1_000          1_000               10 ^ 6
                                            9_000           11_000              101 * 10 ^ 6
"""