import pandas as pd
import api


overheads = pd.read_csv(r'/home/spencer/Homework(Tuition)/overheads.csv')

## Findign the max
def Overhead_max(data):
    val = data.Overheads.idxmax()
    result = {data.loc[val].Category : data.loc[val].Overheads}
    print(result)
    return result

if __name__ == '__main__':
    Overhead_max(overheads)
