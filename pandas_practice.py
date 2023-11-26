import pandas as pd
import piplite


'''
# Read the CSV file into a DataFrame

df = pd.read_csv('your_file.csv')


# Create a Series from a list
data = [10, 20, 30, 40, 50]
s = pd.Series(data)
print(s)
print(s.iloc[3])
print(s[1:4])

'''

'''
# Creating a DataFrame from a dictionary
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 28],
        'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']}
df = pd.DataFrame(data)
print(df)
print(df['Name'])  # Access the 'Name' column
df.to_csv('test_data.csv', index=True)
'''

# Read dat from CSV file
from pyodide.http import pyfetch
import pandas as pd

filename = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/TopSellingAlbums.csv"

async def download(url, filename):
    response = await pyfetch(url)
    if response.status == 200:
        with open(filename, "wb") as f:
            f.write(await response.bytes())


await download(filename, "TopSellingAlbums.csv")
df = pd.read_csv("TopSellingAlbums.csv")


# Read data from Excel File and print the first five rows

xlsx_path = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/jupyterlite/files/Module%205/data/TopSellingAlbums.xlsx'

await download(xlsx_path, "TopSellingAlbums.xlsx")
df = pd.read_excel("TopSellingAlbums.xlsx")
df.head()