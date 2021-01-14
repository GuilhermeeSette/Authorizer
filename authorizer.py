from account import create_account
from transaction import create_transaction
from datetime import datetime

transactions = []
accounts = []

def add_violation(violation, violation_type):
  if violation_type == "transaction":
    transaction_violations.append(violation)
  elif violation_type == "account":
    account_violations.append(violation)

def sum_transactions_ammount(transactions):
  if len(transactions) == 0:
      return 0
  return transactions[0].amount + sum_transactions_ammount(transactions[1:])

def subtract_time(string_time_a, string_time_b):
  time_a = datetime.fromisoformat(string_time_a[:-1])
  time_b = datetime.fromisoformat(string_time_b[:-1])
  return (time_b - time_a).seconds

def calculate_limit(available_limit, transactions_amount):
  return available_limit - transactions_amount

def account_not_itialized(account, transaction):
  if (len(accounts) == 0):
    add_violation("account-not-initialized", "transaction")

def card_not_active(account, transaction):
  if (not(account.active_card)):
   add_violation("card-not-active", "transaction")

def insufficient_limit(account, transaction):
  if (calculate_limit(account.available_limit, sum_transactions_ammount(transactions))< 0):
    add_violation("insufficient-limit", "transaction")
  else:
    response['account']['available-limit'] = calculate_limit(account.available_limit, sum_transactions_ammount(transactions))

def high_frequency_small_interval(account, transaction):
  if len(transactions) >= 3:
    analyzed_transactions = transactions[:3]
    if (subtract_time(analyzed_transactions[0].time, analyzed_transactions[-1].time) <= 180):
      add_violation("high-frequency-small-interval", "transaction")
    
def account_already_initialized(account, transaction):
  if (len(accounts) > 0):
    add_violation("account-already-initialized", "account")

def iterates_through_criterias(criterias, account, transaction=""):
  aux_criterias = criterias.copy()
  if len(aux_criterias)>0:
    current_policy = list(aux_criterias)[0]
    aux_criterias[current_policy](account, transaction)
    del aux_criterias[current_policy]
    iterates_through_criterias(aux_criterias, account)

transaction_criterias_to_be_applied = {
    'account-not-initialized': account_not_itialized,
    'card-not-active': card_not_active,
    'insufficient-limit': insufficient_limit,
    'high-frequency-small-interval': high_frequency_small_interval
  }

account_criterias_to_be_applied = {
  'account-already-initialized': account_already_initialized
}

response = {
  'account': {
    'active-card': "",
    'available-limit': 0
  },
  'violations': []
}

def execute_transaction(param):
  global transaction_violations
  transaction_violations = []
  transaction = create_transaction(param["transaction"]["merchant"], param["transaction"]["amount"], param["transaction"]["time"])
  validate_transaction(accounts[0], transaction)
  print(response)
  

def execute_account(param):
  global account_violations
  account_violations = []
  account = create_account(param["account"]["active-card"], param["account"]["available-limit"])
  validate_account(account)
  print(response)
  

def build_response(account, violations):
  response["account"]["active-card"] = account.active_card
  response["account"]["available-limit"] = account.available_limit if(response["account"]["available-limit"]) == 0 else response["account"]["available-limit"]
  response["violations"] = violations

def validate_account(account):
  iterates_through_criterias(account_criterias_to_be_applied, account)
  if (not("account-already-initialized" in account_violations)):
    accounts.append(account)
  build_response(account, account_violations)
  

def validate_transaction(account, transaction):
  transactions.append(transaction)
  iterates_through_criterias(transaction_criterias_to_be_applied, account, transaction)
  build_response(account, transaction_violations)


    
param = {"account": {"active-card": False, "available-limit": 30}}

param2 = {"transaction": {"merchant": "Burger King", "amount": 20, "time":
"2019-02-13T10:00:00.000Z"}}
param3 = {"transaction": {"merchant": "Burger King", "amount": 20, "time":
"2019-02-13T10:01:00.000Z"}}
param4 = {"transaction": {"merchant": "Burger King", "amount": 20, "time":
"2019-02-13T10:02:00.000Z"}}


execute_account(param)
execute_transaction(param2)
execute_transaction(param3)
execute_transaction(param4)

    



