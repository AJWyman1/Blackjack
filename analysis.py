from game import Game
from player import Player
from dealer import Dealer
from deck import Deck

import pandas as pd
import numpy as np

make_data = False


def play_round(game):
    game.deal_everyone()
    # game.print_hands()
    winner = game.play_hand()
    hand = {'player_hand':str(game.player.hand).strip("[]").replace(',',''),'dealer_hand':str(game.dealer.hand).strip("[]").replace(',',''),'player_points':game.player.points,'dealer_points':game.dealer.points,'winner':winner}
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


if __name__ == "__main__":
    deck = Deck(num_decks=7, depth=7)
    dealer = Dealer(deck)
    player = Player(play_like_dealer=True)
    game = Game(player, dealer)


    if make_data:
        like_dealer_df = create_blackjack_data(game)
        print(like_dealer_df.head().T)
        like_dealer_df.to_csv('data/dealerbot_7_7.csv')

    df = pd.read_csv('data/dealerbot_7_7.csv')
    print(df.head(17).T)

    winnings = df.player_win.sum() - df.player_lose.sum() + (1.5 * df.blackjack.sum())
    print(winnings)