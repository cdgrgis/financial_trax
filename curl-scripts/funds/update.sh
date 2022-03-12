#!/bin/bash

# TOKEN=b70b51a015fd4ec654b832f18a28639bcd839571 PRICE=100.05 ID=41 sh curl-scripts/funds/update.sh

curl "http://localhost:8000/funds/${ID}/" \
  --include \
  --request PATCH \
  --header "Content-Type: application/json" \
  --header "Authorization: Token ${TOKEN}" \
  --data '{
    "fund": {
      "price": "'"${PRICE}"'"
    }
  }'

echo
