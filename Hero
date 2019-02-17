from abc import ABC, abstractmethod


class Hero():
    def __init__(self):
        self.positive_effects = []
        self.negative_effects = []
        self.stats = {
            "HP": 128,
            "MP": 42,
            "SP": 100,
            "Strength": 15,
            "Perception": 4,
            "Endurance": 8,
            "Charisma": 2,
            "Intelligence": 3,
            "Agility": 8,
            "Luck": 1} 
        
    def get_positive_effects(self):
        return self.positive_effects.copy()
    
    def get_negative_effects(self):
        return self.negative_effects.copy()
    
    def get_stats(self):
        return self.stats.copy()


class AbstractEffect(Hero, ABC):

    def __init__(self, base):
        self.base = base

    def get_positive_effects(self):
        return self.base.get_positive_effects()

    def get_negative_effects(self):
        return self.base.get_negative_effects()

    @abstractmethod
    def get_stats(self):
        return self.base.get_stats()


class AbstractPositive(AbstractEffect, ABC):

    def get_positive_effects(self):
        classname = type(self).__name__
        return self.base.get_positive_effects() + [classname]


class AbstractNegative(AbstractEffect, ABC):

    def get_negative_effects(self):
        classname = type(self).__name__
        return self.base.get_negative_effects() + [classname]


class Berserk(AbstractPositive):

    def get_stats(self):
        stats = self.base.get_stats().copy()
        stats['Strength'] += 7
        stats['Endurance'] += 7
        stats['Agility'] += 7
        stats['Luck'] += 7
        stats['Intelligence'] -= 3
        stats['Perception'] -= 3
        stats['Charisma'] -= 3
        stats['HP'] += 50
        return stats


class Blessing(AbstractPositive):
    
    def get_stats(self):
        stats = self.base.get_stats().copy()
        for a, b in stats.items():
            stats[a] = b + 2
        return stats


class Weakness(AbstractNegative):

    def get_stats(self):
        stats = self.base.get_stats().copy()
        stats['Strength'] -= 4
        stats['Endurance'] -= 4
        stats['Agility'] -= 4
        return stats


class Curse(AbstractNegative):

    def get_stats(self):
        stats = self.base.get_stats().copy()
        for a, b in stats.items():
            stats[a] = b - 2
        return stats


class EvilEye(AbstractNegative):

    def get_stats(self):
        stats = self.base.get_stats().copy()        
        stats['Luck'] -= 10
        return stats


nyako = Hero()
print(nyako.get_positive_effects())
print(nyako.get_negative_effects())
print(nyako.get_stats())

imbonyako_on_blessing = Blessing(nyako)
print(imbonyako_on_blessing.get_positive_effects())
print(imbonyako_on_blessing.get_negative_effects())
print(imbonyako_on_blessing.get_stats())

imbonyako_on_blessing_on_bers = Berserk(imbonyako_on_blessing)
print(imbonyako_on_blessing_on_bers.get_positive_effects())
print(imbonyako_on_blessing_on_bers.get_negative_effects())
print(imbonyako_on_blessing_on_bers.get_stats())

imbonyako_on_blessing_on_bers_on_curse = Curse(imbonyako_on_blessing_on_bers)
print(imbonyako_on_blessing_on_bers_on_curse.get_positive_effects())
print(imbonyako_on_blessing_on_bers_on_curse.get_negative_effects())
print(imbonyako_on_blessing_on_bers_on_curse.get_stats())
