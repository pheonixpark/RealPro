from pico2d import *
import random

class Coin:
    def __init__(self):
        self.x, self.y=random.randint(0,1600-1),90
        self.image = load_image('coin.png')

    def update(self):
        pass

    def get_bb(self):
        return self.x-5, self.y-5, self.x+5, self.y+5

    def draw(self):
        self.image.draw(self.x,self.y)
        draw_rectangle(*self.get_bb())
