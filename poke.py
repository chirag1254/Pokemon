class Pokemon:
    def __init__(self,name,primary_type,max_hp):
        self.name = name
        self.primary_type = primary_type
        self.hp = max_hp
        self.max_hp = max_hp
    def __str__(self):
        return f"{self.name} ({self.primary_type}: {self.hp} / {self.max_hp})"

    def feed(self):
        if self.hp < self.max_hp:
            self.hp +=1
            print(f"{self.name} has now {self.hp} HP")
        else:
            print(f"{self.name} is full")


if __name__ == '__main__':
    print(Pokemon('bulbasore', 'grass'))