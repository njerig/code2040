# !/usr/bin/python
# njerig
# CODE2040 Challenge

import requests
import datetime
from datetime import timedelta
import dateutil.parser

def main():
    token = 'a272e0e398eaa14ddeeaaf9cdc21d55d'
    base_url = 'http://challenge.code2040.org/api/'
    headers = {'content-type': 'application/json'}

    #step_one(token, base_url+'register/', headers)
    #step_two(token, base_url+'reverse/', headers)
    #step_three(token, base_url+'haystack/', headers)
    #step_four(token, base_url+'prefix/', headers)
    step_five(token, base_url+'dating/', headers)

def step_one(token, url, headers):
	p = requests.post(url, json={'token': token, 'github': 'https://github.com/njerig/code2040.git'}, headers=headers)
	result = p.text
	print(result)
	return result

def step_two(token, url, headers):
    p_one = requests.post(url, json={'token': token}, headers=headers)

    the_string = p_one.text
    r_string = the_string[::-1]

    p_two = requests.post(url+'validate/', json={'token': token, 'string': r_string}, headers=headers)
    result = p_two.text
    print(result)
    return(result)

def step_three(token, url, headers):
    p_one = requests.post(url, json={'token': token}, headers=headers)
    d = ast.literal_eval(p_one.text)

    needle = d['needle']
    haystack = d['haystack']
    if needle in haystack:
        index = haystack.index(needle)

    p_two = requests.post(url+'validate/', json={'token': token, 'needle': index}, headers=headers)
    result = p_two.text
    print(result)
    return(result)

def step_four(token, url, headers):
    headers = {'content-type': 'application/json'}
    p_one = requests.post(url, json = {'token': token}, headers = headers)
    d = p_one.json()

    array = d['array']
    prefix = d['prefix']
    doesnt = []
    for gibberish in array:
        if not gibberish.startswith(prefix):
            doesnt.append(gibberish)

    p_two = requests.post(url+'validate/', json={'token': token, 'array': doesnt}, headers=headers)
    print(p_two.status_code)
    print(p_two.text)
    return(p_two.text)

def step_five(token, url, headers):
    p_one = requests.post(url, json={'token': token}, headers=headers)
    d = p_one.json()
    datestamp = d['datestamp']
    interval = d['interval']
    print(d)

    init_date = dateutil.parser.parse(datestamp)
    print('date: '+ str(init_date))
    print('interval: '+str(interval))
    new_date = init_date + datetime.timedelta(seconds=interval)
    print(new_date)
    new_date = str(new_date.isoformat())[:-6] + 'Z'
    print(new_date)

    p_two = requests.post(url+'validate/', json={'token': token, 'datestamp': new_date}, headers=headers)
    print(p_two.status_code)
    print(p_two.text)

if __name__ == '__main__':
    main()
