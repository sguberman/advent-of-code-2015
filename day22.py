import random


def game_over(wizard, boss):
    if wizard['hp'] <= 0 or wizard['mp'] <= 0:
        return 'lose'
    elif boss['hp'] <= 0:
        return 'win'
    else:
        return False


def boss_attack(wizard, boss):
    damage = boss['dp'] - wizard['ap']
    if damage <= 0:
        damage = 1
    wizard['hp'] -= damage
    return wizard


def magic_missile(timers, wizard, boss):
    cost = 53
    wizard['mp'] -= cost
    boss['hp'] -= 4
    return cost, timers, wizard, boss


def drain(timers, wizard, boss):
    cost = 73
    wizard['mp'] -= cost
    boss['hp'] -= 2
    wizard['hp'] += 2
    return cost, timers, wizard, boss


def cast_shield(timers, wizard, boss):
    cost = 113
    timers['shield'] = 6
    wizard['mp'] -= cost
    return cost, timers, wizard, boss


def shield_check(timers, wizard):
    if timers['shield']:
        timers['shield'] -= 1
        wizard['ap'] = 7
    else:
        wizard['ap'] = 0
    return timers, wizard


def cast_poison(timers, wizard, boss):
    cost = 173
    timers['poison'] = 6
    wizard['mp'] -= cost
    return cost, timers, wizard, boss


def poison_check(timers, boss):
    if timers['poison']:
        timers['poison'] -= 1
        damage = 3
    else:
        damage = 0
    boss['hp'] -= damage
    return timers, boss


def cast_recharge(timers, wizard, boss):
    cost = 229
    timers['recharge'] = 5
    wizard['mp'] -= cost
    return cost, timers, wizard, boss


def recharge_check(timers, wizard):
    if timers['recharge']:
        timers['recharge'] -= 1
        mp_up = 101
    else:
        mp_up = 0
    wizard['mp'] += mp_up
    return timers, wizard


def wizard_move(timers, wizard):
    moves = [magic_missile, drain, cast_shield, cast_poison, cast_recharge]
    if timers['shield'] or wizard['mp'] < 113:
        moves.remove(cast_shield)
    if timers['poison'] or wizard['mp'] < 173:
        moves.remove(cast_poison)
    if timers['recharge'] or wizard['mp'] < 229:
        moves.remove(cast_recharge)
    if wizard['mp'] < 53:
        moves.remove(magic_missile)
    if wizard['mp'] < 73:
        moves.remove(drain)
    return random.choice(moves)


def simulate():
    boss = {'hp': 51,
            'dp': 9,
            }

    wizard = {'hp': 50,
              'mp': 500,
              'ap': 0,
              }

    timers = {'shield': 0,
              'poison': 0,
              'recharge': 0,
              }

    nextup = 'wizard'
    total_cost = 0
    while not game_over(wizard, boss):
        timers, wizard = shield_check(timers, wizard)
        timers, boss = poison_check(timers, boss)
        timers, wizard = recharge_check(timers, wizard)
        if game_over(wizard, boss):
            break
        if nextup == 'wizard':
            if wizard['mp'] < 53:
                wizard['mp'] = 0
                break
            move = wizard_move(timers, wizard)
            cost, timers, wizard, boss = move(timers, wizard, boss)
            total_cost += cost
            nextup = 'boss'
        else:
            wizard = boss_attack(wizard, boss)
            nextup = 'wizard'
    return total_cost, game_over(wizard, boss)


def simulation(n=100):
    costs = []
    for _ in range(n):
        cost, result = simulate()
        if result == 'win':
            costs.append(cost)
    return len(costs), min(costs), max(costs), sum(costs)/len(costs)


if __name__ == '__main__':
    print simulation(n=100000)
