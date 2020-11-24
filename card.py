class Card(object):

    def __init__(self, rank, suit):
        self.suit = suit
        self.rank = rank

    def __repr__(self):
        cards = {num : str(num) for num in range(2,11)}
        cards.update({11: 'J', 12: 'Q', 13: 'K', 1: 'A'})

        return f'{self.suit}{cards[self.rank]}'

if __name__ == "__main__":
    ace_of_spades = Card(1, '♠')
    ten_of_diamonds = Card(13, '♢')

    print(ace_of_spades)
    print(ten_of_diamonds)