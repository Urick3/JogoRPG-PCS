from attribute import Attribute

class Character:
    def __init__(self, name, race):
        self.name = name
        self.race = race
        self.attributes = self._initialize_attributes()

    def _initialize_attributes(self):
        attributes = {
            'Strength': Attribute('Strength', 0),
            'Dexterity': Attribute('Dexterity', 0),
            'Constitution': Attribute('Constitution', 0),
            'Wisdom': Attribute('Wisdom', 0),
            'Intelligence': Attribute('Intelligence', 0),
            'Charisma': Attribute('Charisma', 0)
        }
        
        for attr in attributes.values():
            attr.value = Attribute.random_value()
        
        race_bonuses = {
            'Dwarf': {'Constitution': 2},
            'Hill Dwarf': {'Wisdom': 1},
            'Mountain Dwarf': {'Strength': 2},
            'Elf': {'Dexterity': 2},
            'High Elf': {'Intelligence': 1},
            'Wood Elf': {'Wisdom': 1},
            'Dark Elf': {'Charisma': 1},
            'Barbarian': {'Dexterity': 2},
            'Lightfoot': {'Charisma': 1},
            'Stout': {'Constitution': 1},
            'Human': {attr: 1 for attr in attributes.keys()},
            'Dragonborn': {'Strength': 2, 'Charisma': 1},
            'Gnome': {'Intelligence': 2},
            'Forest Gnome': {'Dexterity': 1},
            'Rock Gnome': {'Constitution': 1},
            'Tiefling': {'Intelligence': 1, 'Charisma': 2}
        }
        
        if self.race in race_bonuses:
            for attr, bonus in race_bonuses[self.race].items():
                attributes[attr].value += bonus
        
        return attributes

    def get_attribute_status(self, attr_name):
        attr_value = self.attributes[attr_name].value

        status_mapping = {
            'Strength': {
                0: 'Incorpóreo',
                1: 'Incapaz',
                5: 'Incapaz',
                9: 'Fraco',
                11: 'Média',
                15: 'Forte',
                20: 'Super Poderoso',
                float('inf'): 'Imbatível'
            },
            'Dexterity': {
                0: 'Não acordado',
                1: 'Abatido',
                5: 'Abatido',
                9: 'Desajeitado',
                11: 'Regular',
                15: 'Ágil',
                20: 'Ninja',
                float('inf'): 'Imperceptível'
            },
            'Constitution': {
                0: 'Espectro',
                1: 'Doente',
                5: 'Doente',
                9: 'Frágil',
                11: 'Saudável',
                15: 'Difícil',
                20: 'Super resistente',
                float('inf'): 'Imortal'
            },
            'Wisdom': {
                0: 'Inconsciente',
                1: 'Irracional',
                5: 'Irracional',
                9: 'Desatento',
                11: 'Simples',
                15: 'Perspicaz',
                20: 'Filósofo',
                float('inf'): 'Iluminado'
            },
            'Intelligence': {
                0: 'Inanimado',
                1: 'Incivilizado',
                5: 'Incivilizado',
                9: 'Bobo',
                11: 'Mediocre',
                15: 'Estudado',
                20: 'Gênio',
                float('inf'): 'Onisciente'
            },
            'Charisma': {
                0: 'Aberração',
                1: 'Impressionante',
                5: 'Expressivo',
                9: 'Rude',
                11: 'Sociável',
                15: 'Persuasivo',
                20: 'Influente',
                float('inf'): 'Ídolo'
            }
        }

        for threshold, status in status_mapping[attr_name].items():
            if attr_value <= threshold:
                return status

    def __str__(self):
        attributes_str = "\n".join([f"{attr.name}: {attr.value} ({self.get_attribute_status(attr.name)})" for attr in self.attributes.values()])
        
        return f"{self.name} ({self.race}):\n({attributes_str})"