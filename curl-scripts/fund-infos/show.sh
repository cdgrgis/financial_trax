#!/bin/bash

# TOKEN=4ddc0eb92455ae1dc557cd14d877f48f17d1673c ID=1 sh curl-scripts/fund-infos/show.sh

curl "http://localhost:8000/fund-infos/${ID}/" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"

echo
