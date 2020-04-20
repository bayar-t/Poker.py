import itertools, random

class Card(object):
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val

    def show(self):
        print (self.value, "of", self.suit)
    #    "{} of {}".format(self.value, self.suit)

class Deck(object):
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
    #    deck = list(itertools.product(range(1,14), "Spades", ["Clubs", "Diamonds", "Hearts"]))
        for s in ["Spades", "Clubs", "Diamonds", "Hearts"]:
            for v in range(1, 14):
                self.cards.append(Card(s, v))
    def shuffle(self):
        for i in range(len(self.cards)-1, 0, -1):
            rand = random.randint(0, i)
            self.cards[i] = self.cards[rand]
            self.cards[rand] = self.cards[i]

    def show(self):
        for c in self.cards:
            c.show()
    def drawC(self):
        return self.cards.pop()

    def flush(arg1):
        if (len(set(arg1))) != 5:
            return ("This is not a valid poker hand")
        handsuits = set([i[0] for i in arg1])
        if len(handsuits) != 1:
            return False
        handranks = [i[1] for i in arg1]
        #    handranks = transform(handranks)
        sortedranks = sorted(handranks)
        if len(handsuits) == 1:
            if (sortedranks[4]-sortedranks[0]) == 4 or sortedranks == [1, 2, 3, 4, 5] or sortedranks == [1, 10, 11, 12, 13]:
                return False
            else:
                return True
        else:
            return False

    def straight(arg1):
        if (len(set(arg1))) != 5:
            return ("This is not a valid poker hand")
            handsuits = set([i[0] for i in arg1])
            if len(handsuits) == 1:
                return False
                handranks = [i[1] for i in arg1]
    #    handranks = transform(handranks)
        sortedranks = sorted(handranks)
        if 1 == sortedranks[0]:
            return sortedranks == [1, 2, 3, 4, 5] or sortedranks == [1, 10, 11, 12, 13]
        else:
            return (sortedranks[4]-sortedranks[0] == 4) and len(set(sortedranks)) == 5


class Player(object):
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, deck):
        self.hand.append(deck.drawC())
        return self

    def showHand(self):
        for card in self.hand:
            card.show()

    def discard(self):
        return self.hand.pop()

#card = Card("Clubs", 6)
#card.show()
deck = Deck()
deck.shuffle()
#deck.show()
bob = Player("Bob")
bob.draw(deck).draw(deck).draw(deck).draw(deck).draw(deck)
bob.showHand()
#card = Card("Clubs", 6)
#card.show()
suits = ["Spades", "Clubs", "Diamonds", "Hearts"]
ranks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
deck = {(i,j) for i in suits for j in ranks}
num_of_flushes = 0
num_of_straights = 0
#card = deck.drawC()
#card.show()
