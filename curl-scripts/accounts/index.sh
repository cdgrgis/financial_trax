#!/bin/bash

# TOKEN=60ac91d719ef6aeb2610c9e907337b73d80700b7 sh curl-scripts/accounts/index.sh

curl "http://localhost:8000/accounts/" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"

echo
