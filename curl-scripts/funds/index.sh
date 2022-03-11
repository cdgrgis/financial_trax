#!/bin/bash

# TOKEN=4ddc0eb92455ae1dc557cd14d877f48f17d1673c sh curl-scripts/funds/index.sh

curl "http://localhost:8000/funds/" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"

echo
