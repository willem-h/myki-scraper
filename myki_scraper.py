import os
from card import Card
from dotenv import load_dotenv, find_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

load_dotenv(find_dotenv())

class MykiScraper(object):
    def __init__(self):
        self.CARD_TABLE_ID = 'ctl00_uxContentPlaceHolder_uxMyCards'
        self.driver = webdriver.PhantomJS()

    def execute(self):
        self._login()
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, self.CARD_TABLE_ID))
            )
            return self._cards()
        finally:
            self.driver.quit()

    def _card(self, row):
        return Card(**{
            'number': row[0].text,
            'user': row[1].text,
            'balance': row[2].text,
            'provider': 'myki'
        })

    def _cards(self):
        return [self._card(card_html) for card_html in self._table()]

    def _row(self, row):
        cells = row.find_elements_by_tag_name('td')
        return [cell for cell in cells]

    def _table(self):
        CARD_TABLE_ID = 'ctl00_uxContentPlaceHolder_uxMyCards'
        table = self.driver.find_elements_by_css_selector("#{} tr".format(CARD_TABLE_ID))
        rows = [self._row(row_html) for row_html in table]
        rows.pop(0)
        return rows

    def _login(self):
        LOGIN_BUTTON_ID = 'ctl00_uxContentPlaceHolder_uxLogin'
        LOGIN_URL = 'https://www.mymyki.com.au/NTSWebPortal/login.aspx'
        PASSWORD_INPUT_ID = 'ctl00_uxContentPlaceHolder_uxPassword'
        USERNAME_INPUT_ID = 'ctl00_uxContentPlaceHolder_uxUsername'
        self.driver.get(LOGIN_URL)
        username_field = self.driver.find_element_by_id(USERNAME_INPUT_ID)
        password_field = self.driver.find_element_by_id(PASSWORD_INPUT_ID)
        login_button = self.driver.find_element_by_id(LOGIN_BUTTON_ID)
        username_field.send_keys(os.environ['MYKI_USERNAME'])
        password_field.send_keys(os.environ['MYKI_PASSWORD'])
        login_button.click()
