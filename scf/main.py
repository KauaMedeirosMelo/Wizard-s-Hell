from pplay import window, sprite, mouse
from pygame import display, NOFRAME
import os
import entity, tower, background, enemy, toolbar


base_dir = os.path.dirname(os.path.abspath(__file__))
res_access = os.path.join(base_dir, "..", "res") + "\\"

screen = window.Window(1000, 700)
display.set_mode((screen.width, screen.height), NOFRAME)
mouse.Mouse.hide(mouse)

key = screen.get_keyboard()

background.start()
tower.start_towers(screen)
enemy.generate_enemies(screen)
toolbar.init_sprites(screen)
toolbar.visible = True

mouse_mask = sprite.Sprite(res_access+"mouse.png")

def tick():
    mouse_mask.x, mouse_mask.y = mouse.Mouse.get_position(mouse)
    entity.tick(mouse_mask)
    if(key.key_pressed("esc")):
        screen.close()

def render():
    background.render()
    entity.render()
    toolbar.render()
    mouse_mask.draw()
    screen.update()

while(True):

    tick()
    render()
    
    pass