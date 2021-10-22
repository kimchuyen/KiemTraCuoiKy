from card import Card
from random import shuffle
class Deck:
    '''
    Class đại diện cho bộ bài, bao gồm 36 lá
    '''
    rank = ['A', 2,3,4,5,6,7,8,9]
    suit = ['S','C','D','H']

    def build(self):
        self.cards = [Card(rank,suit) for rank in Deck.ranks for suit in Deck.suits]    

    def shuffle_card(self):
        '''tráo bài'''
        shuffle(self.cards)

    def deal_card(self):
        '''Rút một lá bài từ bộ bài'''
        if len(self.cards)>0:
            return self.cards.pop()
