from deck import Deck
from player import Player

class Dealer(Player):

    def __init__(self, shoe):
        self.hand = []
        self.shoe = shoe

    def play(self):
        self.points, self.aces = self.sum_points(self.hand)
        if (self.points < 17 or (self.points == 17 and self.aces)):
            self.hit()

    def hit(self):
        self.hand.append(self.shoe.cards.pop())

    def stand(self):
        pass

if __name__ == "__main__":
    deck = Deck()
    deck.shuffle()
    dealer = Dealer(deck)
    dealer.hit()
    dealer.hit()
    print(dealer.hand)
    print(dealer.sum_points(dealer.hand))
    dealer.play()
    print(dealer.hand)
    print(dealer.sum_points(dealer.hand))

    dealer.hand = []
    dealer.hit()
    dealer.hit()
    print(dealer.hand)
    print(dealer.sum_points(dealer.hand))
    dealer.play()
    print(dealer.hand)
    print(dealer.sum_points(dealer.hand))

    dealer.hand = []
    dealer.hit()
    dealer.hit()
    print(dealer.hand)
    print(dealer.sum_points(dealer.hand))
    dealer.play()
    print(dealer.hand)
    print(dealer.sum_points(dealer.hand))

    dealer.hand = []
    dealer.hit()
    dealer.hit()
    print(dealer.hand)
    print(dealer.sum_points(dealer.hand))
    dealer.play()
    print(dealer.hand)
    print(dealer.sum_points(dealer.hand))
