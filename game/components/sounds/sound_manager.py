import pygame

from game.utils.constants import SONG_GAME, SONG_LOSE,SONG_SHIELD,SONG_DEATH,SONG_MACHINEGUN

class SoundUtils:
    def sound_game_stop(self):
        SONG_GAME.stop()
        
    def sound_game_play(self):
        SONG_GAME.play()
    
    def sound_game_lose(self):
        SONG_LOSE.stop()
           
    def sound_game_lose(self):
        SONG_LOSE.play()
    
    def sound_shield(self):
        SONG_SHIELD.play()
    
    def sound_death(self):
        SONG_DEATH.play()
        
    def sound_machinegun(self):
        SONG_MACHINEGUN.play()
        