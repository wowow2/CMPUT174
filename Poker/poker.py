SUITS = {"spades":"♠", "hearts":"♥", "clubs":"♣", "diamonds":"♦"}
import random
class Card:
    def __init__(self, suit, rank):
        assert suit in {"spades", "hearts", "clubs", "diamonds"}
        assert rank in range(2,15)
        self._rank = rank
        self._suit = suit

    def __repr__(self):
        return f"{self._rank} {self._suit}"
    def suitString(self):
        return SUITS[self._suit]
    def rankString(self):
        if self._rank < 10:
            return f"{self._rank}"
        rankDict = {10: "X", 11: "J", 12: "Q", 13: "K", 14: "A"}
        return rankDict[self._rank]
    def __str__(self):
        '''
        +---+
        + R +
        + S +
        +---+
        '''
        s = "+---+\n"
        s+= f"{self._rank}\n"
        s+= f"{self._suits}\n"
        s+= '+---+'
        return s
class Hand:
    def __init__(self, cards):
        assert len(cards) == 5
        self._cards = cards
    def __repr__(self):
        return str(self._cards)
    def __str__(self):
        borderString = "+---+---+---+---+---+"
        resultString = borderString + '\n'
        rankList = []
        suitList = []
        for card in self._cards:
            rankList.append(card.rankString())
            suitList.append(card.suitString())
        resultString += "+" + "+ ".join(rankList) + "+" + "+".join(rankList) + "+\n"
        resultString += "+" + "+ ".join(rankList) + "+" + "+".join(suitList) + "+\n"
        resultString += borderString
        return resultString
    def checkStaight(self):
        rankList = []
        for card in self._cards:
            rankList.append(card._rank)
        rankList.sort()
        prevNumber = rankList[0]
        for num in rankList[1:]:
            if num != prevNumber + 1:
                return False
            prevNumber = num
        return True
class Deck:
    def __init__(self):
        suits = ('hearts', 'spades', 'diamonds','clubs')
        self._cards = []
        for suit in suits:
            for rank in range(2,15):
                card = Card(rank, suit)
                self._cards.append(card)
    def __repr__(self):
        return str(self._cards)
    def __str__(self):
        return f'Deck has {len(self._cards)} cards left'
    def drawCard(self):
        assert len(self._cards) > 0
        x = random.randint(0,len(self._cards)-1)
        return self._cards.pop(x)
    def drawHand(self):
        assert len(self._cards) >= 5
        loc = []
        for i in range(5):
            loc.append(self.drawCard())
        return Hand(loc)



