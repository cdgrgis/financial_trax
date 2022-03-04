#!/bin/bash

# TOKEN=6f2250de1ced069c1be2c107da20a61d1ad63538 NAME=IRA COMPANY=Voya BALANCE=4470 sh curl-scripts/accounts/create.sh

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
