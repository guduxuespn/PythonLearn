import string

str = 'hello World 123'
print(str)
print(string.capwords(str))
# print(string.whitespace(str))

# print(string.digits)

lett = str.maketrans('abcdefg', '1234567')
print(str.translate(lett))


