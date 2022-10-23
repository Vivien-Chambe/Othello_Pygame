import pygame, tkinter as tk
import fonctions as f
import classes as c
from tkinter import messagebox

# Initialize pygame
pygame.init()
# Set the width and height of the screen [width, height]
size = (400, 400)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Othello")

# Loop until the user clicks the close button.
done = False
# Used to manage how fast the screen updates
clock = pygame.time.Clock()


board = c.Board()

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            x = pos[0] // 50 #Because the board is 8x8, each square is 50x50
            y = pos[1] // 50
            board.add(x, y) #Add the piece to the square the user clicked on
            board.outflank(x, y) #Change the color of the pieces between the two pieces of the same color
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                board.reset()

    # --- Game logic should go here

    # --- Drawing code should go here
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill((255, 255, 255))
    board.draw(screen)


    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)