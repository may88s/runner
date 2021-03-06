import pygame

BLACK=(0,0,0)
WHITE=(255,255,255)
BLUE=(0,0,255)
GREEN=(0,255,0)
RED=(255,0,0)
PURPLE=(255,0,255)
class Wall(pygame.sprite.Sprite)
  def __init__(self,x,y,width,height,colour)
  super().__init__()
