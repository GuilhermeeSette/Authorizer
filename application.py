from account import *
from transaction import *
from datetime import datetime
from response_mapper import *
from db import *


def create_transaction_use_case(param):
  global transaction_violations
  transaction_violations = []
  transaction = create_transaction(param["transaction"]["merchant"], param["transaction"]["amount"], param["transaction"]["time"])
  account_not_itialized(transaction)
  if (not("account-not-initialized" in transaction_violations)):
    validate_transaction(accounts[0], transaction)
  else:
    response["violations"] = transaction_violations
  return response
  

def create_account_use_case(param):
  global account_violations
  account_violations = []
  account = create_account(param["account"]["active-card"], param["account"]["available-limit"])
  validate_account(account)
  return response


def validate_account(account):
  iterates_through_criterias(account_criterias_to_be_applied, account)
  if (not("account-already-initialized" in account_violations)):
    accounts.append(account)
  build_response(account, account_violations)
  

def validate_transaction(account, transaction):
  transactions.append(transaction)
  iterates_through_criterias(transaction_criterias_to_be_applied, account, transaction)
  build_response(account, transaction_violations)


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


def same_transactions(transactionA, transactionB):
  return transactionA.merchant == transactionA.merchant and transactionA.amount == transactionB.amount



def account_not_itialized(transaction, account=""):
  if (len(accounts) == 0):
    add_violation("account-not-initialized", "transaction")
    return True
  return False


def card_not_active(transaction, account):
  if (not(account.active_card)):
   add_violation("card-not-active", "transaction")
   return True
  return False


def insufficient_limit(transaction, account):
  if (calculate_limit(account.available_limit, sum_transactions_ammount(transactions))< 0):
    add_violation("insufficient-limit", "transaction")
    return True
  else:
    response['account']['available-limit'] = calculate_limit(account.available_limit, sum_transactions_ammount(transactions))
    return False


def high_frequency_small_interval(transaction, account):
  if len(transactions) >= 3:
    analyzed_transactions = transactions[:3]
    if (subtract_time(analyzed_transactions[0].time, analyzed_transactions[-1].time) <= 120):
      add_violation("high-frequency-small-interval", "transaction")
      return True
  return False

def doubled_transactions(transaction, account):
  if len(transactions) >= 2:
    analyzed_transactions = transactions[:2]
    if (subtract_time(analyzed_transactions[0].time, analyzed_transactions[-1].time) <= 120 and same_transactions):
      add_violation("doubled-transactions", "transaction")
      return True
  return False
    

def account_already_initialized(transaction, account):
  if (len(accounts) > 0):
    add_violation("account-already-initialized", "account")
    return True
  return False


def iterates_through_criterias(criterias, account, transaction=""):
  aux_criterias = criterias.copy()
  if len(aux_criterias)>0:
    current_policy = list(aux_criterias)[0]
    aux_criterias[current_policy](transaction, account)
    del aux_criterias[current_policy]
    iterates_through_criterias(aux_criterias, account)


transaction_criterias_to_be_applied = {
    'account-not-initialized': account_not_itialized,
    'card-not-active': card_not_active,
    'insufficient-limit': insufficient_limit,
    'high-frequency-small-interval': high_frequency_small_interval,
    'doubled-transactions': doubled_transactions
  }


account_criterias_to_be_applied = {
  'account-already-initialized': account_already_initialized
}

    



