import pandas as pd
import api

cash_on_hand = pd.read_csv(r'/home/spencer/Homework(Tuition)/cash-on-hand-thb.csv')

from_curr  = 'THB'
to_curr = 'SGD'
'''currency_data = api.url_creator(from_curr,to_curr)'''
## Use this data stucture temperoray
currency_data = {'Realtime Currency Exchange Rate': {'1. From_Currency Code': 'USD', '2. From_Currency Name': 'United States Dollar', '3. To_Currency Code': 'SGD', '4. To_Currency Name': 'Singapore Dollar', '5. Exchange Rate': '1.39980000', '6. Last Refreshed': '2022-07-16 12:48:02', '7. Time Zone': 'UTC', '8. Bid Price': '1.39980000', '9. Ask Price': '1.39980000'}}

def Daily_checker(data):
    issues  = {}
    cash_on_hand = data['Cash On Hand']
    
    days = data['Day']
    print(len(days))

    for i in range(len(data)):
        ## Checking the dip
        if  i == len(data)-1:
            break
        if cash_on_hand[i] < cash_on_hand[i+1]:
            diff = 
            issues[days[i]] = cash_on_hand[i]
    print(issues)
        


if __name__ == '__main__':
    Daily_checker(cash_on_hand)


