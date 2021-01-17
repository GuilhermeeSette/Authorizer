from application import *
from db import *
import pytest


def test_create_account_use_case():
  param = {"account": {"active-card": True, "available-limit": 30}}
  assert create_account_use_case(param) == {'account': {'active-card': True, 'available-limit': 30}, 'violations': []}


def test_create_transaction_use_case():
  param = {"transaction": {"merchant": "Burger King", "amount": 20, "time":
"2019-02-13T10:10:00.000Z"}}
  assert create_transaction_use_case(param) == {'account': {'active-card': True, 'available-limit': 10}, 'violations': []}

