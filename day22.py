class Battle(object):

    def __init__(self, player, boss):
        self.player = player
        self.boss = boss

    def turn(self):
        print '\n-- Player turn --'
        self.print_stats()
        self.update_effects()
        self.is_over()
        self.player.magic_missile(self.boss)
        self.is_over()
        print '\n-- Boss turn --'
        self.print_stats()
        self.update_effects()
        self.is_over()
        self.boss.attack(self.player)
        self.is_over()

    def print_stats(self):
        print '- Player has {} hit points, {} amror, {} mana'.format(self.player.hp,
                                                                     self.player.ap,
                                                                     self.player.mp)
        print '- Boss has {} hit points'.format(self.boss.hp)

    def update_effects(self):
        print 'No effects...'

    def is_over(self):
        if self.player.hp <= 0:
            print 'Player dies!'
            return True
        elif self.player.mp <= 0:
            print 'Player loses!'
            return True
        elif self.boss.hp <= 0:
            print 'Boss dies!'
            return True
        else:
            return False


class Wizard(object):

    def __init__(self, hp=50, ap=0, mp=500):
        self.hp = hp
        self.ap = ap
        self.mp = mp

    def magic_missile(self, target):
        print 'Player casts Magic Missile, dealing 4 damage.'
        self.mp -= 53
        target.hp -= 4


class Boss(object):

    def __init__(self, hp=51, dp=9):
        self.hp = hp
        self.dp = dp

    def attack(self, target):
        damage = self.dp - target.ap
        if damage < 1:
            damage = 1
        target.hp -= damage
        print 'Boss attacks for {} damage!'.format(damage)

battle = Battle(Wizard(), Boss())
while not battle.is_over():
    battle.turn()
