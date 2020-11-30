from deck import Deck
from player import Player

class Dealer(Player):

    def __init__(self, shoe):
        self.hand = []
        shoe.shuffle()
        self.shoe = shoe

    def play(self):
        self.sum_points()
        if (self.points < 17 or (self.points == 17 and self.aces)):
            self.hand.append(self.hit())
            self.play()
        else:
            self.stand()

    def hit(self):
        return self.shoe.deal()

    def stand(self):
        if self.shoe.check_shuffle():
            #future home of card counter's count reset
            pass
            
    def deal(self):
        return [self.shoe.deal(), self.shoe.deal()]

    def up_card(self):
        return self.hand[0]


def play_hand(dealer):
    dealer.hand = dealer.deal()
    dealer.play()
    print(dealer.hand)
    print(dealer.sum_points())

if __name__ == "__main__":
    deck = Deck()
    deck.shuffle()
    dealer = Dealer(deck)

    for _ in range(30):
        play_hand(dealer)