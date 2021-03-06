from card import Card
from random import shuffle


class Deck(object):

    def __init__(self, num_decks = 1 , depth = 7):
        self.cards = [] 
        self.num_decks = num_decks
        for _ in range(self.num_decks):
            for rank in range(1,14):
                for suit in ("♠", "♣", "♡", "♢"):
                    self.cards.append(Card(rank, suit))
        self.depth = depth

    def __str__(self):
        string = ""
        for card in self.cards:
            string += str(card) + "\n"
        return string.strip("\n")

    def shuffle(self):
        shuffle(self.cards)

    def deal(self):
        return self.cards.pop()

    def check_shuffle(self):
        if len(self.cards) < (self.num_decks * 52 / self.depth):
            self.__init__(num_decks=self.num_decks, depth=self.depth)
            self.shuffle()
            print('Shuffled')
            return True

if __name__ == "__main__":

    deck = Deck()
    deck.shuffle()
    print(deck)
    deck.shuffle()
    print(deck)