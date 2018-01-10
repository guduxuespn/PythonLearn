# 该函数可以输出n以内的斐波那契数列
# 

def fib(n):
    a = 0
    b = 1
    while b < n:
        print(a)
        a, b = b, a + b


fib(20)
