from pplay import window, sprite, mouse
import os
import entity, tower

screen = window.Window(1200, 800)

base_dir = os.path.dirname(os.path.abspath(__file__))
res_access = os.path.join(base_dir, "..", "res") + "\\"

mouse_mask = sprite.Sprite(res_access+"mouse.png")

def start_game():
    for i in range(3):
        for j in range(3):
            entity.towers[i][j] = tower.Tower(200+60*i, 160+60*j, sprite.Sprite(res_access+"torre1.png"))
    pass

start_game()

while(True):


    #TICK
    mouse_mask.x, mouse_mask.y = mouse.Mouse.get_position(mouse)


    for i in range(len(entity.towers)):
        for j in range(len(entity.towers[i])):
            entity.towers[i][j].tick(mouse_mask)




    #RENDER
    screen.set_background_color((0,0,0))

    for i in range(len(entity.towers)):
        for j in range(len(entity.towers[i])):
            entity.towers[i][j].render()
            #print("i: {}, j: {}".format(i, j))

    screen.update()
    pass