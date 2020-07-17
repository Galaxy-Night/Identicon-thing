import hashlib
import random

#color definitions
end = '\033[0m'


def chooseColor():
    red = '\033[31m'
    green = '\033[32m'
    yellow = '\033[33m'
    blue = '\033[34m'
    magenta = '\033[35m'
    cyan = '\033[36m'
    default = '\033[0m'
    return random.choice((red, green, yellow, blue, magenta, cyan, default))


string = input("Value: ")
bytes = string.encode('utf-8')
hash = hashlib.sha1()
hash.update(bytes)
seed = int.from_bytes(hash.digest(), 'little')
random.seed(seed)
size = random.choice((2, 4, 8))
color = chooseColor()
for i in range(0, size):
    row = ''
    for j in range(0, size):
        val = random.randrange(0, 2)
        if val is not 0:
            row += '\u2588' * int(8/size) * 2
        else:
            row += ' ' * int(8/size) * 2
    row += row[::-1]
    for k in range(0, int(16/size)):
        print(f"{color}{row}{end}".center(size))
