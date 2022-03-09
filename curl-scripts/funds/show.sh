#!/bin/bash

# TOKEN=1bedb342e66d235c6d73d48df07863f0e54afa59 ID=2 sh curl-scripts/funds/show.sh

curl "http://localhost:8000/funds/${ID}/" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"

echo
