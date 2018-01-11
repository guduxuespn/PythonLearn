'''定义一个展示质数列表的函数
'''
def show_prime_number_list(n):
    for x in range(2, n):
        for y in range(2, x):
            if x % y == 0:
                return(x, '=', y, '*', x // y)
                # print(x, 'equals', x, '*', x//y)
                break
        else:
            return(x, '是个质数')


print(show_prime_number_list(100))


# 定义一个函数，将传入的字符串变为首字母大写的一个字符串
def my_capitalize(s):
    s1 = s.split()
    for i in range(0, len(s1)):
        return(s1[i].capitalize())


my_capitalize('hello world , Hello python')


def power (m,n):
    
    return(m**n)

print(power(2,4))