import pytest
import os
import time


def test_process_adding_new_operations(capfd):
  os.system('python3 authorizer.py support_files/operations')
  captured = capfd.readouterr()
  assert  "{'account': {'active-card': True, 'available-limit': 30}, 'violations': []}" in captured.out
  assert  "{'account': {'active-card': True, 'available-limit': 10}, 'violations': []}" in captured.out
  assert  "{'account': {'active-card': True, 'available-limit': 10}, 'violations': ['insufficient-limit', 'doubled-transactions']}" in captured.out
  assert  "{'account': {'active-card': True, 'available-limit': 10}, 'violations': ['insufficient-limit', 'high-frequency-small-interval', 'doubled-transactions']}" in captured.out
  

  