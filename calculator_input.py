#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
from constants import *
from button import Button

class Calculator_input(object):
    def __init__(self):
        self.font = pygame.font.Font("computer-font.ttf",45)
        self.text = self.font.render("0",True,BLACK)
        # self.value will hold the current number on the screen
        self.value = "0"
        # Declare all the numbers buttons
        self.btn0 = Button(20,330,60,40,"0",GRAY)
        self.btn1 = Button(20,270,60,40,"1",GRAY)
        self.btn2 = Button(95,270,60,40,"2",GRAY)
        self.btn3 = Button(170,270,60,40,"3",GRAY) 
        self.btn4 = Button(20,210,60,40,"4",GRAY)
        self.btn5 = Button(95,210,60,40,"5",GRAY)
        self.btn6 = Button(170,210,60,40,"6",GRAY)
        self.btn7 = Button(20,150,60,40,"7",GRAY)
        self.btn8 = Button(95,150,60,40,"8",GRAY)
        self.btn9 = Button(170,150,60,40,"9",GRAY)
        self.btn_point = Button(95,330,60,40,".",GRAY)
        # This boolean will be true when we want to enter a new number 
        self.new_entry = True
        # This boolean will be true when we already pressed a key
        self.key_pressed = False
    
    def event_handler(self,event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.btn0.isPressed():
                self.append_value("0")
                self.btn0.change_bg_color(LIGHT_GRAY)
            elif self.btn1.isPressed():
                self.append_value("1")
                self.btn1.change_bg_color(LIGHT_GRAY)
            elif self.btn2.isPressed():
                self.append_value("2")
                self.btn2.change_bg_color(LIGHT_GRAY)
            elif self.btn3.isPressed():
                self.append_value("3")
                self.btn3.change_bg_color(LIGHT_GRAY)
            elif self.btn4.isPressed():
                self.append_value("4")
                self.btn4.change_bg_color(LIGHT_GRAY)
            elif self.btn5.isPressed():
                self.append_value("5")
                self.btn5.change_bg_color(LIGHT_GRAY)
            elif self.btn6.isPressed():
                self.append_value("6")
                self.btn6.change_bg_color(LIGHT_GRAY)
            elif self.btn7.isPressed():
                self.append_value("7")
                self.btn7.change_bg_color(LIGHT_GRAY)
            elif self.btn8.isPressed():
                self.append_value("8")
                self.btn8.change_bg_color(LIGHT_GRAY)
            elif self.btn9.isPressed():
                self.append_value("9")
                self.btn9.change_bg_color(LIGHT_GRAY)
            elif self.btn_point.isPressed():
                self.append_point()
                self.btn_point.change_bg_color(LIGHT_GRAY)
                
        elif event.type == pygame.MOUSEBUTTONUP:
            self.btn0.change_bg_color(GRAY)
            self.btn1.change_bg_color(GRAY)
            self.btn2.change_bg_color(GRAY)
            self.btn3.change_bg_color(GRAY)
            self.btn4.change_bg_color(GRAY)
            self.btn5.change_bg_color(GRAY)
            self.btn6.change_bg_color(GRAY)
            self.btn7.change_bg_color(GRAY)
            self.btn8.change_bg_color(GRAY)
            self.btn9.change_bg_color(GRAY)
            self.btn_point.change_bg_color(GRAY)
                
        elif event.type == pygame.KEYDOWN:
            # Check for numbers on the keyboard
            if event.key == pygame.K_0 or event.key == pygame.K_KP0:
                self.append_value("0")
                self.btn0.change_bg_color(LIGHT_GRAY)
            elif event.key == pygame.K_1 or event.key == pygame.K_KP1:
                self.append_value("1")
                self.btn1.change_bg_color(LIGHT_GRAY)
            elif event.key == pygame.K_2 or event.key == pygame.K_KP2:
                self.append_value("2")
                self.btn2.change_bg_color(LIGHT_GRAY)
            elif event.key == pygame.K_3 or event.key == pygame.K_KP3:
                self.append_value("3")
                self.btn3.change_bg_color(LIGHT_GRAY)
            elif event.key == pygame.K_4 or event.key == pygame.K_KP4:
                self.append_value("4")
                self.btn4.change_bg_color(LIGHT_GRAY)
            elif event.key == pygame.K_5 or event.key == pygame.K_KP5:
                self.append_value("5")
                self.btn5.change_bg_color(LIGHT_GRAY)
            elif event.key == pygame.K_6 or event.key == pygame.K_KP6:
                self.append_value("6")
                self.btn6.change_bg_color(LIGHT_GRAY)
            elif event.key == pygame.K_7 or event.key == pygame.K_KP7:
                self.append_value("7")
                self.btn7.change_bg_color(LIGHT_GRAY)
            elif event.key == pygame.K_8 or event.key == pygame.K_KP8:
                self.append_value("8")
                self.btn8.change_bg_color(LIGHT_GRAY)
            elif event.key == pygame.K_9 or event.key == pygame.K_KP9:
                self.append_value("9")
                self.btn9.change_bg_color(LIGHT_GRAY)
            elif event.key == pygame.K_PERIOD or event.key == pygame.K_KP_PERIOD:
                self.append_point()
                self.btn_point.change_bg_color(LIGHT_GRAY)
                
                
        elif event.type == pygame.KEYUP:
            self.btn0.change_bg_color(GRAY)
            self.btn1.change_bg_color(GRAY)
            self.btn2.change_bg_color(GRAY)
            self.btn3.change_bg_color(GRAY)
            self.btn4.change_bg_color(GRAY)
            self.btn5.change_bg_color(GRAY)
            self.btn6.change_bg_color(GRAY)
            self.btn7.change_bg_color(GRAY)
            self.btn8.change_bg_color(GRAY)
            self.btn9.change_bg_color(GRAY)
            self.btn_point.change_bg_color(GRAY)
                
    def get_value(self):
        return float(self.value)
            
    def append_value(self,new_value):
        # Set a limit of values that can be entered
        if self.text.get_width() < 260:
            if self.value == "0" or self.new_entry:
                self.value = new_value
                self.new_entry = False
            else:
                self.value += new_value
                
            self.text = self.font.render(self.value,True,BLACK)
            # Set key_pressed as true
            self.key_pressed = True
            
    def append_point(self):
        
        if self.new_entry:
            self.value = "0."
            self.text = self.font.render(self.value,True,BLACK)
            self.new_entry = False
        
        elif not "." in self.value:
            self.value += "."
            self.text = self.font.render(self.value,True,BLACK)
            
    def set_value(self,value):
        if value[-2:] == ".0":
            self.value = value[:-2]
        else:
            self.value = value
        self.new_entry = True
        self.text = self.font.render(self.value,True,BLACK)
        
    def draw(self,screen):
        #--- Calculate the x position
        posX = SCREEN_WIDTH - self.text.get_width() - 35
        #--- Draw rectangle with color green
        pygame.draw.rect(screen,GREEN,pygame.Rect(20,20,280,95))
        #--- Draw the text into the screen
        screen.blit(self.text,(posX,40))
        #--- Draw all the number buttons
        self.btn0.draw(screen)
        self.btn1.draw(screen)
        self.btn2.draw(screen)
        self.btn3.draw(screen)
        self.btn4.draw(screen)
        self.btn5.draw(screen)
        self.btn6.draw(screen)
        self.btn7.draw(screen)
        self.btn8.draw(screen)
        self.btn9.draw(screen)
        self.btn_point.draw(screen)