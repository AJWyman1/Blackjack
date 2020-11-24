from card import Card
import random

class Deck(object):

    def __init__(self, num_decks = 1):
        self.shoe = [] # Shoe - the box on the table that the cards are placed in and dealt from.

        for _ in range(num_decks):
            for rank in range(1,14):
                for suit in ("♠", "♣", "♡", "♢"):
                    self.shoe.append(Card(rank, suit))

        self.shuffle()

    def __str__(self):
        string = ""
        for card in self.shoe:
            string += str(card) + "\n"
        return string.strip("\n")

    def shuffle(self):
        random.shuffle(self.shoe)

if __name__ == "__main__":
    deck = Deck()
    print(deck)