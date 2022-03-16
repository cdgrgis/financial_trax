An app for tracking stocks and accounts, with previous day's stock prices

This project was started as the final submission piece for my Software Engineering boot camp with General Assembly.

## Setup Steps
  1. Fork and clone this repository
  2. Run `npm install` to install all dependencies.
  3. Use `npm run server` to start up server.
   
# Important Links
[Deployed Site] (https://cdgrgis.github.io/financial_trax_client)
[API Repository] (https://github.com/cdgrgis/financial_trax_api)
[API] (https://financial-trax-api.herokuapp.com)

## User Model
  - email
  - hashedPassword

## Account Model
  - type
  - company
  - inception
  - account_number
  - funds(ref to Fund through FundInfo)
  - owner(ref to User)

## Fund Model
  - ticker_symbol
  - company_name
  - price
  - owner(ref to User)

## FundInfo Model
  - amount_owned
  - balance

## Routes
  - accounts/ (GET, POST)
  - accounts/<int:pk>/ (GET, PATCH, DELETE)
  - accounts/<int:pk>/fund-infos/ (GET, POST)
  - funds/ (GET, POST)
  - funds/<int:pk>/ (GET, PATCH, DELETE)
  - fund-infos/ (GET, POST)
  - fund-infos/<int:pk>/ (GET, PATCH, DELETE)
  - sign-up/ (POST)
  - sign-in/ (POST)
  - sign-out/ (DELETE)
  - change-pw/ (PATCH)

# ERD
![Models](https://user-images.githubusercontent.com/88337158/156482703-cb6e21ee-2890-4d3a-bcd3-533f96407315.png)
