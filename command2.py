class Hero2:
    def __init__(self, h, w, g, c, n, s):
        self.height = h
        self.weight = w
        self.gender = g
        self.command = c
        self.namder = n
        self.superpower = s
    def level_up(self):
        return "уровень героя повышен !"

class Soldier3(Hero2):
    def to_follow3(self,):
        return "(солдат 3): иду за героем"



class Soldier4(Hero2):
    def to_follow4(self,):
        return "(солдат 4): иду за героем"