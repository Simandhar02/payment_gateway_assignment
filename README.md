Steps to setup this repo on your machine
1. Clone this repository to your local machine
2. create virtualenv with python3
3. install requirements.txt in the virtualenv
4. execute ./startup.sh
5. Success CURL Request for the API 

curl --location --request POST 'http://0.0.0.0:5012/api/v1/payment/process' \
--header 'Content-Type: application/json' \
--data-raw '{
	"CreditCardNumber": "6594999912346789",
	"CardHolder": "John",
	"ExpirationDate": "2021-01-19T12:22:49",
	"SecurityCode": "567",
	"Amount": "400"
}'

***** To verify the retry mechanism, comment out line numbers 16 and 17 in url_list .py *****