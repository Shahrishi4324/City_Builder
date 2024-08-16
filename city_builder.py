import pygame

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("City Builder")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Font
font = pygame.font.Font(None, 36)

# Resource quantities
resources = {
    "wood": 100,
    "stone": 100,
    "food": 100,
}

# Function to draw resources on the screen
def draw_resources():
    y_offset = 20
    for resource, amount in resources.items():
        text = font.render(f"{resource.capitalize()}: {amount}", True, BLACK)
        window.blit(text, (10, y_offset))
        y_offset += 40

# Structure list
structures = []

# Function to draw structures
def draw_structures():
    for structure in structures:
        pygame.draw.rect(window, GREEN, structure)

# Function to add a structure
def add_structure(x, y):
    if resources["wood"] >= 50 and resources["stone"] >= 30:
        structures.append(pygame.Rect(x, y, 50, 50))
        resources["wood"] -= 50
        resources["stone"] -= 30

import random

# Function to trigger a natural disaster
def trigger_disaster():
    if random.random() < 0.1:  # 10% chance each tick
        if structures:
            destroyed = random.choice(structures)
            structures.remove(destroyed)
            resources["wood"] -= 20
            resources["stone"] -= 20
            print("A disaster occurred! A structure was destroyed.")

# Game loop
def game_loop():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                add_structure(x, y)

        # Clear the screen
        window.fill(WHITE)

        # Trigger random events
        trigger_disaster()

        # Draw resources
        draw_resources()

        # Draw structures
        draw_structures()

        # Update the display
        pygame.display.flip()

# Run the game loop
game_loop()
pygame.quit()