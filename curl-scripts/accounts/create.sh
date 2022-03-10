#!/bin/bash

# TOKEN=60ac91d719ef6aeb2610c9e907337b73d80700b7 TYPE=ROTH COMPANY=PM BALANCE=345 INCEPTION=03-17-2022 ACCOUNT_NUMBER=1426 sh curl-scripts/accounts/create.sh

curl "http://localhost:8000/accounts/" \
  --include \
  --request POST \
  --header "Content-Type: application/json" \
  --header "Authorization: Token ${TOKEN}" \
  --data '{
    "account": {
      "type": "'"${TYPE}"'",
      "company": "'"${COMPANY}"'",
      "balance": "'"${BALANCE}"'",
      "inception": "'"${INCEPTION}"'",
      "account_number": "'"${ACCOUNT_NUMBER}"'"
    }
  }'

echo
