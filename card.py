class Card(object):
    def __init__(self, **card):
        self.number = card['number']
        self.user = card['user']
        self.balance = card['balance']
        self.provider = card['provider']

    def to_dict(self):
        return {
            'number': self.number,
            'user': self.user,
            'balance': self.balance,
            'provider': self.provider
        }
