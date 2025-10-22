enemies = []

towers = [[None for i in range(3)] for j in range(3)]

def tick(mouse_mask):
    for i in range(len(towers)):
        for j in range(len(towers[i])):
            towers[i][j].tick(mouse_mask)
    
    for i in range(len(enemies)):
        enemies[i].tick()

def render():
    for i in range(len(towers)):
        for j in range(len(towers[i])):
            towers[i][j].render()
    
    for i in range(len(enemies)):
        enemies[i].render()