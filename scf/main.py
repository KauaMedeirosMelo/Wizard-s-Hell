from pplay import window, sprite, mouse
from pygame import display, NOFRAME
from resacc import res_access, change_access
import entity, tower, background, enemy, toolbar, models, card

event = False

screen = window.Window(1000, 700)
display.set_mode((screen.width, screen.height), NOFRAME)
mouse.Mouse.hide(mouse)

key = screen.get_keyboard()

background.start(res_access[0])
tower.start_towers(screen, res_access[0])
enemy.generate_enemies(screen, res_access[0], 5)
toolbar.init_sprites(screen, res_access[0])

timer = 0
num = 5


def tick():
    global timer, num, myX, myY

    dt = screen.delta_time()
    timer += dt
    toolbar.game_timer[0] += dt

    if(timer >= 15):
        enemy.generate_enemies(screen, res_access[0],num)
        num = num+2
        timer = 0
    
    entity.tick(toolbar.mouse_mask, dt)
    card.tick(screen, res_access[0], toolbar.mouse_mask, dt)
    if(key.key_pressed("esc")):
        screen.close()

    if(key.key_pressed("e")):
        change_access("eventmodels")

    if(key.key_pressed("p")):
        change_access("models")

    if(key.key_pressed("space")):
        models.change_models(screen)

    toolbar.tick(res_access[0], screen)
    if(toolbar.exp[0] <= 0):
        screen.close()

    if(toolbar.click and toolbar.mode == 3):
        for i in range(len(entity.towers)):
            for j in range(len(entity.towers[i])):
                if(entity.towers[i][j].collision(toolbar.mouse_mask)):
                    toolbar.visible = True
                    toolbar.towerI = i
                    toolbar.towerJ = j
                    toolbar.show_stats[0] = entity.towers[i][j].size
                    toolbar.show_stats[1] = entity.towers[i][j].speed
                    toolbar.show_stats[2] = entity.towers[i][j].cooldown
                    entity.towers[i][j].show_cards = True

    if(card.set_stat and toolbar.click):
        for i in range(len(entity.towers)):
            for j in range(len(entity.towers[i])):
                if(entity.towers[i][j].collision(toolbar.mouse_mask)):
                    if(not (card.stat in entity.towers[i][j].stats)):
                        entity.towers[i][j].stats.append(card.stat)
                        entity.towers[i][j].execute_stats(res_access[0])
                        card.set_stat = False
                        card.stat = None
                        card.show_select = False
                    pass


def render(screen):
    screen.set_background_color((0,0,0))
    background.render()
    entity.render(screen)
    toolbar.render(screen)
    card.render(screen)
    toolbar.mouse_mask.draw()
    screen.update()

while(True):

    tick()
    render(screen)
    
    pass