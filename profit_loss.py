import pandas as pd
import api


PnL = pd.read_csv(r'/home/spencer/Homework(Tuition)/profit-and-loss-thb.csv')
def Daily_checker(data):
    Days = data.Day
    Net_Profit = data['Net Profit']
    issues = {}
    ## Checking for the dip
    for i in range(len(Days)): ## u can apply the start stop and step method here instead
        if (i == 0) or (i == len(Days)):
            continue
        if Net_Profit[i] < Net_Profit[i-1]:
            diff = abs(Net_Profit[i]) - abs(Net_Profit[i-1]) # Take the absolute difference
            issues[Days[i]] = [Net_Profit[i] , diff]
    print(issues)



    return

if __name__ == '__main__':
    Daily_checker(PnL)
