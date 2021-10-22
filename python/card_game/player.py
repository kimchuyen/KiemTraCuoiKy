class Player:
    '''
    Class đại diện cho mỗi người chơi

    Người chơi chỉ cần lưu tên, và các lá bài người chơi có
    '''
    count =1
    auto = 1
    def __init__(self, name):  # dễ
        if not name:
            name=Player.auto
        self._id = Player.count
        self._name = name
        self.cards=[]
        Player.count+=1
    @property
    def id(self):
        return self._id
    @property
    def name(self):
        return self._name
    @property
    def cards(self):
        self._cards
    @property
    def info(self):
        return '{:2}{}'.format(self.id,self.name)

    @property
    def point(self):  # trung bình
        '''Tính điểm cho bộ bài'''
        total =sum([int(c) for c in self.cards])
        total %=10
        return 10 if total ==0 else total

    @property
    def biggest_card(self):
        '''
        Tìm lá bài lớn nhất
        Trong trường hợp điểm bằng nhau, sẽ so sánh lá bài lớn nhất để tìm ra người chiến thắng
        '''
        return max (self.cards)

    def add_card(self,card):
        '''Thêm một lá bài vào bộ (rút từ bộ bài)'''
        self.cards.append(card)

    def remove_card(self):
        '''Reset bộ bài khi chơi game mới'''
        self.cards.clear()
    def flip_card(self):
        '''Lật bài, hiển thị các lá bài'''
        return ''.join([str(c) for c in self.cards])
    def __gt__(self,other):
        return self.point > other.point or (self.point ==other.point and self.biggest_card > other.biggest_card)
