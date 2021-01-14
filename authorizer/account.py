from collections import namedtuple  

Account = namedtuple('Account', ['active_card', 'available_limit'])

def create_account(active_card, available_limit):
  return Account(active_card, available_limit)

