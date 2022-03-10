#!/bin/bash

# TOKEN=60ac91d719ef6aeb2610c9e907337b73d80700b7 AMOUNT_OWNED=4 BALANCE=20 ACCOUNT=3 FUND=3 sh curl-scripts/fund-infos/create.sh

curl "http://localhost:8000/fund-infos/" \
  --include \
  --request POST \
  --header "Content-Type: application/json" \
  --header "Authorization: Token ${TOKEN}" \
  --data '{
    "fund_info": {
      "amount_owned": "'"${AMOUNT_OWNED}"'",
      "balance": "'"${BALANCE}"'",
      "account": "'"${ACCOUNT}"'",
      "fund": "'"${FUND}"'"
    }
  }'

echo
