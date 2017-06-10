class Card(object):
    def __init__(self, **card):
        self.number = card['number']
        self.user = card['user']
        self.balance = card['balance']
