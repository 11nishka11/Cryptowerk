import requests

#get_key = open("store-key.txt","r")
headers = {'Accept':'application/json','X-API-Key': '3Rt2HsLBzpbh50COmNeS9HuJhzQRTKs6MpLw7uhZbaw= Li9Z+kSdllv0VCJj9ccFksxcmCRsNmvVyKYT3Ba6MBA='}

with open("store-key.txt") as get_key:
      ret_id = (list(get_key)[-1])
v = requests.post('https://developers.cryptowerk.com/platform/API/v8/verify', params={'retrievalId':ret_id}, headers = headers)
print (v.json())

verify = v.json()
inserted = verify['documents'][0]['hasBeenInsertedIntoAllRequestedBlockchains']
if inserted:
      print ("this  value has been added to the blockchain");

