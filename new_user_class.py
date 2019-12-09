from user_name_db import *

class New_user():
    def __init__(self,name):
        self.name = name

    # behaviors
    def user_info(self):
        return open(str(self.name+'.txt'),'w')









### testing -------------------------------------------
    ### read test
new_user_1 = New_user('James')
new_user_1.user_info()
