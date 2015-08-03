import re
dataFile = 'openingsList.txt'

# ['8.393', '\xc2\xb1', '0.953', '1', 'Mountebank', '/', 'Chapel', '5/2']

'''
Parse openingsList.txt using cascade method.
At each level, strip out one piece of information and
pass the remaining string along.
'''

class Parser:

    def __init__(self):
        self.lettersRe = re.compile('[a-zA-z][-a-zA-z\s\'/]+[a-zA-z]')

    # return list of openers where each opener is
    # (cards, coinSplit, rating, level)
    # (tuple, string, )
    def parse(self):
        letterRe = re.compile("\D+^.")
        dataFile = "openings.txt"
        openers = []
        with open(dataFile) as f:
            openers = [self._parseLine(line) for line in f]
        return openers

    def _parseLine(self, line):
        line = line.rstrip()
        coinSplit, line = self._stripCoinSplit(line)
        cards, line = self._stripCards(line)
        rating, line = self._stripRating(line)
        level, uncertain = self._stripLevel(line)
        return (cards, coinSplit, rating, level)

    def _stripCoinSplit(self, line):
        lineComp = line.split()
        coinSplit = lineComp.pop()
        return (coinSplit, " ".join(lineComp))

    def _stripCards(self, line):
        letters = self.lettersRe.findall(line)
        cards = letters[0].strip().split("/")
        line = line.replace(letters[0], '')
        return (cards, line)

    def _stripRating(self, line):
        lineComp = line.split()
        if len(lineComp) < 3:
            return (None, line)
        else:
            rating = lineComp.pop()
            return (rating, ' '.join(lineComp))
    
    def _stripLevel(self, line):
        lineComp = line.split()
        if len(lineComp) < 2:
            return (line, None)
        else:
            level, uncertain = lineComp
            return (level, uncertain)
