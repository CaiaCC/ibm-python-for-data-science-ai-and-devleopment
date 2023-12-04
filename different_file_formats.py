import pandas as pd

# CSV
url ='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/addresses.csv'

df = pd.read_csv(url, header=None)
df.columns = ['First Name', 'Last Name', 'Location', 'City', 'State', 'Area Code']

# print(df)
print(df["First Name"]) # select 1 column
cols = df[['First Name', 'Last Name', 'Location', 'City']] # select multiple columns
print(cols)