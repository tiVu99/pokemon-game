# Project Requirements
class Pokemon:
  def __init__(self, name, level, type, max_health, current_health, is_knocked_out=False):
    self.name = name
    self.level = level
    self.type = type
    self.max_health = max_health
    self.current_health = current_health
    self.is_knocked_out = is_knocked_out

  def lose_health(self, health):
    self.current_health -= health
    print("{} now has {} health".format(self.name, self.current_health))

  def gain_health(self, health):
    self.current_health += health
    print("{} now has {} health".format(self.name, self.current_health))

  def knock_out(self):
    if self.current_health is 0:
      self.is_knocked_out = True
      print("{} is knocked out".format(self.name))
    
  def revive(self):
    if self.is_knocked_out:
      self.current_health = self.max_health
      self.is_knocked_out = False
      print("{} is revived and now has {} health".format(self.name, self.current_health))

  def attack(self, other_pokemon):
    print("{} attacked {}...".format(self.name, other_pokemon.name))
    if self.type is other_pokemon.type:
      damage = self.level / 2
      other_pokemon.lose_health(damage)
    if (self.type is "Fire" and other_pokemon.type is "Grass") or (self.type is "Water" and other_pokemon.type is "Fire") or (self.type is "Grass" and other_pokemon.type is "Water"):
      damage = self.level * 2
      print("{} has lost!".format(other_pokemon.name))
      other_pokemon.lose_health(damage)
    if (self.type is "Fire" and other_pokemon.type is "Water") or (self.type is "Water" and other_pokemon.type is "Grass") or (self.type is "Grass" and other_pokemon.type is "Fire"):
      damage = self.level / 2
      other_pokemon.lose_health(damage)
        
charmander = Pokemon("Charmander", 10, "Fire", 100, 50)
squirtle = Pokemon("Squirtle", 10, "Water", 100, 50)
bulbasaur = Pokemon("Bulbasaur", 10, "Grass", 100, 50)
# pikachu.lose_health(10)
# #pikachu.gain_health(10)
# pikachu.knock_out()
# pikachu.revive()
charmander.attack(bulbasaur)
charmander.attack(squirtle)
charmander.attack(charmander)