# Project Requirements
class Pokemon:
  def __init__(self, name, type, level=1, is_knocked_out=False):
    self.name = name
    self.level = level
    self.type = type
    self.max_health = level * 10
    self.current_health = level * 10
    self.is_knocked_out = is_knocked_out

  def __repr__(self):
        return "This level {level} {name} has {health} hit points remaining. They are a {type} type Pokemon".format(level=self.level,name=self.name, health=self.current_health, type = self.type)

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
      print("{} was revived and now has {} health".format(self.name, self.current_health))

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
        
charmander = Pokemon("Charmander", "Fire", 10)
squirtle = Pokemon("Squirtle", "Water", 10)
bulbasaur = Pokemon("Bulbasaur", "Grass", 10)
# pikachu.lose_health(10)
# #pikachu.gain_health(10)
# pikachu.knock_out()
# pikachu.revive()
# charmander.attack(bulbasaur)
# charmander.attack(squirtle)
# charmander.attack(charmander)

class Trainer:
  def __init__(self, name, pokemons, num_potions):
    self.name = name
    self.pokemons = pokemons
    self.num_potions = num_potions
    self.active_pokemon = 0

  def __repr__(self):
    print("The trainer {name} has the following pokemon".format(name=self.name))
    for pokemon in self.pokemons:
      print(pokemon)
    return "The current active pokemon is {name}".format(name=self.pokemons[self.active_pokemon].name)

  def use_a_potion(self, health):
    if self.num_potions > 0:
      print("You used a potion on {name}.".format(name = self.pokemons[self.active_pokemon].name))
      self.num_potions -= 1
      self.pokemons[self.active_pokemon].gain_health(health)
    else:
      print("You have run out of potions!")

  def attack_other_trainer(self, other_trainer):
      my_pokemon = self.pokemons[self.active_pokemon]
      their_pokemon = other_trainer.pokemons[other_trainer.active_pokemon]
      my_pokemon.attack(their_pokemon)

  def switch_active_pokemon(self, new_active):
      if new_active < len(self.pokemons) and new_active >= 0:
        if self.pokemons[new_active].current_health == 0:
          self.pokemons[new_active].knock_out()
          print("You can't make it your active pokemon")
        elif new_active == self.active_pokemon:
          print("{name} is already your active pokemon".format(name = self.pokemons[new_active].name))
            # Switches the pokemon
        else:
          self.active_pokemon = new_active
          print("Go {name}, it's your turn!".format(name = self.pokemons[self.active_pokemon].name))

trainer_1 = Trainer("Red", [charmander, squirtle, bulbasaur], 5)
trainer_2 = Trainer("Blue", [squirtle, bulbasaur, charmander], 3)
trainer_3 = Trainer("Yellow", [squirtle, charmander, bulbasaur], 2)

print(trainer_1)
print(trainer_2)

# trainer_1.attack_other_trainer(trainer_2)
# trainer_2.attack_other_trainer(trainer_1)
# trainer_1.attack_other_trainer(trainer_2)
# trainer_2.attack_other_trainer(trainer_1)
# trainer_1.attack_other_trainer(trainer_2)
# trainer_2.attack_other_trainer(trainer_1)
# trainer_1.attack_other_trainer(trainer_2)
# trainer_2.attack_other_trainer(trainer_1)
# trainer_1.attack_other_trainer(trainer_2)
# trainer_2.attack_other_trainer(trainer_1)

# trainer_1.use_a_potion(20)
# trainer_1.attack_other_trainer(trainer_2)
# trainer_2.attack_other_trainer(trainer_1)

# trainer_1.switch_active_pokemon(0)
# trainer_1.switch_active_pokemon(1)