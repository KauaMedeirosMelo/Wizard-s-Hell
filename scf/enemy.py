from pplay import sprite
import os, random
import entity

base_dir = os.path.dirname(os.path.abspath(__file__))
res_access = os.path.join(base_dir, "..","res") + "\\"

def generate_enemies(screen):
    N = random.randint(0, 20)
    N = 20
    for i in range(N):
        my_sprite = sprite.Sprite(res_access+"enemy1.png")
        UD = random.randint(0, 1)
        LF = random.randint(0, 1)

        if(UD):
            posX = random.randint(int(screen.width*(2/3)), screen.width)
        else:
            posX = random.randint(0, int(screen.width*(1/3)))

        if(LF):
            posY = random.randint(int(screen.height*(2/3)), screen.height)
        else:
            posY = random.randint(0, int(screen.height*(1/3)))

        entity.enemies.append(Enemy(posX, posY, my_sprite))
        

    return


class Enemy():

    stats = []

    def __init__(self, x, y, sprite):
        sprite.x = x
        sprite.y = y

        self.x = x
        self.y = y
        self.sprite = sprite
        print("posX: {}, posY: {}".format(self.sprite.x, self.sprite.y))

    def collision(self):
        pass

    def tick(self):
        pass

    def render(self):
        self.sprite.draw()
        #print("posX: {}, posY: {}".format(self.sprite.x, self.sprite.y))
        pass