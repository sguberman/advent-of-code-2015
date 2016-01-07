from itertools import product, combinations


def hits_to_win(player_attack, boss_armor, boss_hp):
    damage_per_turn = player_attack - boss_armor
    if damage_per_turn < 1:
        damage_per_turn = 1
    hits = boss_hp // damage_per_turn
    return hits


boss_hp = 100
boss_attack = 8
boss_armor = 2

player_hp = 100
player_attack = range(4, 13 + 1)
player_armor = range(0, 10 + 1)
stats = product(player_attack, player_armor)

winning_stats = []
for attack, armor in stats:
    boss_win = hits_to_win(boss_attack, armor, player_hp)
    player_win = hits_to_win(attack, boss_armor, boss_hp)
    if boss_win >= player_win:
        winning_stats.append((attack, armor))


weapons = {'dagger': {'cost': 8, 'attack': 4},
           'shortsword': {'cost': 10, 'attack': 5},
           'warhammer': {'cost': 25, 'attack': 6},
           'longsword': {'cost': 40, 'attack': 7},
           'greataxe': {'cost': 74, 'attack': 8},
           }

armor = {'none': {'cost': 0, 'armor': 0},
         'leather': {'cost': 13, 'armor': 1},
         'chainmail': {'cost': 31, 'armor': 2},
         'splintmail': {'cost': 53, 'armor': 3},
         'bandedmail': {'cost': 75, 'armor': 4},
         'platemail': {'cost': 102, 'armor': 5},
         }

rings = {'attack1': {'attack': 1, 'armor': 0, 'cost': 25},
         'attack2': {'attack': 2, 'armor': 0, 'cost': 50},
         'attack3': {'attack': 3, 'armor': 0, 'cost': 100},
         'armor1': {'attack': 0, 'armor': 1, 'cost': 20},
         'armor2': {'attack': 0, 'armor': 2, 'cost': 40},
         'armor3': {'attack': 0, 'armor': 3, 'cost': 80},
         'none1': {'attack': 0, 'armor': 0, 'cost': 0},
         'none2': {'attack': 0, 'armor': 0, 'cost': 0},
         }

loadouts = product(weapons, armor, combinations(rings, 2))
winning_gear = []
losing_gear = []
for w, a, (r1, r2) in loadouts:
    attack = sum(item['attack'] for item in (weapons[w], rings[r1], rings[r2]))
    defense = sum(item['armor'] for item in (armor[a], rings[r1], rings[r2]))
    cost = sum(item['cost'] for item in (weapons[w], armor[a], rings[r1], rings[r2]))
    if (attack, defense) in winning_stats:
        winning_gear.append((cost, (w, a, r1, r2), (attack, defense)))
    else:
        losing_gear.append((cost, (w, a, r1, r2), (attack, defense)))

print(sorted(winning_gear)[0])
print(sorted(losing_gear, reverse=True)[0])
