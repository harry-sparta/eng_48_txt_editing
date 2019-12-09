from functions import *

## Variable = text document to be read
file_user = 'user_name.txt'
## Creating an empty dictionary
user_dict = {}
## Calling read function to return content in file_user
file_user_list = file_read(file_user)
print(file_user_list)
## Setting a counter to count and name user object in for loop below
user_counter = 1
## for loop to insert individual user_"num" : "name" into user_dictionary. Where "num" is incremental.
for user in file_user_list:
    user_formatted = user.strip('\n')
    user_dict[f'user_{user_counter}'] = user_formatted
    user_counter += 1

## Check updated dictionary for all user_"num" : "name" stored
print(user_dict)
