# Run file
from new_user_class import *
from functions import *

# 0.) Initial setup - overwrite 10 names in file
    ## 10 names
initial_setup = ['Tom', 'James', 'Indie', 'Peter', 'Lawrence', 'Bob', 'Langley', 'Tottenpoo', 'Alvaro', 'Nigel']
    ## overwrite user_name.txt file with 1st name item 'Tom'
file_overwrite('user_name.txt',(initial_setup[0]))
    ## append the rest of the 9 names with a for loop
for line in initial_setup[1:]:
    file_append('user_name.txt', str(line))

# 1.) Read file and store each name as an object
file_user = 'user_name.txt'
user_dict = {}

file_user_list = file_read(file_user)
print(file_user_list)
user_counter = 1
for user in file_user_list:
    user_formatted = user.strip('\n')
    user_dict = {f'user_{user_counter}' : user_formatted}
    print(user_dict)
    user_counter += 1



