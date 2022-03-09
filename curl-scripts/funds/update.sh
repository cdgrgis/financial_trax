#!/bin/bash

# TOKEN=7154deb5839d198e2395c4034411a7bf223708ba TICKER_SYMBOL=AAPL COMPANY_NAME="Apple Inc" PRICE=0.95 ID=3 sh curl-scripts/funds/update.sh

curl "http://localhost:8000/funds/${ID}/" \
  --include \
  --request PATCH \
  --header "Content-Type: application/json" \
  --header "Authorization: Token ${TOKEN}" \
  --data '{
    "fund": {
      "ticker_symbol": "'"${TICKER_SYMBOL}"'",
      "company_name": "'"${COMPANY_NAME}"'",
      "price": "'"${PRICE}"'"
    }
  }'

echo
