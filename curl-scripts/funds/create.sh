#!/bin/bash

# TOKEN=461aa69af742f3f5502f78a010e0818f37cf4f5e TICKER_SYMBOL=AAPL COMPANY_NAME="Apple Inc" PRICE=162.95 sh curl-scripts/funds/create.sh

curl "http://localhost:8000/funds/" \
  --include \
  --request POST \
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
