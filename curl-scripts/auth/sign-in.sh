# EMAIL=d@d.com PASSWORD=daddy sh curl-scripts/auth/sign-in.sh

curl "http://localhost:8000/sign-in/" \
  --include \
  --request POST \
  --header "Content-Type: application/json" \
  --data '{
    "credentials": {
      "email": "'"${EMAIL}"'",
      "password": "'"${PASSWORD}"'"
    }
  }'

echo
