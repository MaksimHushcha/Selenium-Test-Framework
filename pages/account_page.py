from base_page import BasePage
from locators import account_page_locators as loc
from dotenv import load_dotenv

load_dotenv()

class LoginPage(BasePage):

    endpoint = "account"