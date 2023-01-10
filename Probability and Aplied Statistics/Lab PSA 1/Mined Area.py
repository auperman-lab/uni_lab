from PIL import Image
import random
img = Image.open('/Probability and Aplied Statistics/Lab PSA 1/laboratory_work_math_files/danger_zone.png')

data = img.load()
n = int(input())
mine = 0
height = img.size[0]
width = img.size[1]

for i in range(n):
    x = random.randint(0, height-1)
    y = random.randint(0, width-1)
    if data[x, y] != data[3, 3]:
        mine += 1

print(42*mine/n)
