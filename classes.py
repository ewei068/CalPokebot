# classes.py
import random
import pickle
import math
import copy
from pokeballs import *
from typechart import *


class Pokemon():
    iv_spread = [31, 31, 31, 31, 31, 31]  # default IVs were 100 for testing
    nature = None  # may be implemented later
    type1 = None
    type2 = None
    damaging_moves = []

    def __init__(self, info, species, id, level: int = 75):
        self.id = id
        self.api_info = info  # gets pokemon info from api

        # sprite, species, level
        self.sprite = self.api_info["sprites"]["front_default"]
        self.species = species
        self.level = level

        # sets typing
        if len(self.api_info["types"]) == 1:
            self.type1 = self.api_info["types"][0]["type"]["name"]
        else:
            self.type1 = self.api_info["types"][0]["type"]["name"]
            self.type2 = self.api_info["types"][1]["type"]["name"]

        self.get_moves()  # retrieves current valid moves based on level
        self.moveset = {}
        # chooses four most recently-learned moves by level, or less if less moves are valid
        total_moves = 4 if len(self.damaging_moves) >= 4 else len(self.damaging_moves)
        for move_number in range(total_moves):
            self.moveset[move_number + 1] = self.damaging_moves[-move_number]

        # randomizes IVs
        self.iv_spread = [random.choice(range(0, 32)) for _ in range(6)]

        #sets base stats
        self.base_hp = self.api_info["stats"][5]["base_stat"]
        self.base_atk = self.api_info["stats"][4]["base_stat"]
        self.base_df = self.api_info["stats"][3]["base_stat"]
        self.base_satk = self.api_info["stats"][2]["base_stat"]
        self.base_sdf = self.api_info["stats"][1]["base_stat"]
        self.base_spd = self.api_info["stats"][0]["base_stat"]

        self.calculate_stats()  # calculates current stats based on base stats

    def calculate_stats(self):
        # stats calculated using main game formulas with level, IVs, and base stats (no EVs or nature yet)
        self.hp = math.floor((2 * self.base_hp + self.iv_spread[5]) * self.level / 100 + self.level + 10)
        self.atk = math.floor(math.floor((2 * self.base_atk + self.iv_spread[4]) * self.level / 100 + 5) * 1)
        self.df = math.floor(math.floor((2 * self.base_df + self.iv_spread[3]) * self.level / 100 + 5) * 1)
        self.satk = math.floor(math.floor((2 * self.base_satk + self.iv_spread[2]) * self.level / 100 + 5) * 1)
        self.sdf = math.floor(math.floor((2 * self.base_sdf + self.iv_spread[1]) * self.level / 100 + 5) * 1)
        self.spd = math.floor(math.floor((2 * self.base_spd + self.iv_spread[0]) * self.level / 100 + 5) * 1)

    def get_moves(self):
        # gets pre-cached move data
        cache_path = 'move_cache'
        dbfile = open(cache_path, 'rb')
        move_cache = pickle.load(dbfile)
        dbfile.close()

        # gets moves
        valid_moves = []
        damaging_moves = []

        # gets all moves learned by level up which within Pokemon's level
        for move in self.api_info["moves"]:
            learn_details = move["version_group_details"][-1]
            if learn_details["level_learned_at"] <= self.level and learn_details["move_learn_method"][
                "name"] == "level-up":
                valid_moves += [move]
        self.valid_moves = valid_moves

        # gets all level up moves which do damage
        for move in valid_moves:
            move_name = move["move"]["name"]
            move_data = move_cache[move_name]
            damage_type = (move_data["damage_class"]["name"] == "special" or move_data["damage_class"][
                "name"] == "physical") and move_data["power"]
            if damage_type:
                damaging_moves += [move_name]
        self.damaging_moves = damaging_moves


class BattlePokemon():
    hp = 0
    spd = 0
    fainted = False

    def __init__(self, owner, pokemon):
        self.pokemon = copy.copy(pokemon)  # copies Pokemon instance's stats
        self.owner = owner  # sets owner

    def attack(self, target, move_number):
        # gets pre-cached move data
        cache_path = 'move_cache'
        dbfile = open(cache_path, 'rb')
        move_cache = pickle.load(dbfile)
        dbfile.close()

        # gets move data
        move = self.pokemon.moveset[move_number]
        move_data = move_cache[move]
        move_type = move_data["type"]["name"]
        power, damage_class = move_data["power"], move_data["damage_class"]["name"]

        stab = 1.2 if move_type == self.pokemon.type1 or move_type == self.pokemon.type2 else 1  # checks for STAB bonus
        modifier = 1 * type_chart[move_type].get(target.pokemon.type1, 1) * type_chart[move_type].get(target.pokemon.type2, 1) * stab  # checks for type weakness or resistance

        # checks for physical or special
        if damage_class == 'physical':
            damage = math.floor(modifier * (((((2 * self.pokemon.level/5 + 2) * self.pokemon.atk * power)/target.pokemon.df)/50)+2))
        else:
            damage = math.floor(modifier * (
                        ((((2 * self.pokemon.level / 5 + 2) * self.pokemon.satk * power) / target.pokemon.sdf) / 50) + 2))

        remaining_hp = target.take_damage(damage)  # deals damage to defender
        return damage, remaining_hp, modifier  # returns results

    def take_damage(self, damage):
        self.pokemon.hp -= damage  # takes damage
        # checks for faint
        if self.pokemon.hp <= 0:
            self.owner.faint(self)
        return self.pokemon.hp

    def check_moves(self, move_number):
        # makes sure Pokemon knows selected move
        if move_number in self.pokemon.moveset.keys():
            return True
        return False

class Player():
    team = []
    active_pokemon = None

    def __init__(self, player):
        self.player = player

        # gets team
        self.team = self.team[:]
        team_path = 'users/' + str(player.id) + '/team'
        dbfile = open(team_path, 'rb')
        self.team_dict = pickle.load(dbfile)
        dbfile.close()

        # loads all Pokemon in team
        for _ in range(len(self.team_dict.keys())):
            pokemon_path = 'users/' + str(player.id) + '/pokemon/' + str(self.team_dict[_ + 1])
            dbfile = open(pokemon_path, 'rb')
            pokemon = pickle.load(dbfile)
            dbfile.close()
            self.team += [BattlePokemon(self, pokemon)]  # creates new instances for each Pokemon and adds them to team

    def send(self, slot):
        self.active_pokemon = self.team[slot-1]  # sends out chosen Pokemon

    def faint(self, pokemon):
        self.team = [poke for poke in self.team if poke is not pokemon]  # removes fainted Pokemon from team
        pokemon.fainted = True

    def check_slots(self, slot):
        if slot - 1 in range(len(self.team)):
            return True
        return False
