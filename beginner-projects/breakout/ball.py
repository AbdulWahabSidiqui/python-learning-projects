from pygame import *

class Ball:
    def __init__(self,screen_width,screen_height):
        self.radius = 10
        self.color = (45, 212, 191)

        self.screen_width = screen_width
        self.screen_height = screen_height

        self.speed_x = 5
        self.speed_y = -5

        self.rect = Rect(screen_width//2 - self.radius,
                         screen_height//2 -self.radius,
                         self.radius * 2,
                         self.radius * 2)
    def draw(self,screen):
        draw.circle(screen,self.color,self.rect.center,self.radius)

    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

    def bounce(self,paddle):
        if self.rect.left <= 0:
            self.speed_x *= -1

        if self.rect.right >= self.screen_width:
            self.speed_x *= -1

        if self.rect.top <= 0:
            self.speed_y *= -1

        if self.rect.colliderect(paddle.rect):
            self.speed_y *= -1

    def is_out(self):
        return self.rect.bottom >= self.screen_height