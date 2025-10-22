from pplay import sprite
import os
import entity

base_dir = os.path.dirname(os.path.abspath(__file__))
res_access = os.path.join(base_dir, "..","res") + "\\"

def start_towers(screen):
    for i in range(3):
        for j in range(3):
            my_sprite = sprite.Sprite(res_access+"torre1.png")
            posX = (screen.width - my_sprite.width*1.5)/2 + my_sprite.width*(i-1)*1.5
            posY = (screen.height - my_sprite.height)/2 + my_sprite.height*(j-1)*1.5
            entity.towers[i][j] = Tower(posX , posY, my_sprite)
    return

class Tower():

    stats = []

    def __init__(self, x, y, sprite):
        sprite.x = x
        sprite.y = y

        self.x = x
        self.y = y
        self.sprite = sprite


    def collision(self, obj):
        if(self.sprite.collided(obj)):
            return True
        return False

    def tick(self, mouse):
        if(self.collision(mouse)):
            pass

        pass

    def render(self):
        self.sprite.draw()
        pass