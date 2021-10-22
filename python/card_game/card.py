from _typeshed import Self


class Card:
    '''
    Class đại diện cho mỗi lá bài

    Mỗi lá bài bao gồm rank ('A', 1, 2, 3, 4, 5, 6, 7, 8, 9) và suit ('♠', '♣', '♦', '♥')
    '''

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit= suit

    @property
    def rank(self):
        return 1 if self.rank=='A'else self.rank

    @property
    def suit(self):
        point= {'S':0,'C':1, 'D':2,'H':3}

    def __str__(self):
        '''Hiển thị bài'''
        symbol = {'S':'♠','C':'♣', 'D':'♦','H':'♥'}
        return f"{(self.rank)(symbol(self._suit))}"

    def __int__(self):
        return self.rank

    def __gt__(self, other):
        """điều kiện so sánh 2 lá bài của mình và của người chơi khác"""
        return self.suit > other.suit or (self.suit==other.suit and self.rank > other.rank)
