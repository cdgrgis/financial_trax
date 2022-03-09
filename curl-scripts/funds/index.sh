#!/bin/bash

# TOKEN=7154deb5839d198e2395c4034411a7bf223708ba sh curl-scripts/funds/index.sh

curl "http://localhost:8000/funds/" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"

echo
