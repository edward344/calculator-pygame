#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
from constants import *
from calculator import Calculator

def main():
    # Initialize all imported pygame modules
    pygame.init()
    # Set the width and height of the screen [width, height]
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    # Set the current window caption
    pygame.display.set_caption("Calculator")
    #Loop until the user clicks the close button.
    done = False
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
    # Create calculator object
    calculator = Calculator()
    # -------- Main Program Loop -----------
    while not done:
        # --- Main event loop
        # --- Process events (keystrokes, mouse clicks, etc)
        done = calculator.process_events()
        # --- Game logic should go here
        calculator.run_logic()
        # --- Draw the current frame
        calculator.display_frame(screen)
        # --- Limit to 30 frames per second
        clock.tick(30)
    # Close the window and quit.
    # If you forget this line, the program will 'hang'
    # on exit if running from IDLE.
    pygame.quit()

if __name__ == '__main__':
    main()