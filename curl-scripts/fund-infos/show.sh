#!/bin/bash

# TOKEN=b70b51a015fd4ec654b832f18a28639bcd839571 ID=15 sh curl-scripts/fund-infos/show.sh

curl "http://localhost:8000/fund-infos/${ID}/" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"

echo
