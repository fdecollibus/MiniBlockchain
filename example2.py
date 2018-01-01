
import hashlib
import sys
textFile=open(sys.argv[1],"r")
todayTransaction = ""
for i in textFile:
    todayMenu+=i
print(todayTransaction)
hash_object = hashlib.sha256(todayTransaction.encode())
hex_dig = hash_object.hexdigest()
print(type(hex_dig))
print(hex_dig)
