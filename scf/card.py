from pplay import sprite
import toolbar, entity
import random

cards = []

types = ["size", "speed"]

def render(screen):
    for i in cards:
        i.render(screen)

def tick(screen, res_access, mouse_mask, dt):
    if(toolbar.exp[0] >= 200):
        toolbar.exp[0] = 100
        toolbar.exp_change += 0.2
        new_cards(screen, res_access)
    for i in cards:
        i.tick(mouse_mask, dt)

def new_cards(screen, res_access):
    for i in range(3):
        t = random.randint(0, len(types)-1)
        my_sprite = sprite.Sprite(res_access+types[t]+"_card.png")
        cards.append(Card(my_sprite, screen.width - my_sprite.width*1.25, 20 + my_sprite.height*i*1.2, types[t]))


    return

def release_cards():
    while(len(cards) != 0):
        cards.pop(0)

class Card():
    
    def __init__(self, sprite, x, y, type):
        self.x = x
        self.y = y
        sprite.x = x
        sprite.y = y
        self.sprite = sprite

        self.type = type

    def collision(self, obj):
        if(self.sprite.collided(obj)):
            return True

    def tick(self, mouse_mask, dt):
        if(toolbar.click):
            if(self.collision(mouse_mask)):
                for i in range(len(entity.towers)):
                    for j in range(len(entity.towers[i])):
                        setattr(entity.towers[i][j], self.type, getattr(entity.towers[i][j], self.type) *1.2)
                release_cards()

        pass

    def render(self, screen):
        self.sprite.draw()