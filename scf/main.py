from pplay import window, sprite, mouse
from pygame import display, NOFRAME
from resacc import res_access, change_access, change_models
import entity, tower, background, enemy, toolbar

event = False

screen = window.Window(1000, 700)
display.set_mode((screen.width, screen.height), NOFRAME)
mouse.Mouse.hide(mouse)

key = screen.get_keyboard()

background.start(res_access[0])
tower.start_towers(screen, res_access[0])
enemy.generate_enemies(screen, res_access[0])
toolbar.init_sprites(screen, res_access[0])
toolbar.visible = True

mouse_mask = sprite.Sprite(res_access[0]+"mouse.png")

def tick():
    mouse_mask.x, mouse_mask.y = mouse.Mouse.get_position(mouse)
    entity.tick(mouse_mask)
    if(key.key_pressed("esc")):
        screen.close()

    if(key.key_pressed("e")):
        change_access("eventmodels")

    if(key.key_pressed("p")):
        change_access("models")

    if(key.key_pressed("space")):
        change_models(screen)


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