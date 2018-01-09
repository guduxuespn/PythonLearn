import re

m = re.match('foo', 'foo')
if m is not None:
    str = m.group()

    print(str)
