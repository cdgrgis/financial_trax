#!/bin/bash

# TOKEN=4ddc0eb92455ae1dc557cd14d877f48f17d1673c ID=1 sh curl-scripts/fund-infos/delete.sh

curl "http://localhost:8000/fund-infos/${ID}/" \
  --include \
  --request DELETE \
  --header "Authorization: Token ${TOKEN}"

echo
