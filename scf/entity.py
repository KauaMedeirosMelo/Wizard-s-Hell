
enemies = None

towers = None

def init():
    global enemies, towers

    enemies = []

    towers = [[None for i in range(3)] for j in range(3)]



def tick(mouse_mask, dt):
    for i in range(len(towers)):
        for j in range(len(towers[i])):
            towers[i][j].tick(mouse_mask, dt)
    
    i = 0
    while(i < len(enemies)):
        enemies[i].tick(dt)
        if(enemies[i].die):
            enemies.pop(i)
            i-=1
        i+=1

    # for i in range(len(enemies)):
    #     enemies[i].tick(dt)

def render(screen):
    for i in range(len(towers)):
        for j in range(len(towers[i])):
            towers[i][j].render(screen)
    
    for i in range(len(enemies)):
        enemies[i].render()