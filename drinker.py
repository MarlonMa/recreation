#!/usr/bin/env python
"""Program to calculate how many bottles of wine the drinkers with specified amount of money can drink.
==========
Conditions: 
1 bottle of wine is worth 2 yuan
2 bottles can exchange for 1 bottle of wine
4 caps can exchange for 1 bottle of wine
==========
"""

class Drinker:

    def __init__(self, money):
        self.property = money
        self.money = money
        self.drunk = 0
        self.bottle = 0
        self.cap = 0

    def exchange_wine(self):
        exchangeable = 0
        if self.money >= 2:
            e1, self.money = divmod(self.money, 2)
            exchangeable += e1
        if self.bottle >= 2:
            e2, self.bottle = divmod(self.bottle, 2)
            exchangeable += e2
        elif self.cap >= 4:
            e3, self.cap = divmod(self.cap, 4)
            exchangeable += e3
        self.drunk += exchangeable
        self.bottle += exchangeable
        self.cap += exchangeable


def drink_wine(drinker):
    while True:
        if drinker.money >= 2 or drinker.bottle >= 2 or drinker.cap >= 4:
            drinker.exchange_wine()
        else:
            print("%s yuan can drink %s %s of wine" % (drinker.property,
                                                       drinker.drunk, 'bottles' if drinker.drunk > 1 else 'bottle'))
            break

if __name__ == '__main__':
    drinker1 = Drinker(10)
    drinker2 = Drinker(10 ** 5)
    drinker3 = Drinker(10 ** 8)
    for drinker in [drinker1, drinker2, drinker3]:
        drink_wine(drinker)