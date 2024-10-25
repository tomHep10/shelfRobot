import pygame
from robot import Robot
from utils import scale_image

robot = scale_image(pygame.image.load(r"C:\Users\tomhu\Desktop\Code\GitHub\shelfRobot\Robot.png"), 8)
robot_rect = robot.get_rect()

robotObj = Robot(robot_rect)

# Initialize Pygame
pygame.init()

# Set window dimensions
width = 800
height = 600

# Create the window
screen = pygame.display.set_mode((width, height))

# Set window title
pygame.display.set_caption("Robot Sim")

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Game logic (update game state, etc.)

    # Drawing (render graphics)
    screen.fill((255, 255, 255))
    robotObj.draw(screen, robot)
    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()