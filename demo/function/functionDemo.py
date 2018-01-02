from functools import reduce


def square(x):
    return x * x


print(square(5))

# python内建的map函数使用示例
r = map(square, [4, 3, 7, 12, 34, 6])
print(list(r))

# python内建的reduce函数


def fn(x, y):
    return x * 10 + y


reduce(fn, [2, 4])

reduce(fn, [2, 4, 1, 7, 5])
