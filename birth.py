import hashlib
import random

secret = "698d51a19d8a121ce581499d7b701668" #111
dict = '1234567890'

for i in range (858993459):
    pwd = ''

    for j in range (3):
        pwd += random.choice( dict )
    hash = hashlib.md5(pwd.encode('utf-8')).hexdigest()
    file = open('date.txt', 'a')
    file.write(hash + '\n')
    file.close()

find = "1"
file = open('date.txt', 'r')
while find:
    find = file.readline()
    find = find.rstrip('\n')
    if (find == secret):
        print("done")
        break;
#работает,прочитать про json формат,чтобы хранить данные в виде - пароль:хеш
#либо все в форе делать,закрывая файл, а потом опять открывая
