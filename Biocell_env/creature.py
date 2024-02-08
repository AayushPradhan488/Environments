# creature.py
import random
from environment import BOARD_SIZE, BLOCK_SIZE
import pygame

# Directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

#Colours
RED = (255, 0, 0)
GREEN = (0, 255, 0)
GREY = (128, 128, 128)

# Creature class
class Creature:
    def __init__(self):
        self.body = [(random.randint(0, BOARD_SIZE - 1), random.randint(0, BOARD_SIZE - 1))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.color = GREEN
        self.health = 100
        self.is_alive = True

    def move(self):
        if self.is_alive:
            head = self.body[0]
            new_head = ((head[0] + self.direction[0]) % BOARD_SIZE, (head[1] + self.direction[1]) % BOARD_SIZE)
            self.body.insert(0, new_head)

    def affect_health(self, toxicity, toxic_pool):
        if self.body[0] in toxic_pool and self.health>0:
            self.health += toxicity
            if self.health <= 0:
                self.is_alive = False

    def draw(self, surface):
        if self.is_alive:
            pygame.draw.rect(surface, GREEN, ((self.body[0][0] * BLOCK_SIZE)+(BLOCK_SIZE*0.1), (self.body[0][1] * BLOCK_SIZE)+(BLOCK_SIZE*0.1), BLOCK_SIZE*0.95, BLOCK_SIZE*0.95))
        else:
            pygame.draw.rect(surface, GREY, ((self.body[0][0] * BLOCK_SIZE)+(BLOCK_SIZE*0.1), (self.body[0][1] * BLOCK_SIZE)+(BLOCK_SIZE*0.1), BLOCK_SIZE*0.95, BLOCK_SIZE*0.95))