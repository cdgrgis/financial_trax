#!/bin/bash

# TOKEN=b70b51a015fd4ec654b832f18a28639bcd839571 ID=15 AMOUNT_OWNED=9 sh curl-scripts/fund-infos/update.sh

curl "http://localhost:8000/fund-infos/${ID}/" \
  --include \
  --request PATCH \
  --header "Content-Type: application/json" \
  --header "Authorization: Token ${TOKEN}" \
  --data '{
    "fund_info": {
      "amount_owned": "'"${AMOUNT_OWNED}"'"
      }
    }'

echo
