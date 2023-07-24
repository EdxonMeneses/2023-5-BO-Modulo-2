import pygame

from game.utils.constants import SONG_GAME, SONG_LOSE,SONG_SHIELD

class SoundUtils:
    def sound_game_stop(self):
        SONG_GAME.stop
        
    def sound_game_play(self):
        SONG_GAME.play()
        
    def sound_game_lose(self):
        SONG_LOSE.play()
    
    def sound_shield(self):
        SONG_SHIELD.play()
        