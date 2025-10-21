from pplay import sprite
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
res_access = os.path.join(base_dir, "..","res") + "\\"

#sprite1 = sprite.Sprite(res_access+"torre1.png")

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
        #print("aebaa")
        pass