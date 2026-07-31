class Enemy:

    def __init__(self,type_of_animal,attack_damage, health_points ):
        self.type_of_animal = type_of_animal
        self.attack_damage = attack_damage
        self.health_points = health_points


    def talk(self):
        print(f'I am a {self.type_of_animal} . Be Prepared to fight!')

    def walk_forward(self):
        print(f'{self.type_of_animal} moves closer to you')
    