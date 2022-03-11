#!/bin/bash

# TOKEN=b70b51a015fd4ec654b832f18a28639bcd839571 ID=3 sh curl-scripts/fund-infos/index_specific.sh

curl "http://localhost:8000/accounts/${ID}/fund-infos/" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}" \


echo
