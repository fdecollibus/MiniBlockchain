
import hashlib
todayTransaction = "I have received 10 buck and I have given you 5 bucks"
hash_object = hashlib.sha256(todayTransaction.encode())
hex_dig = hash_object.hexdigest()
print(hex_dig)
