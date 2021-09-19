from random import randint, randrange, random

def randImg():
    from PIL import Image, ImageDraw, ImageFont
    import random
    
    bebas = "fonts\BebasNeue.ttf"
    hack = "fonts\HackNF.ttf"
    mont = "fonts\Montserrat.ttf"
    roboto = "fonts\RobotoMono.ttf"
    slab = "fonts\RobotoSlab.ttf"
    grey = "fonts\GreyQo.ttf"
    raleway = "fonts\Raleway.ttf"
    rubik = "fonts\RubikBeastly.ttf"
    
    lstFont = [bebas, hack, mont, roboto, slab, grey, raleway, rubik]
    lstNum = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    lstAlpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    lstSym = ["`", "~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "{", "]", "}"]

    numLen = len(lstNum) -1
    alphaLen = len(lstAlpha) -1
    symLen = len(lstSym) -1
    fntLen = len(lstFont) -1
    
    width = random.randint(200,800)
    height = random.randint(200,800)
    
    randNum = random.randint(0, 100)

    r = random.randint(0, 255)
    b = random.randint(0, 255)
    g = random.randint(0, 255)
    a = random.randint(0, 255)

    img = Image.new("RGBA", (width, height), (r, b, g, a))
    draw = ImageDraw.Draw(img)
    
    for _ in range(randNum):
        fontSize1 = randint(1, 100)
        fontSize2 = randint(1, 100)
        fontSize3 = randint(1, 100)
        
        posX1 = random.randint(0, width)
        posY1 = random.randint(0, height)
        
        posX2 = random.randint(0, width)
        posY2 = random.randint(0, height)
        
        posX3 = random.randint(0, width)
        posY3 = random.randint(0, height)
        
        num = lstNum[randrange(0, numLen)]
        alpha = lstAlpha[randrange(0, alphaLen)]
        sym = lstSym[randrange(0, symLen)]
        fnt = lstFont[randrange(0, fntLen)]
        
        r1 = random.randint(0, 255)
        b1 = random.randint(0, 255)
        g1 = random.randint(0, 255)
        fnt1 = ImageFont.truetype(fnt, fontSize1)
        draw.text((posX1,posY1), str(num), fill = (r1, g1, b1), font = fnt1)
        
        r2 = random.randint(0, 255)
        b2= random.randint(0, 255)
        g2 = random.randint(0, 255)
        fnt2 = ImageFont.truetype(fnt, fontSize2)
        draw.text((posX2,posY2), str(alpha), fill=(r2, g2, b2), font = fnt2)
        
        r3 = random.randint(0, 255)
        b3 = random.randint(0, 255)
        g3 = random.randint(0, 255)
        fnt3 = ImageFont.truetype(fnt, fontSize3)
        draw.text((posX3,posY3), str(sym), fill= (r3, g3, b3), font = fnt3)

    img.show()
    img.save("yolo.png")
    
randImg()