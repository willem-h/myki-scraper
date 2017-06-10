import os
import requests
from bs4 import BeautifulSoup
from card import Card
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

class GoCardScraper(object):
    def __init__(self):
        self.session = requests.Session()
        login_data = {
            'cardNum': os.environ['GOCARD_USERNAME'],
            'pass': os.environ['GOCARD_PASSWORD'],
            'cardOps': 'Display'
        }
        login_url = 'https://gocard.translink.com.au/webtix/welcome/welcome.do'
        self.content = self.session.post(login_url, login_data, verify=True).text

    def execute(self):
        return Card(**{
            'number': self._get_card_number(),
            'user': self._get_user(),
            'balance': self._get_balance()
        })

    def _get_balance(self):
        soup = BeautifulSoup(self.content, 'html5lib')
        table = soup.find('table', { 'id': 'balance-table' })
        return table.find_all('td')[1].text

    def _get_card_number(self):
        return os.environ['GOCARD_USERNAME']

    def _get_user(self):
        content = self.session.get('https://gocard.translink.com.au/webtix/tickets-and-fares/go-card/online/details').content
        soup = BeautifulSoup(content, 'html5lib')
        name = soup.find('span', { 'id': 'full-name' }).text
        return ' '.join(name.split())
