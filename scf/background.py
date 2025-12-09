from pplay import sprite
import resacc

image = None

def init(res_access):
    global image
    image = sprite.Sprite(resacc.resource_path("res\\models\\background1.png"))
    image.x = 150

def render():
    image.draw()