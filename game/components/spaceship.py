import pygame
from pygame.sprite import Sprite

from game.utils.constants import SPACESHIP, SCREEN_HEIGHT, SCREEN_WIDTH

class Spaceship(Sprite):
    SPACESHIP_WIDTH = 40
    SPACESHIP_HEIGHT = 60
    X_POS = (SCREEN_WIDTH//2) - SPACESHIP_WIDTH//2
    Y_POS = 500
    SPEED = 10
    SCREEN_ERROR = 10

    def __init__(self):
        self.image = pygame.transform.scale(SPACESHIP,(self.SPACESHIP_WIDTH,self.SPACESHIP_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.type = 'type' 

    def update(self, user_input):
        #movimiento en diagonal hacia abajo izquierda
        if user_input[pygame.K_DOWN] and user_input[pygame.K_LEFT]:
            if self.rect.x == 0 and self.rect.bottom < SCREEN_HEIGHT:
                self.rect.x = SCREEN_WIDTH - self.SPACESHIP_WIDTH
                self.rect.y += 5
            if self.rect.left > 0 and self.rect.bottom < SCREEN_HEIGHT:
                self.rect.x -= 5
                self.rect.y += 5
        #movimiento diagonal hacia arriba izquierda
        elif user_input[pygame.K_UP] and user_input[pygame.K_LEFT]:
            if self.rect.x == 0 and self.rect.top > SCREEN_HEIGHT//2:
                self.rect.x = SCREEN_WIDTH - self.SPACESHIP_WIDTH
                self.rect.y -= 5
            if self.rect.left > 0 and self.rect.top > SCREEN_HEIGHT//2:
                self.rect.x -= 5
                self.rect.y -= 5
        #movimiento diagonal hacia arriba derecha
        elif user_input[pygame.K_UP] and user_input[pygame.K_RIGHT]:
            if self.rect.x > SCREEN_WIDTH-self.SPACESHIP_WIDTH and self.rect.top > SCREEN_HEIGHT//2:
                self.rect.x = self.SPEED
                self.rect.y -= 5
            if self.rect.right < SCREEN_WIDTH and self.rect.top > SCREEN_HEIGHT//2:
                self.rect.x += 5
                self.rect.y -= 5
        #movimiento diagonal hacia abajo derecha
        elif user_input[pygame.K_DOWN] and user_input[pygame.K_RIGHT]:
            if self.rect.x > SCREEN_WIDTH-self.SPACESHIP_WIDTH and self.rect.bottom < SCREEN_HEIGHT:
                self.rect.x = self.SPEED
                self.rect.y += 5
            if self.rect.right < SCREEN_WIDTH and self.rect.bottom < SCREEN_HEIGHT:
                self.rect.x += 5
                self.rect.y += 5

        #va a la izquierda 
        elif user_input[pygame.K_LEFT]:
            if self.rect.x == 0:
                self.rect.x = SCREEN_WIDTH - self.SPACESHIP_WIDTH
            if self.rect.left > 0:
                self.rect.x -= self.SPEED
        #va a la derecha
        elif user_input[pygame.K_RIGHT]:
            if self.rect.x > SCREEN_WIDTH - self.SPACESHIP_WIDTH - self.SCREEN_ERROR:
                self.rect.x = self.SPEED
            if self.rect.right < SCREEN_WIDTH:
                self.rect.x += self.SPEED
        #va arriba
        elif user_input[pygame.K_UP]:
            if self.rect.top > SCREEN_HEIGHT//2:
                self.rect.y -= self.SPEED
        #va abajo
        elif user_input[pygame.K_DOWN]:
            if self.rect.bottom < SCREEN_HEIGHT: 
                self.rect.y += self.SPEED   

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

