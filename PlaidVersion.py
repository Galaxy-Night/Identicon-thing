#I really like plaid
from PIL import Image, ImageDraw, ImageColor
import hashlib
import random


def choosecolor(hue):
    return ImageColor.getrgb(f'hsl({hue}, 50%, {random.randrange(0, 100)}%)')


def choosecolors(hue):
    returned = []
    for i in range(0, 5):
        returned.append(choosecolor(hue))
    return returned


hue = random.randrange(0, 360)
output = Image.new('RGB', (320, 320), color=choosecolor(hue))
string = input("Value: ")
bytes = string.encode('utf-8')
hash = hashlib.sha1()
hash.update(bytes)
seed = int.from_bytes(hash.digest(), 'little')
random.seed(seed)
size = random.choice((2, 4))
colors = choosecolors(hue)
multiplier = 320/(size)
numHorizontalStripes = random.randrange(1, 5)
for i in range(0, numHorizontalStripes):
    leftside = random.randint(0, multiplier - 1)
    rightside = random.randrange(leftside, multiplier)
    color = random.choice(colors)
    pasted = Image.new('RGBA', (320, 320), color='#ffffff00')
    stripe = ImageDraw.Draw(pasted)
    for j in range(0, size):
        translation = j * multiplier
        stripe.rectangle((leftside + translation, 0, rightside + translation, 320), color)
    pasted.putalpha(128)
    output.paste(pasted, (0, 0), pasted)
    output.save(f'{string}.png')
numVerticalStripes = random.randrange(1, 5)
for i in range(0, numVerticalStripes):
    top = random.randint(0, multiplier - 1)
    bottom = random.randrange(top, multiplier)
    color = random.choice(colors)
    pasted = Image.new('RGBA', (320, 320), color='#ffffff00')
    stripe = ImageDraw.Draw(pasted)
    for j in range(0, size):
        translation = j * multiplier
        stripe.rectangle((0, top + translation, 320, bottom + translation), color)
    pasted.putalpha(128)
    output.paste(pasted, (0, 0), pasted)
    output.save(f'{string}.png')
output.show()

