import re

v=input('Enter Your Password')

if(len(v)>=8):
    if(bool(re.match('((?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%*&^]).{8,30})',v))==True):
        print('The password is strong')
        
    elif(bool(re.match('((\d*)([a-z]*)([A-Z]*)([!@#$%*&^]*).{8,30})',v))==True):
        print('The password is weak')
        
else:
    print('You have entered the wrong password')