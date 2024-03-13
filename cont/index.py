# count é um iterador sem fim (itertools)

import itertools

c1 = itertools.count(10, 8)
r1 = range(10, 100, 8)

print('c1', hasattr(c1, '__iter__'))

print('count')
for i in c1:
    if i > 100:
        break
    print(i)

print()
print('renge')

for i in r1:
    print(i)