# main.py
import pygame
from environment import *
from creature import Creature

# Initialize Pygame
pygame.init()

NUM_CREATURES = 10
NUM_MOVES = 20

SNAKE_SPEED = 5

# Main function
def main():
    # Initialize screen
    screen = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption("Bacterial Simulation")

    # Initialize clock
    clock = pygame.time.Clock()

    # Initialize game objects
    environment = Environment()
    creatures = [Creature() for _ in range(NUM_CREATURES)]

    # Game loop
    running = True
    moves_counter = 0
    while running and moves_counter < NUM_MOVES:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Move all creatures
        for creature in creatures:
            creature.move()

        # Affect creature health based on toxic pool
        for creature in creatures:
            creature.affect_health(environment.toxicity, environment.toxic_pool)

        # Draw objects
        screen.fill(WHITE)
        environment.draw_grid(screen)
        environment.draw_toxic_pool(screen)
        for creature in creatures:
            creature.draw(screen)
        pygame.display.flip()

        # Increment moves counter
        moves_counter += 1

        # Cap the frame rate
        clock.tick(SNAKE_SPEED)

    # Quit Pygame
    pygame.quit()

if __name__ == "__main__":
    main()
