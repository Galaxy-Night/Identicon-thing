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
size = random.choice((2, 4))
color = chooseColor()
multiplier = 320/(size * 2)
for i in range(0, size):
    for j in range(0, size * 2):
        val = random.randrange(0, 2)
        if val is not 0:
            square = ImageDraw.Draw(output)
            square.rectangle((multiplier * i, multiplier * j, multiplier * (i + 1), multiplier * (j + 1)), color)
            output.save('test.png')
            square.rectangle((multiplier * (size * 2 - i - 1), multiplier * j, multiplier * (size * 2 - i),
                              multiplier * (j + 1)), color)
            output.save('test.png')

