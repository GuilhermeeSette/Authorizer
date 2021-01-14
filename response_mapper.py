response = {
  'account': {
    'active-card': "",
    'available-limit': ""
  },
  'violations': []
}

def build_response(account, violations):
  response["account"]["active-card"] = account.active_card
  response["account"]["available-limit"] = account.available_limit
  response["violations"] = violations