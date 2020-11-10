from itertools import count
from itertools import cycle
# iterator 1
start = 3
for el in count(start):
    if el > 10:
        break
    else:
        print(f'{el} ', end='')
print()
# iterator 2
counter = 0
c_list = ['X', 'Y', 'Z']
for el in cycle(c_list):
    if counter > 10:
        break
    print(f'{el} ', end='')
    counter += 1
