from parser import Parser

class OpeningFinder:

    def __init__(self):
        self.parser = Parser()
        self.openings = self.parser.parse()
        
    # given a list of kingdom cards
    # search through available openings and return
    # all valid openings in order of rank
    def findBestOpener(self, cardList):
        cardListSet = set(cardList)
        for opening in self.openings:
            openingSet = set(opening[0])
            if openingSet.issubset(cardListSet):
                return opening
        return None