import random
from game.components.enemies.enemy import Enemy
from game.utils.constants import SCREEN_HEIGHT
class EnemyManager:

    def __init__(self):
        self.enemies = []
        self.index=0
    
    def update(self):
        self.add_enemy()
        for enemy in self.enemies:
            enemy.update()
            if enemy.rect.y >= SCREEN_HEIGHT:
                self.enemies.remove(enemy)
                
    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)

    def add_enemy(self):
        #añadi que haya 3 enemigos
        if len(self.enemies) < 3:
            #que este en un rango de 1 a 100
            self.index = random.randint(1,100)
            #divide entre 12 y saca la probabilidad de quien sale mas que si el residio sale en el rango de 0 a 7 
            if self.index % 12 <= 7  :
                enemy = Enemy(0)
            #divide entre 12 y saca la probabilidad de quien sale mas de 0 a 10
            elif self.index % 12 <= 10:            
                enemy = Enemy(1)
            #si no esta en el rango de 7 o 10 y si sale 11 saca este enemigo 
            else:
                enemy = Enemy(2)
            self.enemies.append(enemy)