
import random
import string
import hashlib
import sys
import time
import glob

def randomword(length):
   return ''.join(random.choice(string.ascii_lowercase) for i in range(length))

originalTransaction = "This is the holy starting point of our glorious blockchain"
hash_object = hashlib.sha256(originalTransaction.encode())
original_hex_dig = hash_object.hexdigest()
print("Previous hash to match:{}".format(original_hex_dig))
filenames = glob.glob("block*.bck")
difficulty=2
for filename in sorted(filenames):
    print("Now processing block {}".format(filename))
    textFile=open(filename,"r+")
    accumulator = ""
    for line in textFile:
        accumulator+=line
        if line.startswith('previousHash='):
            previousHash = line.split('=')[-1].strip()
            print(previousHash)
            if (previousHash==original_hex_dig):
                print("Previous transaction verified")
            else :
                print(accumulator)
                raise Exception("Previous block not verified, transaction tampered");
        if line.startswith('nonce='):
            currentNonce = line.split('=')[-1].strip()
            if (len(currentNonce)<1):
                start = time.time()
                hex_dig = ''
                while not(hex_dig.startswith(difficulty*'0')):
                    nonce = randomword(10)
                    hash_object = hashlib.sha256((accumulator + nonce).encode())
                    hex_dig = hash_object.hexdigest()
                    print(hex_dig)
                    end = time.time()
                print("your desired nonce is: " + nonce)
                print(" it took {} seconds to find out".format(end-start))
                textFile.write(line[:len(line)-1]+nonce)
                if ((end-start)<5):
                    difficulty+=1
                    print("Problem is too easy: increasing difficulty to: {}".format(difficulty))
                if ((end-start)>20):
                    difficulty-=1
                    print("Problem is too difficult: decreasing difficulty to {}".format(difficulty))
                textFile.close()
                break;
