from pico2d import *
import random

class Coin:
    def __init__(self, no='NONO',x=0, y=0):
        self.no=no
        self.x, self.y=x,y
        self.image = load_image('coin.png')

    def update(self):
        pass

    def get_bb(self):
        return self.x-5, self.y-5, self.x+5, self.y+5

    def draw(self):
        self.image.draw(self.x,self.y)
        draw_rectangle(*self.get_bb())
