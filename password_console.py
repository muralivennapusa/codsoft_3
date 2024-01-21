import random
import string

def funcPassword(length):
    char = string.ascii_letters + string.digits + string.punctuation
    result = ''.join(random.choice(char) for _ in range(length))
    return result

n=input("Enter Number of Characters: ")

if n=='':
    passwd="ERROR: Empty password"
elif (n.isdigit() and int(n)>100):
    passwd="ERROR: password length must be less than 100"
elif(n.isdigit() and int(n)>0):
    passwd=funcPassword(int(n))
elif(n[0]=='+' and n[1:].isdigit() and int(n)>0 and int(n)<100):
    passwd=funcPassword(int(n))
elif (n[0]=='-' and n[1:].isdigit() and int(n)<=0):
    passwd="ERROR: enter a valid LENGTH value"
elif (n.isdigit() and int(n)==0):
    passwd="ERROR: password length must be greater than zero"
elif ((n[0]=='-' or n[0]=='+') and n[:1].isdigit() and int(n)==0):
    passwd="ERROR: password length must be greater than zero"
else:
    passwd="ERROR: INVALID PASSWORD"
print("Generated password:-\n",passwd)
