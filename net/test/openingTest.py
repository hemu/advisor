import unittest
from opening import OpeningFinder

class TestOpeningFinder(unittest.TestCase):

    def test_top_ten_openings(self):
        topFiveOpenings = [["Mountebank", "Chapel"], \
                           ["Tournament", "Ambassador"], \
                           ["Mint", "Fool's Gold"], \
                           ["Witch", "Chapel"], \
                           ["Tournament", "Chapel"], \
                           ["Caravan", "Ambassador"], \
                           ["Upgrade", "Chapel"], \
                           ["Mountebank", "Hamlet"], \
                           ["Tournament", "Masquerade"], \
                           ["Hunting Party", "Chapel"], \
                           ["Vault", "Chapel"]]
        allTopOpeningCards = []
        [allTopOpeningCards.extend(a) for a in topFiveOpenings]

        for topOpening in topFiveOpenings:
            kingdomGenerator = KingdomGenerator()
            openingFinder = OpeningFinder()
            kingdomCards = kingdomGenerator.getCards(10, topOpening, allTopOpeningCards)
            opener = openingFinder.findBestOpener(kingdomCards)
            print ""
            print kingdomCards
            print opener
            print ""
            self.assertTrue(opener)
            self.assertItemsEqual(opener[0][0], topOpening)

  # def test_isupper(self):
  #     self.assertTrue('FOO'.isupper())
  #     self.assertFalse('Foo'.isupper())

  # def test_split(self):
  #     s = 'hello world'
  #     self.assertEqual(s.split(), ['hello', 'world'])
  #     # check that s.split fails when the separator is not a string
  #     with self.assertRaises(TypeError):
  #         s.split(2)

class KingdomGenerator:

    def __init__(self):
        cardListFile = "data/cardList.txt"
        with open(cardListFile) as f:
            self.cards = [l.strip() for l in f]
            import random
            random.shuffle(self.cards)

    def getCards(self, count, requiredCards, excludeCards):
        numExtra = count - len(requiredCards)
        kingdomCards = []
        numAdded = 0
        for card in self.cards:
            if card not in requiredCards and card not in excludeCards:
                kingdomCards.append(card)
                numAdded += 1
                if numAdded >= numExtra:
                    break
        kingdomCards.extend(requiredCards)
        kingdomCards.extend(["Silver", "Estate"])
        return kingdomCards

if __name__ == '__main__':
    unittest.main()