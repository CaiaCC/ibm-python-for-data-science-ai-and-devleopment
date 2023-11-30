import requests
import json
import pandas as pd

data = requests.get('https://fruityvice.com/api/fruit/all')
result = json.loads(data.text)
df1 = pd.DataFrame(result)
# result is a nested json format, so df1 contains multiple subcolumns -> needs to be flattened/normalized
df2 = pd.json_normalize(result)

'''
print('df1', df1)
print('df2', df2)
'''
cherry = df2.loc[df2["name"] == 'Cherry']
print(cherry)
print((cherry.iloc[0]['family']) , (cherry.iloc[0]['genus']))