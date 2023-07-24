import random
from game.utils.constants import SCREEN_WIDTH
from pygame.sprite import Sprite

class PowerUps(Sprite):
    def __init__(self, image, type):
        self.image = image 
        self.rect = self.image.get_rect()
        self.rect.y = 0
        self.rect.x = random.randint(20, SCREEN_WIDTH - 500)
        self.type = type
        self.star_time = 0

    def update(self,game_speed):
        self.rect.y += game_speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)