class Player(object):

    def __init__(self, play_like_dealer=False):
        # self.name = name
        self.hand = []
        self.play_like_dealer = play_like_dealer

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

    def like_dealer(self, dealer):
        self.sum_points()
        if (self.points < 17 or (self.points == 17 and self.aces)):
            self.hand.append(dealer.hit())
            self.like_dealer(dealer)
        self.sum_points()

    def play(self, dealer):
        if self.play_like_dealer:
            self.like_dealer(dealer)