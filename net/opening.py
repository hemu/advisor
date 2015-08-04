from parser import Parser

class OpeningFinder:

    def __init__(self):
        self.parser = Parser()
        self.openings = self.parser.parse()
        
    # given a list of kingdom cards
    # search through available openings and return
    # all valid openings in order of rank
    def find_top_openings(self, cardList):
        card_list_set = set(cardList)
        best_openings = []
        for opening in self.openings:
            opening_set = set(opening[0])
            if opening_set.issubset(card_list_set):
                best_openings.append(opening)
        return best_openings