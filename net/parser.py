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
        self.letters_re = re.compile('[a-zA-z][-a-zA-z\s\'/]+[a-zA-z]')

    # return list of openers where each opener is
    # (cards, coin_split, rating, level)
    # ((string,string), string, string, string)
    def parse(self):
        import os
        script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
        rel_path = "data/openings.txt"
        abs_openings_file_path = os.path.join(script_dir, rel_path)
        openers = []
        with open(abs_openings_file_path) as f:
            openers = [self._parse_line(line) for line in f]
        return openers

    def _parse_line(self, line):
        line = line.rstrip()
        coin_split, line = self._strip_coin_split(line)
        cards, line = self._strip_cards(line)
        rating, line = self._strip_rating(line)
        level, uncertain = self._strip_level(line)
        return (cards, coin_split, rating, level)

    def _strip_coin_split(self, line):
        line_comp = line.split()
        coin_split = line_comp.pop()
        return (coin_split, " ".join(line_comp))

    def _strip_cards(self, line):
        letters = self.letters_re.findall(line)
        cards = letters[0].strip().split("/")
        line = line.replace(letters[0], '')
        return (cards, line)

    def _strip_rating(self, line):
        line_comp = line.split()
        if len(line_comp) < 3:
            return (None, line)
        else:
            rating = line_comp.pop()
            return (rating, ' '.join(line_comp))
    
    def _strip_level(self, line):
        line_comp = line.split()
        if len(line_comp) < 2:
            return (line, None)
        else:
            level, uncertain = line_comp
            return (level, uncertain)
