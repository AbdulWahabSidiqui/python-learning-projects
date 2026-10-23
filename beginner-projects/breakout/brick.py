import pygame

class Brick:
    def __init__(self, x,y,color):
        self.width = 100
        self.height = 30

        self.color = color

        self.rect = pygame.Rect(x,y,self.width,self.height)

    def draw(self,screen):
        pygame.draw.rect(screen,self.color,self.rect,border_radius=6)