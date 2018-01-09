'''定义一个展示质数列表的函数
'''

def show_prime_number_list(n):
    for x in range(2, n):
        for y in range(2, x):
            if x % y == 0:
                print(x, '=', y, '*', x // y)
                # print(x, 'equals', x, '*', x//y)
                break
        else:
            print(x, '是个质数')


show_prime_number_list(100)
