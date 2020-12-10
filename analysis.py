from game import Game
from player import Player
from dealer import Dealer
from deck import Deck

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

make_data = False


def play_round(game):
    game.deal_everyone()
    # game.print_hands()
    winner, double = game.play_hand()
    hand = {'player_hand':str(game.player.hand).strip("[]").replace(',',''), 
            'dealer_hand':str(game.dealer.hand).strip("[]").replace(',',''), 
            'player_inital':str(game.player.initial_cards()).strip("[]").replace(',',''),
            'dealer_upcard':str(game.dealer.up_card()).strip("[]").replace(',',''), 
            'player_initial_points':game.player.initial_points,
            'dealer_initial_points':game.dealer.up_card().points,
            'player_points':game.player.points, 
            'dealer_points':game.dealer.points, 
            'winner':winner,
            'double':double}
    return hand

def analyze_game(df):
    df['player_busted'] = df.apply(lambda row: 1 if row['player_points'] > 21 else 0, axis=1)
    df['dealer_busted'] = df.apply(lambda row: 1 if row['dealer_points'] > 21 else 0, axis=1)
    df['player_win'] = df.apply(lambda row: 1 if row['winner'] == 'Player' or row['winner'] == 'Blackjack' else 0, axis=1)
    df['player_lose'] = df.apply(lambda row: 1 if row['winner'] == 'Dealer' else 0, axis=1)
    df['blackjack'] = df.apply(lambda row: 1 if row['winner'] == 'Blackjack' else 0, axis=1)

    return df

def create_blackjack_data(game):
    df = pd.DataFrame(data=play_round(game), index=[0])

    for _ in range(10000):
        df2 = pd.DataFrame(data=play_round(game), index=[0])
        df = df.append(df2, ignore_index=True)

    df = analyze_game(df)
    return df

def busted_per_starting_points(df):

    s = df.player_busted.groupby(df.player_initial_points).sum().reset_index()
    print(s)
    fig, ax = plt.subplots()

    ax.bar(s.player_initial_points, s.player_busted)
    ax.set_xticks(s.player_initial_points)
    ax.set_xlabel('Player Starting Points')
    ax.set_ylabel('Number of Busted Hands')
    ax.set_title('Times Player Busted for Each Starting Total')
    plt.show()

def wins_per_upcard(df):

    s = df.player_win.groupby(df.dealer_initial_points).sum().reset_index()
    print(s)
    fig, ax = plt.subplots()

    ax.bar(s.dealer_initial_points, s.player_win)
    ax.set_xticks(s.dealer_initial_points)
    ax.set_xlabel('Dealer Upcard')
    ax.set_ylabel('Number of Victories')
    ax.set_title('Times Player Won for Each Dealer Upcard')
    plt.show()

if __name__ == "__main__":

    if make_data:

        deck = Deck(num_decks=7, depth=7)
        dealer = Dealer(deck)
        player = Player(play_like_dealer=True)
        game = Game(player, dealer)

        like_dealer_df = create_blackjack_data(game)
        like_dealer_df.to_csv('data/dealerbot_7_7.csv')

    df = pd.read_csv('data/dealerbot_7_7.csv')
    print(df.head(15).T)

    winnings = df.player_win.sum() - df.player_lose.sum() + (1.5 * df.blackjack.sum())
    print(winnings)
    print(df.dealer_busted.sum())
    print(df.player_busted.sum())

    # ax = df.player_initial_points.value_counts().plot(kind='bar')

    busted_per_starting_points(df)
    wins_per_upcard(df)