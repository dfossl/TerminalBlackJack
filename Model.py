import random
"""
Module that holds all the classes and functions for the Model.
this includes a Card class, a Deck Class, a Player class and a dealer class.
"""

faceRankToLetter = {11: "J", 12: "Q", 13: "K", 1: "A"}
class Card:
    """
    Cards are represented by holding three values a rank, a value and a suit.
    """

    def __init__(self, rank, suit):
        """
        constructs a card of provided rank and suit.
        :param rank:
        :param suit:
        """
        self.rank = rank
        if rank > 10:
            self.value = 10
        elif rank == 1:
            self.value = 11
        else:
            self.value = rank
        self.suit = suit

    def __str__(self):
        if self.rank > 10 or self.rank == 1:
            return f'[{faceRankToLetter[self.rank]} {self.suit}]'
        else:
            return f'[{self.rank} {self.suit}]'

    def __repr__(self):
        return str(self)


suits = ["♥", "♣", "♠", "♦"]
class Deck:
    """
    A deck holds a list that hold 52 cards.
    The deck is generated such that eah card has a unique value, rank and suit set.
    """

    def __init__(self):
        """
        Constructs new deck of card.
        """
        self.remake()

    def __str__(self):
        return str(self.deck)

    def __repr__(self):
        return str(self)

    def shuffle(self):
        """
        Shuffles deck
        :return:
        """
        random.shuffle(self.deck)

    def dealCard(self):
        """
        removes card from top of deck
        :return:
        """
        return self.deck.pop()

    def remake(self):
        """
        Makes a new deck of cards
        :return:
        """
        self.deck = []
        for suit in suits:
            for i in range(1, 14):
                self.deck.append(Card(i, suit))


class Hand():
    """
    Hand class essentiall a list of cards.
    """

    def __init__(self):
        self.hand = []

    def __str__(self):
        return(str(self.hand))

    def __iter__(self):
        return iter(self.hand)

    def insert(self, card):
        self.hand.append(card)

    """
    Most important hand method
    holds the logic for totaling a hand which will
    choose the value of an Ace to be 11 or 1 when appropriate.
    """
    def total(self):
        aceCtr = 0
        total = 0
        for card in self.hand:
            if card.rank == 1:
                aceCtr += 1
            total += card.value

        for i in range(0, aceCtr):
            if total <= 21:
                break
            total = total - 10

        return total


    def discard(self):
        """
        creates an empty hand.
        :return:
        """
        self.hand = []


# Player is a simple class that just has a hand and a isBust value.
class Player():
    """
    Player is a simple class that just has a hand, name and an isBust value.
    """

    def __init__(self, name):
        self.name = name
        self.isBust = False
        self.hand = Hand()

    def getCard(self, deck):
        """
        Recieves card from deck.
        :param deck:
        :return:
        """
        self.hand.insert(deck.dealCard())

# Dealer inhereits from Player and has an additional method for determining if it should hit or not.
class Dealer(Player):
    """
    Dealer inhereits from Player and has an additional method for
    determining if it should hit or not.
    """

    def __init__(self):
        self.name = "Dealer"
        self.isBust = False
        self.hand = Hand()

    def hitDecision(self):
        """
        Per blackjack rules hit on all values less then 17
        :return:
        """
        if self.hand.total() >= 17:
            return False
        else:
            return True

def findWinner(Player, Dealer):
    """
    Given two players returns the winner.
    If a tie I win :)
    :param Player:
    :param Dealer:
    :return:
    """
    if Player.hand.total() > Dealer.hand.total():
        return Player
    elif Player.hand.total() == Dealer.hand.total():
        return "Dylan Fossl"
    else:
        return Dealer
