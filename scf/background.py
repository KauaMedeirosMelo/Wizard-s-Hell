from pplay import sprite
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
res_access = os.path.join(base_dir, "..", "res") + "\\"
image = None

def start():
    global image
    image = sprite.Sprite(res_access+"background1.png")

def render():
    image.draw()