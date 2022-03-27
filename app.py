from random import randint, randrange
import os


def randImg(numberOfThings):
    from PIL import Image, ImageDraw, ImageFont
    import random
    from read import english_words

    bebas = os.path.join("fonts", "BebasNeue.ttf")
    hack = os.path.join("fonts", "HackNF.ttf")
    mont = os.path.join("fonts", "Montserrat.ttf")
    roboto = os.path.join("fonts", "RobotoMono.ttf")
    slab = os.path.join("fonts", "RobotoSlab.ttf")
    grey = os.path.join("fonts", "GreyQo.ttf")
    raleway = os.path.join("fonts", "Raleway.ttf")
    rubik = os.path.join("fonts", "RubikBeastly.ttf")
    art = os.path.join("fonts", "Art Brewery.ttf")
    orange = os.path.join("fonts", "orange juice 2.0.ttf")
    remachine = os.path.join("fonts", "RemachineScript.ttf")
    wedgie = os.path.join("fonts", "Wedgie.ttf")
    dancing = os.path.join("fonts", "DancingScript.ttf")
    little = os.path.join("fonts", "LittleLordFontleroyNF.ttf")

    lstFont = [
        bebas,
        hack,
        mont,
        roboto,
        slab,
        grey,
        raleway,
        rubik,
        art,
        orange,
        remachine,
        wedgie,
        dancing,
        little,
    ]

    fntLen = len(lstFont) - 1
    engLen = len(english_words) - 1

    width = random.randint(1000, 5000)
    height = random.randint(1000, 5000)

    randNum = random.randint(0, numberOfThings)

    r = random.randint(0, 255)
    b = random.randint(0, 255)
    g = random.randint(0, 255)
    a = random.randint(0, 255)

    img = Image.new("RGBA", (width, height), (r, b, g, a))
    draw = ImageDraw.Draw(img)

    for _ in range(randNum):
        fontSize1 = randint(20, 200)

        posX1 = random.randint(0, width)
        posY1 = random.randint(0, height)

        fnt = lstFont[randrange(0, fntLen)]
        eng = english_words[randrange(0, engLen)]

        r1 = random.randint(0, 255)
        b1 = random.randint(0, 255)
        g1 = random.randint(0, 255)
        fnt1 = ImageFont.truetype(fnt, fontSize1)
        draw.text((posX1, posY1), eng, fill=(r1, g1, b1), font=fnt1)

    fileName = english_words[randrange(0, engLen)]
    img.save(fileName + ".png")
    img.show()


randImg(50)
