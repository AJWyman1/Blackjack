from card import Card
import random


class Deck(object):

    def __init__(self, num_decks = 1):
        self.cards = [] 
        for _ in range(num_decks):
            for rank in range(1,14):
                for suit in ("♠", "♣", "♡", "♢"):
                    self.cards.append(Card(rank, suit))


    def __str__(self):
        string = ""
        for card in self.cards:
            string += str(card) + "\n"
        return string.strip("\n")

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()

if __name__ == "__main__":

    deck = Deck()
    deck.shuffle()
    print(deck)
    deck.shuffle()
    print(deck)