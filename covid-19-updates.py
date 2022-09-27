import requests
import json
from win10toast import ToastNotifier
import time

response = requests.get('https://coronavirus-19-api.herokuapp.com/countries')
data = response.json()
# print(data[1])
def covid_update():
    cases = data[1]['cases']
    deaths = data[1]['deaths']
    today_cases = data[1]['todayCases']
    today_deaths = data[1]['todayDeaths']
    recovered = data[1]['recovered']
    text = f'Confirmed Cases: {cases}\nDeaths: {deaths}\nToday Case: {today_cases}\nToday Death: {today_deaths}\nRecovered: {recovered}\n'

    while True:
        toast = ToastNotifier()
        toast.show_toast('Covid-19 Updates USA', text, duration= 15)
        time.sleep(8)

covid_update()