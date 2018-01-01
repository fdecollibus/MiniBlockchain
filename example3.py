import random
import string
import hashlib
import sys
import time

def randomword(length):
   return ''.join(random.choice(string.ascii_lowercase) for i in range(length))

start = time.time()
textFile=open(sys.argv[1],"r")
todayTransaction = ""
for i in textFile:
    todayTransaction+=i
print(todayTransaction)
hex_dig = ''
while not(hex_dig.startswith('00000')):
    nonce = randomword(10)
    hash_object = hashlib.sha256((todayTransaction + nonce).encode())
    hex_dig = hash_object.hexdigest()
    print(hex_dig)
end = time.time()
print("your desired nonce is: " + nonce)
print(todayTransaction + nonce)
print(hex_dig)
print(" it took {} seconds to find out".format(end-start))
textFile=open(sys.argv[1],"w")
textFile.write(todayTransaction + nonce)
textFile.close()
