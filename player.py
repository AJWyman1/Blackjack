class Player(object):

    def __init__(self, play_like_dealer=False, basic_strategy=False):
        # self.name = name
        self.hand = []
        self.play_like_dealer = play_like_dealer
        self.basic_strategy = basic_strategy
        self.double = False
        self.split = False

        if self.basic_strategy:

            self.b_hard_strategy ={    #    8,        9,       10,       11,      12,      13,      14,      15,      16,     17
                                    11:['hit',    'hit',    'hit', 'double',   'hit',   'hit',   'hit',   'hit',   'hit', 'stand'],
                                    10:['hit',    'hit',    'hit', 'double',   'hit',   'hit',   'hit',   'hit',   'hit', 'stand'],
                                    9: ['hit',    'hit', 'double', 'double',   'hit',   'hit',   'hit',   'hit',   'hit', 'stand'],
                                    8: ['hit',    'hit', 'double', 'double',   'hit',   'hit',   'hit',   'hit',   'hit', 'stand'],
                                    7: ['hit',    'hit', 'double', 'double',   'hit',   'hit',   'hit',   'hit',   'hit', 'stand'],
                                    6: ['hit', 'double', 'double', 'double', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand'],
                                    5: ['hit', 'double', 'double', 'double', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand'],
                                    4: ['hit', 'double', 'double', 'double', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand'],
                                    3: ['hit', 'double', 'double', 'double',   'hit', 'stand', 'stand', 'stand', 'stand', 'stand'],
                                    2: ['hit',    'hit', 'double', 'double',   'hit', 'stand', 'stand', 'stand', 'stand', 'stand']
                }

            self.b_soft_strategy = {  #       A2,       A3,       A4,       A5,       A6,       A7,       A8,     A9
                                    11:[   'hit',    'hit',    'hit',    'hit',    'hit',    'hit',  'stand', 'stand'],
                                    10:[   'hit',    'hit',    'hit',    'hit',    'hit',    'hit',  'stand', 'stand'],
                                    9: [   'hit',    'hit',    'hit',    'hit',    'hit',    'hit',  'stand', 'stand'],
                                    8: [   'hit',    'hit',    'hit',    'hit',    'hit',  'stand',  'stand', 'stand'],
                                    7: [   'hit',    'hit',    'hit',    'hit',    'hit',  'stand',  'stand', 'stand'],
                                    6: ['double', 'double', 'double', 'double', 'double', 'double', 'double', 'stand'],
                                    5: ['double', 'double', 'double', 'double', 'double', 'double',  'stand', 'stand'],
                                    4: [   'hit',    'hit', 'double', 'double', 'double', 'double',  'stand', 'stand'],
                                    3: [   'hit',    'hit',    'hit',    'hit', 'double', 'double',  'stand', 'stand'],
                                    2: [   'hit',    'hit',    'hit',    'hit',    'hit', 'double',  'stand', 'stand']
                        }

            self.b_pair_strategy = {  #      22,      33,      44,  55,      66,      77,      88,      99,  TT,     AA
                                    11:[    'n',     'n',     'n', 'n',     'n',     'n', 'split',     'n', 'n', 'split'],
                                    10:[    'n',     'n',     'n', 'n',     'n',     'n', 'split',     'n', 'n', 'split'],
                                    9: [    'n',     'n',     'n', 'n',     'n',     'n', 'split', 'split', 'n', 'split'],
                                    8: [    'n',     'n',     'n', 'n',     'n',     'n', 'split', 'split', 'n', 'split'],
                                    7: ['split', 'split',     'n', 'n',     'n', 'split', 'split',     'n', 'n', 'split'],
                                    6: ['split', 'split', 'split', 'n', 'split', 'split', 'split', 'split', 'n', 'split'],
                                    5: ['split', 'split', 'split', 'n', 'split', 'split', 'split', 'split', 'n', 'split'],
                                    4: ['split', 'split',     'n', 'n', 'split', 'split', 'split', 'split', 'n', 'split'],
                                    3: ['split', 'split',     'n', 'n', 'split', 'split', 'split', 'split', 'n', 'split'],
                                    2: ['split', 'split',     'n', 'n', 'split', 'split', 'split', 'split', 'n', 'split']
                        }
        

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


    def play(self, dealer):
        self.initial_cards = self.get_initial_cards()
        if self.play_like_dealer:
            if len(self.hand) == 2:
                self.initial_points, _ = self.sum_points()
            self.like_dealer(dealer)
        elif self.basic_strategy:
            if len(self.hand) == 2:
                self.initial_points, _ = self.sum_points()
            self.basic_strat(dealer)


    def get_initial_cards(self):
        return self.hand[:2]


    def like_dealer(self, dealer):
        self.sum_points()
        if (self.points < 17 or (self.points == 17 and self.aces)):
            self.hand.append(dealer.hit())
            self.like_dealer(dealer)
        self.sum_points()


    def get_hand_type(self):
        if self.hand[0] == self.hand[1]:
            self.hand_type = 'pair'
        elif self.aces:
            self.hand_type = 'soft'
        else:
            self.hand_type = 'hard'


    def basic_strat(self, dealer):
        up = dealer.up_card().points #get dealer visible points
        self.sum_points() # update point total and aces
        
        if len(self.hand) == 2:
            self.get_hand_type()
        else: self.hand_type = 'hard'

        if self.hand_type == 'pair':
            move = self.b_pair_strategy[up][self.hand[0].points - 2]
            if move == 'n':
                self.hand_type = 'hard'
        elif self.hand_type == 'soft':
            move = self.b_soft_strategy[up][self.points - 13]
        if self.hand_type == 'hard':
            if self.points < 8:
                move = 'hit'
            elif self.points > 17:
                move = 'stand'
            else:
                move = self.b_hard_strategy[up][self.points - 8]

        print(move)
        if move == 'hit':
            self.hand.append(dealer.hit())
            self.basic_strat(dealer)
        elif move == 'double':
            self.double = True
            self.hand.append(dealer.hit())
        elif move == 'split':
            self.split = True
        self.sum_points()

    def split_hands(self, dealer):
        hand_0, hand_1 = [self.hand[0]], [self.hand[1]]
        hand_0.append(dealer.hit())
        hand_1.append(dealer.hit())
        self.hand = hand_0
        self.basic_strat(dealer)
        hand_0 = self.hand

        self.hand = hand_1
        self.basic_strat(dealer)
        
        
