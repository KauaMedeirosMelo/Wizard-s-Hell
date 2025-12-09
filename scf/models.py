from pplay import sprite
from entity import enemies, towers
from toolbar import init_sprites as init_toolbar
from background import init as init_background
import resacc


def change_models(screen):
    for i in range(len(towers)):
        for j in range(len(towers[i])):
                towers[i][j].sprite = sprite.Sprite(resacc.resource_path("res\\models\\torre1.png"))
                towers[i][j].sprite.x = towers[i][j].x
                towers[i][j].sprite.y = towers[i][j].y
    
    for i in enemies:
        i.sprite = sprite.Sprite(resacc.resource_path("res\\models\\enemy1.png"))
        i.sprite.x = i.x
        i.sprite.y = i.y

    init_toolbar(screen, resacc.res_access[0])
    init_background(resacc.res_access[0])

    return
