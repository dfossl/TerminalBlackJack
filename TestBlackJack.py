import unittest
import Model as M


class TestBlackJack(unittest.TestCase):
    """
    Test script for blackjack model.
    """

    def test_handInsert(self):
        """
        Tests card hand insertion
        :return:
        """
        hand = M.Hand()
        self.assertEqual(0, len(hand.hand))
        hand.insert(M.Card(1, "h"))
        self.assertEqual(1, len(hand.hand))
        hand.insert(M.Card(1, "h"))
        self.assertEqual(2, len(hand.hand))

    def test_handDiscard(self):
        """
        checks if discard empties hand properly
        :return:
        """
        hand = M.Hand()
        hand.insert(M.Card(1, "h"))
        hand.insert(M.Card(1, "h"))
        hand.discard()
        self.assertEqual(0, len(hand.hand))

    def test_handTotal(self):
        """
        tests different hand combinations to ensure
        total function is counting card values correctly
        :return:
        """
        hand = M.Hand()
        four = M.Card(4, "")
        eight = M.Card(8, "")
        ten = M.Card(10, "")
        king = M.Card(13, "")
        queen = M.Card(12, "")
        jack = M.Card(11, "")
        ace = M.Card(1, "")

        # testing non-face cards
        cardList = [four, eight, ten]
        for card in cardList:
            hand.insert(card)
        self.assertEqual(22, hand.total())
        hand.discard()

        # testing if face card get correct value
        cardList = [jack, queen, king]
        for card in cardList:
            hand.insert(card)
        self.assertEqual(30, hand.total())
        hand.discard()

        # Testing if ace will be value 1
        cardList = [ten, ace, eight]
        for card in cardList:
            hand.insert(card)
        self.assertEqual(19, hand.total())
        hand.discard()

        # testing if ace will be value 11
        cardList = [ten, ace]
        for card in cardList:
            hand.insert(card)
        self.assertEqual(21, hand.total())
        hand.discard()

    def test_CardValue(self):
        """
        Checking if card have appropriate values.
        :return:
        """
        self.assertEqual(5, M.Card(5, "").value)
        self.assertEqual(10, M.Card(12, "").value)
        self.assertEqual(11, M.Card(1, "").value)

    def test_DeckFormation(self):
        """
        Ensures that deck that is created has proper number of cards.
        :return:
        """
        deck = M.Deck()
        self.assertEqual(52, len(deck.deck))

    def test_DeckDeal(self):
        """
        ensures that deck is losing cards as it deals
        :return:
        """
        deck = M.Deck()
        deck.dealCard()
        self.assertEqual(51, len(deck.deck))

    def test_PlayerGetCard(self):
        """
        Ensuring that player can get cards from deck.
        :return:
        """
        player = M.Player("test")
        deck = M.Deck()
        self.assertEqual(0, len(player.hand.hand))
        player.getCard(deck)
        self.assertEqual(1, len(player.hand.hand))

    def test_findWinner(self):
        """
        Makes sure that appropriate player is winning
        :return:
        """
        player = M.Player("test")
        dealer = M.Dealer()
        deck = M.Deck()
        player.getCard(deck)
        player.getCard(deck)
        dealer.getCard(deck)
        dealer.getCard(deck)
        self.assertEqual("Dylan Fossl", M.findWinner(player, dealer))
        player.getCard(deck)
        self.assertEqual(player, M.findWinner(player, dealer))
        dealer.getCard(deck)
        dealer.getCard(deck)
        self.assertEqual(dealer, M.findWinner(player, dealer))

    def test_DealerHitDecision(self):
        """
        makes sure dealer is hitting when they should be.
        :return:
        """
        dealer = M.Dealer()
        deck = M.Deck()
        dealer.getCard(deck)
        self.assertEqual(True, dealer.hitDecision())
        dealer.getCard(deck)
        self.assertEqual(False, dealer.hitDecision())


if __name__ == '__main__':
    unittest.main()
