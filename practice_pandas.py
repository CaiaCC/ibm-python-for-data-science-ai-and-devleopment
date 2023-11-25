import pandas as pd

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

# Creating a DataFrame from a dictionary
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 28],
        'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']}
df = pd.DataFrame(data)
print(df)
print(df['Name'])  # Access the 'Name' column
'''
df.to_csv('test_data.csv', index=True)
'''