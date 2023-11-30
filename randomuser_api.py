from randomuser import RandomUser
import pandas as pd

'''
r = RandomUser()
random_list = r.generate_users(10)
name = r.get_full_name()
for user in random_list:
    print(user.get_full_name()," ", user.get_email())
'''


def get_users():
    users = []
    for user in RandomUser.generate_users(10):
        users.append({"Name": user.get_full_name(), "Gender": user.get_gender(), "City":user.get_city(),"State":user.get_state(),"Email":user.get_email(), "DOB":user.get_dob(),"Picture":user.get_picture()})
    return pd.DataFrame(users)

users = get_users()
print(users.head())
