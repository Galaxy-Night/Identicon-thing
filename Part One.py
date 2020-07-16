import hashlib
import random

string = input("Value: ")
bytes = string.encode('utf-8')
hash = hashlib.sha1()
hash.update(bytes)
seed = int.from_bytes(hash.digest(), 'little')
random.seed(seed)
size = random.choice((1, 2, 4))
for i in range(0, size):
    row = ''
    for j in range(0, size):
        val = random.randrange(0, 2)
        if val is not 0:
            row += '\u2588' * int(4/size) * 2
        else:
            row += ' ' * int(4/size) * 2
    row += row[::-1]
    for k in range(0, int(8/size)):
        print(row.center(size))
