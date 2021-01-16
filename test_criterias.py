from application import *
from db import *
import pytest
  

def test_account_already_initialized():
  accountA = Account(True, 30)
  accountB = Account(True, 40)
  transactionA = Transaction("BK", 30, "2019-02-13T10:00:00.000Z")

  accounts.append(accountB)

  assert account_already_initialized(transactionA, accountB) == True
  
  
def test_account_not_itialized():
  transactionA = Transaction("BK", 30, "2019-02-13T10:00:00.000Z")

  assert account_not_itialized(transactionA) == False


def test_card_not_active():
  accountA = Account(True, 30)
  transactionA = Transaction("BK", 30, "2019-02-13T10:00:00.000Z")

  assert card_not_active(transactionA, accountA) == False


def test_insufficient_limit():
  accountA = Account(True, 30)
  transactionA = Transaction("BK", 30, "2019-02-13T10:00:00.000Z")
  transactionB = Transaction("BK", 30, "2019-02-13T10:02:00.000Z")
  transactions.append(transactionA)
  transactions.append(transactionB)

  assert insufficient_limit(transactionA, accountA) == True
  

def test_high_frequency_small_interval():
  accountA = Account(True, 30)
  transactionA = Transaction("BK", 30, "2019-02-13T10:00:00.000Z")
  transactionB = Transaction("BK", 30, "2019-02-13T10:02:00.000Z")
  transactionC = Transaction("BK", 30, "2019-02-13T10:10:00.000Z")
  transactions.append(transactionA)
  transactions.append(transactionB)
  transactions.append(transactionC)

  assert high_frequency_small_interval(transactionC, accountA) == False


def test_doubled_transactions():
  accountA = Account(True, 30)
  transactionA = Transaction("BK", 30, "2019-02-13T10:00:00.000Z")
  transactionB = Transaction("BK", 30, "2019-02-13T10:05:00.000Z")
  transactionC = Transaction("BK", 30, "2019-02-13T10:10:00.000Z")
  transactions.append(transactionA)
  transactions.append(transactionB)
  transactions.append(transactionC)

  assert doubled_transactions(transactionC, accountA) == False

 
def test_sum_transactions_ammount():
  transactionA = Transaction("BK", 30, "2019-02-13T10:00:00.000Z")
  transactionB = Transaction("BK", 30, "2019-02-13T10:02:00.000Z")
  transactionC = Transaction("BK", 30, "2019-02-13T10:03:00.000Z")
  transactions = [transactionA, transactionB, transactionC]

  assert sum_transactions_ammount(transactions) == 90


def test_subtract_time():
  assert subtract_time("2019-02-13T10:00:00.000Z", "2019-02-13T10:02:00.000Z") == 120


def test_calculate_limit():
  accountA = Account(True, 100)
  assert calculate_limit(accountA.available_limit, 90) == 10


def test_same_transactions():
  transactionA = Transaction("BK", 30, "2019-02-13T10:00:00.000Z")
  transactionB = Transaction("BK", 30, "2019-02-13T10:02:00.000Z")

  assert same_transactions(transactionA, transactionB) == True
