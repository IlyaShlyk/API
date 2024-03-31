import requests

api_url = 'https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/btc.json'
response = requests.get(api_url)
data = response.json()
date = data["date"]
kurs = data["btc"]["rub"]
if response.status_code == 200:
    print("Дата запроса: ", date)
    print("Курс биткоина к рублю: ", kurs)
else:
    print(response.status_code)
