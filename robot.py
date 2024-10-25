import pygame

class Robot:
    def __init__(self, rect):
        self.rect = rect
        self.x, self.y = (400, 400)
        self.acceleration = 0.5
    def draw(self, win, img):
        win.blit(img, self.rect)
        