from pico2d import *

class Brick:
    def __init__(self, no,x=0,y=0):
        self.image = load_image('brick.png')
    def update(self):
        self.x=self.x
    def get_bb(self):
        return self.x-5, self.y-5, self.x+5, self.y+5

    def draw(self):
        self.image.draw(self.x,self.y)
        draw_rectangle(*self.get_bb())

