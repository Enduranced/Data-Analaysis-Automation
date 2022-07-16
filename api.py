import os
import requests

##API_key = 'BFG6InJETSpWj9eUBaF3kjTdZuRTs3fp' ## She has to input her own
def url_creator(from_curr, to_curr, API_key = 'BFG6InJETSpWj9eUBaF3kjTdZuRTs3fp'):
    url = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=" + from_curr
    "&to_currency=" + to_curr+ "&apikey=" + 'BFG6InJETSpWj9eUBaF3kjTdZuRTs3fp'

    r = requests.get(url)
    data = r.json()
    return data

