from pygame import *

class Paddle:
    def __init__(self,screen_width,screen_height):
        self.width = 120
        self.height = 20
        self.speed = 8
        self.color = (248, 250, 252)
        self.margin = 20

        self.screen_width = screen_width
        self.rect = Rect(screen_width//2 - self.width//2,screen_height-40,self.width,self.height)


    def draw(self,screen):
        draw.rect(screen,self.color,self.rect)
    def move_left(self):
        if self.rect.left > self.margin:
            self.rect.x -= self.speed
    def move_right(self):
        if self.rect.right < self.screen_width - self.margin:
            self.rect.x += self.speed