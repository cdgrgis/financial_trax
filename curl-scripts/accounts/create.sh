#!/bin/bash

# TOKEN=454be1befad99ad3d4a6cc8d19ebbbba777d5433 TYPE=IRA COMPANY=Voya BALANCE=4470 INCEPTION=2022-03-01 ACCOUNT_NUMBER=123456 sh curl-scripts/accounts/create.sh

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
