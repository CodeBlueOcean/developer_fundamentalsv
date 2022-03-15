class PlayerCharacter:
    def _init_(self, name, age):
        self.name = name
        self.age = age
    
    def run(self):
        return self

player1 = PlayerCharacter('andrei', 100) 

print(player1.run())

