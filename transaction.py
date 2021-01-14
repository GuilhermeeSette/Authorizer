from collections import namedtuple  

Transaction = namedtuple('Transaction', ['merchant', 'amount', 'time'])

def create_transaction(merchant, amount, time):
  return Transaction(merchant, amount, time)