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
bob.draw(deck).draw(deck)
bob.showHand()


#card = deck.drawC()
#card.show()
