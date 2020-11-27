class Player(object):

    def __init__(self):
        # self.name = name
        self.hand = []

    def sum_points(self):
        self.points = 0
        self.aces = 0

        for card in self.hand:
            self.points += card.points
            if card.rank == 1:
                self.aces += 1

        while self.points > 21 and self.aces:
            self.points -= 10
            self.aces -= 1

        return self.points, self.aces

    def play_like_dealer(self, dealer):
        self.sum_points()
        if (self.points < 17 or (self.points == 17 and self.aces)):
            self.hand.append(dealer.hit())
            self.play_like_dealer(dealer)
        self.sum_points()