import Model as M
import View as V
"""
Module that contains all the the necessary classes and methods
for the BlackJack Controller
"""

def preGameInfo():
    """
    Gets User input for if they want to play a game and if they want to play music,
    then constructs and returns a game object.
    :return:
    """
    V.clearTerminal()
    yes = V.askYesNo("Would you like to play blackjack?")
    if yes:
        music = V.askYesNo("Would you like music?")
        name = V.askForName()
        return Game(name, music)


class Game():
    """
    Class that holds model objects and connects the view to them.
    holds the layout of the black jack game.
    """

    def __init__(self, name, music):
        """
        Contrsucts a player, dealer and deck.
        :param name:
        :param music:
        """
        if music:
            V.playMusic()
        self.dealer = M.Dealer()
        self.player = M.Player(name)
        self.deck = M.Deck()

    def playGame(self):
        """
        Plays through game logic using model objects and getting input from View
        :return:
        """
        # while loop breaks once a winner is determined for the round
        while True:
            V.clearTerminal()

            self.dealer.isBust = False
            self.player.isBust = False

            # Gets Empties hand
            self.player.hand.discard()
            self.dealer.hand.discard()

            # makes new deck and shuffles
            self.deck.remake()
            self.deck.shuffle()

            # print(self.deck)

            # alternating deals cards to dealer and player.
            self.dealer.getCard(self.deck)
            self.player.getCard(self.deck)
            self.dealer.getCard(self.deck)
            self.player.getCard(self.deck)

            # print(self.player.name)
            # print(self.player.hand)

            V.printTable(self.dealer, self.player, False)

            # return

            # goes through player's deisions on hiting or standing and checks for bust.
            self.playHand(self.player, False)
            if self.player.isBust:
                # V.printTotals(self.player, self.dealer)
                V.clearTerminal()
                V.printTable(self.dealer, self.player, True)
                V.printVictory(self.dealer)
                break

            V.printTable(self.dealer, self.player, True)

            # Goes through dealers decisions on hiting and standing and checks for bust.
            self.playHand(self.dealer, True)
            if self.dealer.isBust:
                # V.printTotals(self.player, self.dealer)
                V.clearTerminal()
                V.printTable(self.dealer, self.player, True)
                V.printVictory(self.player)
                break

            # print("Finding Winner")
            # V.printTotals(self.player, self.dealer)
            # V.clearTerminal()
            V.printTable(self.dealer, self.player, True)
            V.printVictory(M.findWinner(self.player, self.dealer))
            break

        # Checks if player wishes to play another hand.
        yes = V.askYesNo("Would you like to play another hand?")
        if yes:
            self.playGame()

    def playHand(self, Player1, showDealer):
        """
        Goest though the hit and stand layout getting decision from current player.
        :param Player1:
        :param showDealer:
        :return:
        """
        hit = True
        while hit:
            if Player1.hand.total() <= 21:
                hit = V.getHitChoice(Player1)
                V.clearTerminal()
            else:
                Player1.isBust = True
                V.clearTerminal()
                V.printTable(self.dealer, self.player, True)
                V.printBusted(Player1)
                break
            if hit:
                # print("Dealer hit")
                Player1.getCard(self.deck)
                V.printTable(self.dealer, self.player, showDealer)
