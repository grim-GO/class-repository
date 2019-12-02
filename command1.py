class Hero1:
    def __init__(self, h, w, g, c, n):
        self.height = h
        self.weight = w
        self.gender = g
        self.command = c
        self.namder = n
    def level_up(self):
        return "уровень героя повышен !"

class Soldier1(Hero1):
    def to_follow1(self,):
        return "(солдат 1): иду за героем"



class Soldier2(Hero1):
    def to_follow2(self,):
        return "(солдат 2): иду за героем"
