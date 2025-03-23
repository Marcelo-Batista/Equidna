class Monster:
    def __init__(self, level, especie, class_):
        self.name = ""
        self.level = int(level)
        self.especie = especie
        self.class_ = class_
        self.attribute = {"strength": 0, "inteligence": 0, "dexterity": 0, "speed": 0, "vitality": 0}
        self.hp = 0 #10 * self.attribute["vitality"]
        self.mp = 0 #10 * self.attribute["inteligence"]
        self.attack = 0 #(self.attribute["strength"] + self.attribute["dexterity"]) * 2
        self.defense = 0 #(self.attribute["vitality"] + self.attribute["speed"]) * 2
        self.skills = []
        self.items = []

    def update_stats(self):
        self.hp = 10 * (self.attribute["vitality"] + self.level)
        self.mp = 10 * (self.attribute["inteligence"] + self.level)
        self.attack = (self.attribute["strength"] + self.attribute["dexterity"]) * 2 + self.level
        self.defense = (self.attribute["vitality"] + self.attribute["speed"]) * 2 + self.level

    def __str__(self):
        return f'{self.name} ({self.especie}), {self.level}\n HP: {self.hp}, MP: {self.mp}\n ATK: {self.attack}, DEF: {self.defense}\n Skills: {", ".join(self.skills)}'