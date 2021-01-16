from application import create_account_use_case, create_transaction_use_case
import json


def readlines(file):
  file1 = open(file, 'r') 
  Lines = file1.readlines() 
  result = []
  for line in Lines: 
      print(identify_and_call_operation(json.loads(line)))


def identify_and_call_operation(json_line):
  if (list(json_line)[0] == "account"):
    return create_account_use_case(json_line)
  elif (list(json_line)[0] == "transaction"):
    return create_transaction_use_case(json_line)


    