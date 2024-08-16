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

# Game loop
def game_loop():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Clear the screen
        window.fill(WHITE)

        # Draw resources
        draw_resources()

        # Draw UI elements (placeholder)
        pygame.draw.rect(window, GRAY, (50, 50, 200, 100))
        text = font.render("City Builder", True, BLACK)
        window.blit(text, (60, 80))

        # Update the display
        pygame.display.flip()

# Run the game loop
game_loop()
pygame.quit()