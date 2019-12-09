# Functions file

## Reading file function
def file_read(file):
    with open(file,'r') as opened_file:
        return opened_file.readlines()

## Writing file function (overwriting everything existing)
def file_overwrite(file, item):
    with open(file,'w') as opened_file:
        return opened_file.write(item)

## Writing file function (extending from existing on a new line)
def file_append(file, item):
    with open(file,'a') as opened_file:
        return opened_file.write('\n'+item)



#------------------------------------------------------------------
## functions testing
    ### read file testing
# lines = file_read('user_name.txt')
# for line in lines:
#     print(line.strip('\n'))
    ### overwrite file testing
# file_overwrite('user_name.txt','12345678910')
    ### appending file on a new line testing
# file_append('user_name.txt','abcdefghijk')