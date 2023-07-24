import pygame
import random
from game.components.power_ups.heavy_machine_gun import HeavyMachineGun
from game.components.power_ups.shield import Shield
from game.utils.constants import SCREEN_HEIGHT, SPACESHIP_SHIELD,SPACESHIP


class PowerUPManager:
    def __init__(self):
        self.power_ups = []
        self.power_ups_shoot = []
        self.when_appears = random.randint(5000,10000)
        self.duration = random.randint(3,5)

    def update(self, game):
        current_time = pygame.time.get_ticks()  
        if len(self.power_ups) == 0 and current_time >= self.when_appears:
            power_up = Shield()
            power_up_shoot = HeavyMachineGun()
            self.when_appears += random.randint(5000,10000)
            self.power_ups.append(power_up)
            self.power_ups_shoot.append(power_up_shoot)

        for power_up in self.power_ups: 
            power_up.update(game.game_speed)
            if power_up.rect.y >= SCREEN_HEIGHT:
                self.power_ups.remove(power_up)
            if game.player.rect.colliderect(power_up.rect):
                power_up.start_time = pygame.time.get_ticks()
                game.player.power_up_type = power_up.type
                game.player.has_power_up = True
                game.player.power_time_up = power_up.start_time + (self.duration *1000)
                game.player.set_image((65,75), SPACESHIP_SHIELD)
                game.sound_game.sound_shield()
                self.power_ups.remove(power_up) 
                for power_up_shoot in self.power_ups_shoot:
                    self.power_ups_shoot.remove(power_up_shoot) 
                current_time = pygame.time.get_ticks()  

        for power_up_shoot in self.power_ups_shoot:
            power_up_shoot.update(game.game_speed)
            if power_up_shoot.rect.y >= SCREEN_HEIGHT:
                self.power_ups_shoot.remove(power_up_shoot)
            if game.player.rect.colliderect(power_up_shoot.rect):
                power_up_shoot.star_time = pygame.time.get_ticks()
                game.player.power_up_type = power_up_shoot.type
                game.player.has_power_up_shoot = True
                game.player.power_time_up = power_up_shoot.star_time + (self.duration *1000)
                game.player.set_image((65,75))
                game.sound_game.sound_machinegun()
                self.power_ups_shoot.remove(power_up_shoot)
                self.power_ups.remove(power_up)
                game.bullet_manager.burst = 3
                current_time = pygame.time.get_ticks()  
                
    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

        for power_up_shoot in self.power_ups_shoot:
            power_up_shoot.draw(screen)