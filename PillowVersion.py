from PIL import Image, ImageDraw, ImageColor
import hashlib
import random

output = Image.new('RGB', (320, 320), color='white')


def chooseColor():
    red = ImageColor.getrgb('#ff553f')
    green = ImageColor.getrgb('#a8c023')
    yellow = ImageColor.getrgb('#d6bf55')
    blue = ImageColor.getrgb('#5394ec')
    magenta = ImageColor.getrgb('#ae8abe')
    cyan = ImageColor.getrgb('#299999')
    default = ImageColor.getrgb('#2b2b2b')
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
            output.save(f'{string}.png')
            square.rectangle((multiplier * (size * 2 - i - 1), multiplier * j, multiplier * (size * 2 - i),
                              multiplier * (j + 1)), color)
            output.save(f'{string}.png')
output.show()
