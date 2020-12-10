class Card(object):

    def __init__(self, rank, suit):
        self.suit = suit
        self.rank = rank

        if self.suit in ["♠", "♣"]:
            self.color = 'black'
        else:
            self.color = 'red'

        #Points for blackjack
        if rank > 10:
            self.points = 10
        elif rank == 1:
            self.points = 11
        else:
            self.points = rank

    def __repr__(self):
        cards = {num : str(num) for num in range(2,11)}
        cards.update({11: 'J', 12: 'Q', 13: 'K', 1: 'A'})

        return f'{self.suit}{cards[self.rank]}'

    def __add__(self, other):
        return self.points + other.points

    def __eq__(self, other):
        return self.points == other.points

if __name__ == "__main__":
    ace_of_spades = Card(1, '♠')
    ten_of_diamonds = Card(10, '♢')

    print(ace_of_spades)
    print(ten_of_diamonds)

    lst = [ace_of_spades, ten_of_diamonds]

    print(ace_of_spades + ten_of_diamonds)

    print(ace_of_spades == ten_of_diamonds)

