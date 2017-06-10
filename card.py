class Card(object):
    def __init__(self, **card):
        self.number = card['number']
        self.holder = card['holder']
        self.value = card['value']
