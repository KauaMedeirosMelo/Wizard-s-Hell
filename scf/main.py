from pplay import window, sprite, mouse
import os
import entity, tower, background, enemy, toolbar

screen = window.Window(1200, 800)
mouse.Mouse.hide(mouse)

base_dir = os.path.dirname(os.path.abspath(__file__))
res_access = os.path.join(base_dir, "..", "res") + "\\"

mouse_mask = sprite.Sprite(res_access+"mouse.png")

background.start()
tower.start_towers(screen)
enemy.generate_enemies(screen)
toolbar.init_sprites(screen)

toolbar.visible = True

def tick():
    mouse_mask.x, mouse_mask.y = mouse.Mouse.get_position(mouse)
    entity.tick(mouse_mask)

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