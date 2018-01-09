def fib(n):
    a = 0
    b = 1
    a,b=a,a+b
    print (a,b)
    c = a + b
    if c < n:
        for m in range(0, n):
            c = a + b
            a = b
            print(a, c)


fib(20)
