from game.utils.constants import MACHINEGUN, HEAVY_MACHINE_GUN_TYPE
from game.components.power_ups.power_up_shoot import PowerUps

class HeavyMachineGun(PowerUps):
    def __init__(self):
        super().__init__(MACHINEGUN, HEAVY_MACHINE_GUN_TYPE)
