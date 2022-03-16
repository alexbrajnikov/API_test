import pprint

from config import *
from td.client import TDClient

td_client = TDClient(client_id=consumer_key, redirect_uri=redirect_url, credentials_path=json_path)

td_sesion = td_client.login()
quotes_responce = td_client.get_quotes(instruments=["MSFT", "AAPL","SQ"])
pprint.pprint(quotes_responce)
orders_positions = td_client.get_accounts(account='all',fields=['positions','orders'])
pprint.pprint(orders_positions)