#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
from constants import *

class Button(object):
    def __init__(self,x,y,width,height,text,color):
        self.rect = pygame.Rect(x,y,width,height)
        self.font = pygame.font.Font(None,40)
        self.text = self.font.render(text,True,WHITE)
        self.bg_color = color

    def draw(self,screen):
        """ This method will draw the button to the screen """
        # Fisrt fill the rect with the bg_color
        pygame.draw.rect(screen,self.bg_color,self.rect)
        # Get the width and height of the text surface
        width = self.text.get_width()
        height = self.text.get_height()
        # Calculate the posX and posY
        posX = self.rect.centerx - (width / 2)
        posY = self.rect.centery - (height / 2)
        # Draw the image into the screen
        screen.blit(self.text,(posX,posY))

    def isPressed(self):
        """ Return true if the mouse is on the button """
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            return True
        else:
            return False
            
    def change_bg_color(self,color):
        self.bg_color = color