from tartaro.monster import Monster

class Equidna(Monster):
    def __init__(self, level, especie, class_):
        super().__init__(level, especie, class_)

    modifiers = { "Beast": [2, 1, 0, 3, 3], "Demon": [1, 2, 3, 2, 1], "Dragon": [8, 5, 4, 6, 8],
                  "Elemental": [1, 3, 2, 1, 2], "Fairy": [0, 3, 3, 2, 1], "Human": [2, 2, 2, 2, 2],
                    "Insect": [2, 1, 1, 4, 1], "Plant": [3, 1, 1, 1, 4], "Undead": [4, 0, 0, 1, 4] }
    
    grown_factor = { "Beast": 1.2, "Demon": 1.2, "Dragon": 1.4, "Elemental": 1.2, "Fairy": 1.1, 
                    "Human": 1.1,"Insect": 1.1, "Plant": 1.2, "Undead": 1 }

    @classmethod
    def create_horde(cls, especie, class_, **levels):
        horde = [cls(i, especie, class_) for i in levels]


    def apply_especie_modifiers(self, modifiers, grown_factor):
        for key, value in modifiers.items():
            if key == self.especie:
                self.attribute["strength"] += (value[0] + round(self.level * grown_factor[self.especie]))
                self.attribute["inteligence"] += (value[1] + round(self.level * grown_factor[self.especie]))
                self.attribute["dexterity"] += (value[2] + round(self.level * grown_factor[self.especie]))
                self.attribute["speed"] += (value[3] + round(self.level * grown_factor[self.especie]))
                self.attribute["vitality"] += (value[4] + round(self.level * grown_factor[self.especie]))
                break
                
        self.update_stats()

    def __repr__(self):
        return f'Equidna({self.name})'