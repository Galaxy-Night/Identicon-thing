#I really like plaid
from PIL import Image, ImageDraw, ImageColor
import hashlib
import random

output = Image.new('RGB', (320, 320), color='white')


def chooseColor():
    red = ImageColor.getrgb('#ff553f80')
    green = ImageColor.getrgb('#a8c02380')
    blue = ImageColor.getrgb('#5394ec80')
    cyan = ImageColor.getrgb('#29999980')
    return [red, green, blue, cyan]


string = input("Value: ")
bytes = string.encode('utf-8')
hash = hashlib.sha1()
hash.update(bytes)
seed = int.from_bytes(hash.digest(), 'little')
random.seed(seed)
size = random.choice((2, 4))
colors = chooseColor()
multiplier = 320/(size)
numHorizontalStripes = random.randrange(1, 5)
for i in range(0, numHorizontalStripes):
    leftside = random.randint(0, multiplier - 1)
    rightside = random.randrange(leftside, multiplier)
    color = random.choice(colors)
    stripe = ImageDraw.Draw(output)
    for j in range(0, size):
        translation = j * multiplier
        stripe.rectangle((leftside + translation, 0, rightside + translation, 320), color)
        output.save(f'{string}.png')
numVerticalStripes = random.randrange(1, 5)
for i in range(0, numVerticalStripes):
    top = random.randint(0, multiplier - 1)
    bottom = random.randrange(top, multiplier)
    color = random.choice(colors)
    stripe = ImageDraw.Draw(output)
    for j in range(0, size):
        translation = j * multiplier
        stripe.rectangle((0, top + translation, 320, bottom + translation), color)
        output.save(f'{string}.png')

'''for i in range(0, size):
    for j in range(0, size * 2):
        val = random.randrange(0, 2)
        if val is not 0:
            square = ImageDraw.Draw(output)
            square.rectangle((multiplier * i, multiplier * j, multiplier * (i + 1), multiplier * (j + 1)), color)
            output.save(f'{string}.png')
            square.rectangle((multiplier * (size * 2 - i - 1), multiplier * j, multiplier * (size * 2 - i),
                              multiplier * (j + 1)), color)
            output.save(f'{string}.png')'''

