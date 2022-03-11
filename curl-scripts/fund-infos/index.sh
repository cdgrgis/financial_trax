#!/bin/bash

# TOKEN=b70b51a015fd4ec654b832f18a28639bcd839571 sh curl-scripts/fund-infos/index.sh

curl "http://localhost:8000/fund-infos/" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"
  --data '{
    "account: "'"${ACCOUNT}"'"
    }'
    
echo
