from PIL import Image, ImageDraw
import hashlib
import random

output = Image.new('RGB', (320, 320), color='white')

#color definitions
end = '\033[0m'


def chooseColor():
    red = 'red'
    green = 'green'
    yellow = 'yellow'
    blue = 'blue'
    magenta = 'magenta'
    cyan = 'cyan'
    default = 'black'
    return random.choice((red, green, yellow, blue, magenta, cyan, default))


string = input("Value: ")
bytes = string.encode('utf-8')
hash = hashlib.sha1()
hash.update(bytes)
seed = int.from_bytes(hash.digest(), 'little')
random.seed(seed)
size = 8
color = chooseColor()
for i in range(0, size):
    for j in range(0, size * 2):
        val = random.randrange(0, 2)
        if val is not 0:
            square = ImageDraw.Draw(output)
            square.rectangle((20 * i, 20 * j, 20 * (i + 1), 20 * (j + 1)), color)
            output.save('test.png')
            square.rectangle((20 * (size * 2 - i - 1), 20 * j, 20 * (size * 2 - i),
                              20 * (j + 1)), color)
            output.save('test.png')

