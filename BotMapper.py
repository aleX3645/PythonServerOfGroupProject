class BotMapper:
    __charge = 0.0
    __weight = 0.0
    __speed = 0.0
    __tiredness = 0.0
    __range = 0.0
    __damage = 0.0
    __game_field = [[]]

    def __init__(self, charge: float, weight: float, speed: float, tiredness: float, damage: float, rang: float,
                 position_x: int, position_y: int, game_field):
        self.__game_field = game_field
        self.__charge = charge
        self.__weight = weight
        self.__tiredness = tiredness
        self.__speed = speed
        self.__rang = rang
        self.__damage = damage
        self.__position_y = position_y
        self.__position_x = position_x

    def get_tiredness(self):
        return self.__tiredness

    def get_charge(self):
        return self.__charge

    def get_speed(self):
        return self.__speed

    def get_weight(self):
        return self.__weight


