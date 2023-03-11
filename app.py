from random import randint, randrange
import os

data = []
iterationsData = []


def makeFilePath(fileName):
    return os.path.join("fonts", fileName)


def randImg(numberOfThings, fileData=True):
    from PIL import Image, ImageDraw, ImageFont
    import random
    from read import english_words

    lstFont = [
        makeFilePath("BebasNeue.ttf"),
        makeFilePath("HackNF.ttf"),
        makeFilePath("Montserrat.ttf"),
        makeFilePath("RobotoMono.ttf"),
        makeFilePath("RobotoMono.ttf"),
        makeFilePath("GreyQo.ttf"),
        makeFilePath("Raleway.ttf"),
        makeFilePath("RubikBeastly.ttf"),
        makeFilePath("Art Brewery.ttf"),
        makeFilePath("orange juice 2.0.ttf"),
        makeFilePath("RemachineScript.ttf"),
        makeFilePath("Wedgie.ttf"),
        makeFilePath("DancingScript.ttf"),
        makeFilePath("LittleLordFontleroyNF.ttf"),
    ]

    fntLen = len(lstFont) - 1
    engLen = len(english_words) - 1

    width = random.randint(1000, 5000)
    height = random.randint(1000, 5000)

    randNum = random.randint(0, numberOfThings)

    bgR, bgG, bgB, bgA = (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
    )

    img = Image.new("RGBA", (width, height), (bgR, bgG, bgB, bgA))
    draw = ImageDraw.Draw(img)

    data.append(
        {
            "imageSize": {"width": width, "height": height},
            "color": {"red": bgR, "blue": bgB, "green": bgG},
            "iteration": randNum,
            "iterationData": [],
        }
    )

    for _ in range(randNum):
        fontSize = randint(20, 200)

        fnt = lstFont[randrange(0, fntLen)]
        tempFnt = fnt
        eng = english_words[randrange(0, engLen)]

        frameBufferX = width - ((fontSize * len(eng)) % width)
        frameBufferY = height - (fontSize * (fontSize % 3))

        posX = random.randint(0, frameBufferX)
        posY = random.randint(0, frameBufferY)

        r, g, b = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)

        fnt = ImageFont.truetype(fnt, fontSize)
        draw.text((posX, posY), eng, fill=(r, g, b), font=fnt)

        iterationsData.append(
            {
                "fontSize": fontSize,
                "font": tempFnt,
                "word": eng,
                "frameBuffer": {
                    "frameBufferX": frameBufferX,
                    "frameBufferY": frameBufferY,
                },
                "position": {"PositionX": posX, "PositionY": posY},
                "color": {"red": r, "blue": b, "green": g},
            }
        )

    data[0]["iterationData"] = iterationsData
    fileName = english_words[randrange(0, engLen)]

    if not os.path.exists("images"):
        os.makedirs("images")

    path = os.path.join("images", fileName + ".png")
    img.save(path)

    img.show()
    if fileData:
        return data
    return 0
