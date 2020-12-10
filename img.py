import PIL.ImageDraw as ImageDraw, PIL.Image as Image, PIL.ImageShow as ImageShow

mx, my = -1, -1
with open('img.csv')as f:
    im = Image.new("RGB", (300, 41))
    for l in f.readlines():
        x, y, r, g, b = map(int, l.split(','))
        mx = max(mx, x)
        my = max(my, y)
        im.putpixel((x,y), (r, g, b))
    im.save("g.jpg")

print(mx, my)
