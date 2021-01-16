import pytest
import os
import time


def test_process_adding_new_operations(capsys):
  os.system('python3 authorizer.py support_files/operations')
  captured = capsys.readouterr()
  print(captured.out)
  #assert  "{'account': {'active-card': True, 'available-limit': 30}, 'violations': []}" in captured.out
  

  