#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
from constants import *
from button import Button
from calculator_input import Calculator_input

class Calculator(object):
    def __init__(self):
        # Declare all the buttons
        self.btn_substraction = Button(245,150,60,40,"-",BLUE)
        self.btn_addition = Button(245,210,60,40,"+",BLUE)
        self.btn_multiplication = Button(245,270,60,40,"x",BLUE)
        self.btn_division = Button(245,330,60,40,"/",BLUE)
        self.btn_equal = Button(170,330,60,40,"=",ORANGE)
        
        self.prevVal = 0
        self.newVal = 0
        self.operator = ""
        self.resultVal = 0
        
        # Declare the calculator_input 
        self.calculator_input = Calculator_input()
        
    def process_events(self):
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                return True
                
            self.calculator_input.event_handler(event)
            
            # Check for the buttons
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.btn_equal.isPressed():
                    self.calculate()
                    self.btn_equal.change_bg_color(LIGHT_ORANGE)
                                
                elif self.btn_addition.isPressed():
                    self.addition()
                    self.btn_addition.change_bg_color(LIGHT_BLUE)

                elif self.btn_substraction.isPressed():
                    self.substraction()
                    self.btn_substraction.change_bg_color(LIGHT_BLUE)
                    
                elif self.btn_multiplication.isPressed():
                    self.multiplication()
                    self.btn_multiplication.change_bg_color(LIGHT_BLUE)
                    
                elif self.btn_division.isPressed():
                    self.division()
                    self.btn_division.change_bg_color(LIGHT_BLUE)
                    
            elif event.type == pygame.MOUSEBUTTONUP:
                self.btn_equal.change_bg_color(ORANGE)
                self.btn_addition.change_bg_color(BLUE)
                self.btn_substraction.change_bg_color(BLUE)
                self.btn_multiplication.change_bg_color(BLUE)
                self.btn_division.change_bg_color(BLUE)
                    
            # Check for the keyboard
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_KP_PLUS:
                    self.addition()
                    self.btn_addition.change_bg_color(LIGHT_BLUE)
                    
                elif event.key == pygame.K_KP_MINUS:
                    self.substraction()
                    self.btn_substraction.change_bg_color(LIGHT_BLUE)
                    
                elif event.key == pygame.K_KP_MULTIPLY:
                    self.multiplication()
                    self.btn_multiplication.change_bg_color(LIGHT_BLUE)
                    
                elif event.key == pygame.K_KP_DIVIDE:
                    self.division()
                    self.btn_division.change_bg_color(LIGHT_BLUE)
                    
                elif event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                    self.calculate()
                    self.btn_equal.change_bg_color(LIGHT_ORANGE)
                
                elif event.key == pygame.K_ESCAPE:
                    self.calculator_input.set_value("0")
                    self.resultVal = 0
                    self.newVal = 0
                    self.prevVal = 0
                    self.operator = ""
                    
            elif event.type == pygame.KEYUP:
                self.btn_equal.change_bg_color(ORANGE)
                self.btn_addition.change_bg_color(BLUE)
                self.btn_substraction.change_bg_color(BLUE)
                self.btn_multiplication.change_bg_color(BLUE)
                self.btn_division.change_bg_color(BLUE)
                    
        return False
        
    
    def addition(self):
        self.prevVal = self.newVal
        self.operator = "+"
        self.calculator_input.set_value(str(self.newVal))
        
    def substraction(self):
        self.prevVal = self.newVal
        self.operator = "-"
        self.calculator_input.set_value(str(self.newVal))
        
    def multiplication(self):
        self.prevVal = self.newVal
        self.operator = "*"
        self.calculator_input.set_value(str(self.newVal))
        
    def division(self):
        self.prevVal = self.newVal
        self.operator = "/"
        self.calculator_input.set_value(str(self.newVal))
        
    def calculate(self):
        if self.operator == "+":
            self.resultVal = self.prevVal + self.newVal
            self.calculator_input.set_value(str(self.resultVal))
            self.newVal = self.resultVal
        elif self.operator == "-":
            self.resultVal = self.prevVal - self.newVal
            self.calculator_input.set_value(str(self.resultVal))
            self.newVal = self.resultVal
        elif self.operator == "*":
            self.resultVal = self.prevVal * self.newVal
            self.calculator_input.set_value(str(self.resultVal))
            self.newVal = self.resultVal
        elif self.operator == "/":
            try:
                self.resultVal = self.prevVal / self.newVal
                self.calculator_input.set_value(str(self.resultVal))
                self.newVal = self.resultVal
            except ZeroDivisionError:
                self.calculator_input.set_value("Math error")
                self.resultVal = 0
                self.newVal = 0
                self.prevVal = 0
                
        self.operator = ""
    
    def run_logic(self):
        if self.calculator_input.key_pressed:
            self.newVal = self.calculator_input.get_value()
            self.calculator_input.key_pressed = False
        
    def display_frame(self,screen):
        # First clear the screen with white.
        screen.fill(BACKGROUND_COLOR)
        #--- Drawing code should go here ---
        
        #--- Draw all the buttons:
        self.btn_substraction.draw(screen)
        self.btn_addition.draw(screen)
        self.btn_multiplication.draw(screen)
        self.btn_division.draw(screen)
        self.btn_equal.draw(screen)
        # --- Call the draw the calculator_input buttons
        self.calculator_input.draw(screen)
        
        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
        

