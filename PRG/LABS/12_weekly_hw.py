class Card:
 
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.dict_card = {"J":"jack",
        "Q": "queen",
        "K": "king",
        "A": "ace",
        "C": "clubs", 
        "D": "diamonds", 
        "H": "hearts", 
        "S": "spades"}
        self.ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
        self.suits = ["C", "D", "H", "S"]

    
 
 
    def __str__(self):
        if type(self.rank) == int:
            ranked = self.rank
        elif type(self.rank) == str:
            ranked = self.dict_card[self.rank]
        suited = self.dict_card[self.suit]
        return "Card: {} of {}".format(ranked, suited) 

 
 
    def __repr__(self):
        return str(self)
 
    def __eq__(self, other):
        return self.rank == other.rank and self.suit == other.suit    
 
    def __lt__(self, other):
        if self.rank != other.rank:
            index_1 = self.ranks.index(self.rank)
            index_2 = self.ranks.index(other.rank)
            return index_1 < index_2
        else:
            index_1 = self.suits.index(self.suit)
            index_2 = self.suits.index(other.suit)
            return index_1 < index_2



 
 
if __name__ == "__main__":
    cards = []
    cards.append(Card('A', 'D'))
    cards.append(Card(10, 'S'))
    cards.append(Card('K', 'H'))
    cards.append(Card('A', 'C'))
    cards.append(Card(3, 'S'))
    cards.append(Card(3, 'D'))
 
 
    print(cards)
    cards.sort()
 
    print(cards)
 
    