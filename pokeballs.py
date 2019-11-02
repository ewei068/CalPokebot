import random

common = ['bulbasaur', 'charmander', 'wartortle', 'caterpie', 'metapod', 'weedle', 'kakuna', 'pidgey', 'rattatta',
          'spearow', 'ekans', 'sandshrew', 'nidoran-f', 'nidoran-m', 'zubat', 'oddish', 'paras', 'venonat', 'diglet',
          'meowth', 'psyduck', 'mankey', 'poliwag', 'abra', 'machop', 'bellsprout', 'tentacool', 'geodude',
          'ponyta', 'magnemite', 'doduo', 'seel', 'grimer', 'shellder', 'ghastly', 'drowsee', 'krabby', 'voltorb'
                                                                                                        'cubone',
          'koffing', 'rhyhorn', 'horsea', 'goldeen', 'staryu', 'magikarp', 'eevee', 'porygon', 'omanyte',
          'kabuto', 'dratini', 'chikorita', 'cyndaquil', 'totodile', 'sentret', 'hoothoot', 'ledyba', 'spinarak',
          'chinchou', 'pichu', 'clefa', 'igglybuff', 'togepi', 'natu', 'mareep', 'hoppip', 'aipom', 'sunkern', 'wooper'
          'pineco', 'snubbull', 'quilfish', 'teddiursa', 'sulgma', 'swinub', 'corsola', 'remoraid', 'houndour',
          'phanpy', 'tyrouge', 'smoochum', 'elekid', 'magby', 'larvitar']

rare = ['ivysaur', 'charmeleon', 'wartortle', 'butterfree', 'beedrill', 'pidgeotto', 'raticate', 'fearow', 'arbok',
        'pikachu', 'sandslash', 'nidorina', 'nidorino', 'clefairy', 'vulpix', 'jigglypuff', 'golbat', 'gloom',
        'parasect', 'venomoth', 'dugtrio', 'persian', 'golduck', 'primeape', 'growlithe', 'poliwhirl', 'kadabra',
        'machoke', 'weepinbell', 'tentacruel', 'graveler', 'rapidash', 'slowpoke', 'magneton', 'farfetchd',
        'dodrio', 'dewgong', 'muk', 'cloyster', 'haunter', 'onix', 'hypno', 'kingler', 'electrode', 'exeggcute',
        'marowak', 'hitmonlee', 'hitmonchan', 'lickitung', 'weezing', 'rhydon', 'chansey', 'tangela', 'kangaskhan'
                                                                                                      'seadra',
        'seaking', 'starmie', 'mr-mime', 'scyther', 'jynx', 'electabuzz', 'magmar', 'pinsir', 'tauros',
        'omastar', 'kabutops', 'dragonair', 'bayleef', 'quilava', 'croconaw', 'furret', 'noctowl', 'ledian', 'ariados',
        'lanturn', 'togetic', 'xatu', 'flaaffy', 'marill', 'sudowoodo', 'skiploom', 'sunflora', 'yanma', 'quagsire',
        'murkrow', 'misdreavus', 'wobbuffet', 'girafarig', 'forretress', 'dunsparce', 'gligar', 'granbull', 'shuckle',
        'sneasel', 'ursaring', 'magcargo', 'piloswine', 'octillery', 'delibird', 'mantine', 'houndoom', 'donphan',
        'porygon2', 'stantler', 'hitmontop', 'miltank', 'pupitar']

epic = ['venusaur', 'charizard', 'blastoise', 'pidgeot', 'raichu', 'nidoqueen', 'nidoking', 'clefable', 'ninetails',
        'wigglytuff', 'vileplume', 'arcanine', 'poliwrath', 'alakazam', 'machamp', 'victreebel', 'golem', 'slowbro'
                                                                                                          'gengar',
        'exeggcutor', 'gyarados', 'lapras', 'vaporeon', 'jolteon', 'flareon', 'aerodactyl',
        'snorlax', 'dragonite', 'meganium', 'typhlosion', 'feraligatr', 'crobat', 'ampharos', 'bellossom', 'azumarill',
        'politoed', 'jumpluff', 'espeon', 'umbreon', 'slowking', 'steelix', 'scizor', 'heracross', 'skarmory', 'kingdra',
        'blissey', 'tyranitar']

legendary = ['articuno', 'zapdos', 'moltres', 'mewtwo', 'raikou', 'entei', 'suicune', 'ho-oh', 'lugia']

mythical = ['mew', 'celebi']


def poke():
    rarity_roll = random.choice(range(1, 101))
    if rarity_roll in range(1, 61):
        rarity = common
        rarity_name = 'common'
    elif rarity_roll in range(61, 86):
        rarity = rare
        rarity_name = 'rare'
    elif rarity_roll in range(86, 96):
        rarity = epic
        rarity_name = 'epic'
    elif rarity_roll in range(96, 100):
        rarity = legendary
        rarity_name = 'legendary'
    else:
        rarity = mythical
        rarity_name = 'mythical'

    pokemon_roll = random.choice(rarity)
    return pokemon_roll, rarity_name

def great():
    rarity_roll = random.choice(range(1, 101))
    if rarity_roll in range(1, 61):
        rarity = rare
        rarity_name = 'rare'
    elif rarity_roll in range(61, 91):
        rarity = epic
        rarity_name = 'epic'
    elif rarity_roll in range(91, 99):
        rarity = legendary
        rarity_name = 'legendary'
    else:
        rarity = mythical
        rarity_name = 'mythical'

    pokemon_roll = random.choice(rarity)
    return pokemon_roll, rarity_name

def ultra():
    rarity_roll = random.choice(range(1, 101))
    if rarity_roll in range(1, 61):
        rarity = epic
        rarity_name = 'epic'
    elif rarity_roll in range(61, 96):
        rarity = legendary
        rarity_name = 'legendary'
    else:
        rarity = mythical
        rarity_name = 'mythical'

    pokemon_roll = random.choice(rarity)
    return pokemon_roll, rarity_name

def master():
    rarity_roll = random.choice(range(1, 101))
    if rarity_roll in range(1, 91):
        rarity = legendary
        rarity_name = 'legendary'
    else:
        rarity = mythical
        rarity_name = 'mythical'

    pokemon_roll = random.choice(rarity)
    return pokemon_roll, rarity_name
