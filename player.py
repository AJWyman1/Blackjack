class Player(object):

    def __init__(self):
        # self.name = name
        self.hand = []

    def sum_points(self, hand):
        points = 0
        aces = 0

        for card in hand:
            points += card.points
            if card.rank == 1:
                aces += 1

        while points > 21 and aces:
            points -= 10
            aces -= 1

        return points, aces