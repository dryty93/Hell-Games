from Player import*

gokuStance = makeSprite(os.path.join("images", "goku0.png"))
gokuStanceR = makeSprite(os.path.join("images", "goku0R.png"))
imageListG = [gokuStance,gokuStanceR ]

class Goku(Player):

    def __init__(self, image, xPos, yPos,  xSpeed, ySpeed):
        super().__init__(self, xPos, yPos, xSpeed, ySpeed)
        self.image = image
        self.xPos = xPos
        self.yPos = yPos
        self.xSpeed = xSpeed
        self.ySpeed = ySpeed


