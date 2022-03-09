#!/bin/bash

# TOKEN=7154deb5839d198e2395c4034411a7bf223708ba TICKER_SYMBOL=GME COMPANY_NAME="GameStop Corp" PRICE=105.21 sh curl-scripts/funds/create.sh

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
