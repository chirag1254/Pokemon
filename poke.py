import random

class Pokemon:
    max_hp = 100
    def __init__(self,name,primary_type):
        self.name = name
        self.primary_type = primary_type
        self.hp = Pokemon.max_hp
        self.max_hp = Pokemon.max_hp

    def __str__(self):
        return f"{self.name} ({self.primary_type}: {self.hp} / {self.max_hp})"

    def Feed(self):
        if self.hp < self.max_hp:
            self.hp +=1
            print(f"{self.name} has now {self.hp} HP")
        else:
            print(f"{self.name} is full")
    def Battle(self,other):
        print('Battle',self.name,other.name)
        result = self.type_wheel(self.primary_type ,other.primary_type)
        if result == 'Lose':
            self.hp -= 10
            print(f"{self.name} lost and now has {self.hp} HP.")
        print(f"{self.name} fought {other.name} and the result is a {result}")
    
    @staticmethod
    def type_wheel(type_1,type_2):
        result = {0:'Lose',1:'Win',-1 :'Tie'}
        # mapping between types and resutl conditions
        game_map = {'water':0,'fire':1,'grass':2}
        # implement win-lose matrix
        wl_matrix = [
            [-1,1,0] ,#water,
            [0,-1,1] ,#fire
            [1,0,-1] #grass
            ]
        # declare result
        wl_result = wl_matrix[game_map[type_1]][game_map[type_2]]
        return result[wl_result]

if __name__ == '__main__':
    pokemon_dict = {'balbasuar':'grass','charmender':'grass','Abomasnow':'grass',
                'Arcanine':'fire','Blaziken':'fire','Braixen':'fire',
                'Alomomola':'water','Araquanid':'water'}
    
    pokemon_name_list = [poke for poke in pokemon_dict.keys()]
    
    pk_input = str(input("Enter your pokemon's name "))
    primary_type = str(input("Enter it's primary type "))
    
    
    pokemon = Pokemon(pk_input,primary_type)
    # selecting random enemy
    
    enemy_poke_name = random.choice([poke for poke in pokemon_dict.keys()])
    enemy = Pokemon(enemy_poke_name,pokemon_dict[enemy_poke_name])
    #start Battle 
    input('Click to start battle')
    
  
    pokemon.Battle(enemy)