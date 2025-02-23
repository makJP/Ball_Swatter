import pygame
import random
import image
from settings import *
from red import Red

class Green(Red):
    def __init__(self):
        #size
        random_size_value = random.uniform(GREEN_SIZE_RANDOMIZE[0], GREEN_SIZE_RANDOMIZE[1])
        size = (int(GREENS_SIZES[0] * random_size_value), int(GREENS_SIZES[1] * random_size_value))
        # moving
        moving_direction, start_pos = self.define_spawn_pos(size)
        # sprite
        self.rect = pygame.Rect(start_pos[0], start_pos[1], size[0]//1.4, size[1]//1.4)
        self.images = [image.load("Assets/green/GREEN.png", size=size, flip=moving_direction=="right")] # load the image
        self.current_frame = 0
        self.animation_timer = 0
        

    def kill(self, red): # remove the red ball from the list
        red.remove(self)
        return -GREEN_PENALITY
