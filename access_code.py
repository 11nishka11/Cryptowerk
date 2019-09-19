import requests
import random
import hashlib
import json
import time

store = open("store-key.txt","w+")

print("generating a random 26-bit number")
p = random.getrandbits(26)
print(p)

print("appending a timestamp and security code")
s = random.getrandbits(38)

key = str(p)+str(s)

print(key)

m=hashlib.sha256(key.encode('utf-8')).hexdigest()

print ("our hashed access code is: ")
print(m)

headers = {'Accept':'application/json','X-API-Key': '3Rt2HsLBzpbh50COmNeS9HuJhzQRTKs6MpLw7uhZbaw= Li9Z+kSdllv0VCJj9ccFksxcmCRsNmvVyKYT3Ba6MBA='}

r = requests.post('https://developers.cryptowerk.com/platform/API/v8/register', params={'hashes': m},headers = headers)

data = r.json()
ret_id = data['documents'][0]['retrievalId']
print (data)
print(ret_id)
store.write(ret_id)


store.close()

