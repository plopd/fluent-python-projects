"""
    Source: “Fluent Python by Luciano Ramalho (O’Reilly). Copyright 2015 Luciano Ramalho, 978-1-491-94600-8.”
"""
import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

if __name__ == "__main__":
    beer_card = Card('7', 'diamonds')
    print(beer_card) # Card(rank='7', suit='diamonds')

    deck = FrenchDeck()
    print(len(deck)) # 52

    print(deck[0]) # Card(rank='2', suit='spades')
    
    print(deck[-1]) # Card(rank='A', suit='hearts')

    import random
    random.seed(0)

    print(random.choice(deck)) # Card(rank='K', suit='diamonds')
    print(random.choice(deck)) # Card(rank='J', suit='hearts')
    print(random.choice(deck)) # Card(rank='2', suit='clubs')

    print(deck[:3]) # [Card(rank='2', suit='spades'), Card(rank='3', suit='spades'), Card(rank='4', suit='spades')]

    print(deck[12::13]) # [Card(rank='A', suit='spades'), Card(rank='A', suit='diamonds'), Card(rank='A', suit='clubs'), Card(rank='A', suit='hearts')]
    # Prints all the cards in the deck.
    for card in deck:
        print(card)

    # Prints the deck reversed.
    for card in reversed(deck):
        print(card)

    print(Card('Q', 'hearts') in deck) # True

    print(Card('7', 'beasts') in deck) # False

    suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

    def spades_high(card):
        rank_value = FrenchDeck.ranks.index(card.rank)
        return rank_value * len(suit_values) + suit_values[card.suit]

    # List the deck in order of increasing rank
    for card in sorted(deck, key=spades_high):
        print(card)
