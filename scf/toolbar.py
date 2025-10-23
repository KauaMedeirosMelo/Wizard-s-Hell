from pplay import sprite

tower_stats = None
visible = False

toolbar = None

def init_sprites(screen, res_access):
    global tower_stats, toolbar

    tower_stats = sprite.Sprite(res_access+"tower_stats.png")
    tower_stats.x = screen.width - tower_stats.width - 20
    tower_stats.y = 20

    toolbar = sprite.Sprite(res_access+"toolbar.png")
    toolbar.x = 20
    toolbar.y = 20

# def position_stats(posX, posY):
#     global tower_stats
#     tower_stats.x = posX
#     tower_stats.y = posY

def render():
    global visible

    toolbar.draw()
    
    if(visible):
        tower_stats.draw()