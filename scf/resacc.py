import os
from pplay import sprite
from entity import enemies, towers
from toolbar import init_sprites as init_toolbar
from background import start as init_background

base_dir = os.path.dirname(os.path.abspath(__file__))
res_access = []
res_access.append(os.path.join(base_dir, "..", "res") + "\\" + "models\\")


def change_access(name):
    res_access[0]= os.path.join(base_dir, "..", "res\\") + name + "\\"
    
    return

def change_models(screen):

    for i in range(len(towers)):
        for j in range(len(towers[i])):
                towers[i][j].sprite = sprite.Sprite(res_access[0]+"torre1.png")
                towers[i][j].sprite.x = towers[i][j].x
                towers[i][j].sprite.y = towers[i][j].y
    
    for i in enemies:
        i.sprite = sprite.Sprite(res_access[0]+"enemy1.png")
        i.sprite.x = i.x
        i.sprite.y = i.y

    init_toolbar(screen, res_access[0])
    init_background(res_access[0])

    return
