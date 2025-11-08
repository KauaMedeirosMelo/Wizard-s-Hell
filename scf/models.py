from pplay import sprite
from entity import enemies, towers
from toolbar import init_sprites as init_toolbar
from background import start as init_background
from resacc import res_access


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
