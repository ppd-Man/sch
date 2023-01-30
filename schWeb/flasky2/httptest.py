#!/usr/bin/python3
import requests
import json
import sys
# ' it.test@wiidreamthinker.com':'1234'
# r = requests.post('https://www.google.com.tw/')

server_address =str(sys.argv[1])

r = requests.post(f'http://{server_address}:5000/api/v1/tokens/', auth=(' it.test@wiidreamthinker.com', '1234'))
print(r.text)
print(r.json())
token=r.json()['token']
print(token)
order='{"ordernum": "A202111199","cupcount":1,"content":[{"cupnum":"0007-01","stationa":"03","stationb":"01000200030004000500","stationc":"01000200030004000500","stationd":"01000200030004050500","statione":"01000200030004000500","stationf":"01000200031704000500"}]}'


r = requests.post(f'http://{server_address}:5000/api/v1/posts/',auth=(token,''),json={'body':order})
print('====================================')
print(r.text)
