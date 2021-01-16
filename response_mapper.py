response = {
  'account': {
    'active-card': "",
    'available-limit': 0
  },
  'violations': []
}


def build_response(account, violations):
  response["account"]["active-card"] = account.active_card
  response["account"]["available-limit"] = account.available_limit if(response["account"]["available-limit"]) == 0 else response["account"]["available-limit"]
  response["violations"] = violations