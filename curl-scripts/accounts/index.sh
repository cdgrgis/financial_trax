#!/bin/bash

# TOKEN=cbcb9f0e415f2ddce2cd0d4d09e507d0e0b1ca5b sh curl-scripts/accounts/index.sh

curl "http://localhost:8000/accounts/" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"

echo
