import hashlib
import random

secret = "962012d09b8170d912f0669f6d7d9d07" 
dict = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'

int minLen
int maxLen
for i in range (2147483648):
    pwd = ''

    for j in range (random.randint(minLen, maxLen)):
        pwd += random.choice( dict )
    hash = hashlib.md5(pwd.encode('utf-8')).hexdigest()
    if(hash == secret):
        print(pwd + " done")
        break;
        
