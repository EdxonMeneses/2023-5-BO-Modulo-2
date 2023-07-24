import pygame
import os
pygame.mixer.init()

# Global Constants
TITLE = "Spaceships Game"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))

SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

MACHINEGUN = pygame.image.load(os.path.join(IMG_DIR, "Other/MachineGun.png"))

DEFAULT_TYPE = "default"
SHIELD_TYPE = 'shield'
HEAVY_MACHINE_GUN_TYPE = 'machinegun'

SPACESHIP = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))
SPACESHIP_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship_shield.png"))

BULLET = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_1.png"))
BULLET_ENEMY = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_2.png"))
ENEMY_1 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_1.png"))
ENEMY_2 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_2.png"))

SONG_GAME = pygame.mixer.Sound(os.path.join(IMG_DIR,"Song/songGame.mp3"))
SONG_LOSE = pygame.mixer.Sound(os.path.join(IMG_DIR,"Song/songLose.mp3"))
SONG_SHIELD = pygame.mixer.Sound(os.path.join(IMG_DIR,"Song/songShield.mp3"))
SONG_DEATH = pygame.mixer.Sound(os.path.join(IMG_DIR,"Song/songDeath.mp3"))
SONG_MACHINEGUN = pygame.mixer.Sound(os.path.join(IMG_DIR,"Song/HeavyMachineGun.mp3"))
    

FONT_STYLE = 'freesansbold.ttf'
