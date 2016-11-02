# !/usr/bin/python
# njerig
# CODE2040 Challenge

import requests
import ast
import json


def main():
    token = 'a272e0e398eaa14ddeeaaf9cdc21d55d'
    base_url = 'http://challenge.code2040.org/api/'

    #step_one(token, base_url+'register/')
    #step_two(token, base_url+'reverse/')
    #step_three(token, base_url+'haystack/')
    step_four(token, base_url+'prefix/')
    #step_five(token)

def step_one(token, url):
	p = requests.post(url, data={'token': token, 'github': 'https://github.com/njerig/code2040.git'})
	result = p.text
	print(result)
	return result

def step_two(token, url):
    p_one = requests.post(url, data={'token': token})

    the_string = p_one.text
    r_string = the_string[::-1]

    p_two = requests.post(url+'validate/', data={'token': token, 'string': r_string})
    result = p_two.text
    print(result)
    return(result)

def step_three(token, url):
    p_one = requests.post(url, data={'token': token})
    d = ast.literal_eval(p_one.text)

    needle = d['needle']
    haystack = d['haystack']
    if needle in haystack:
        index = haystack.index(needle)

    p_two = requests.post(url+'validate/', data={'token': token, 'needle': index})
    result = p_two.text
    print(result)
    return(result)

def step_four(token, url):
    p_one = requests.post(url, {'token': token})
    '''
    print(p_one.text)
    print('\n')
    '''
    d = p_one.json()
    '''
    print(d)
    print('\n')
    '''

    array = d['array']
    prefix = d['prefix']
    doesnt = []
    for gibberish in array:
        if not gibberish.startswith(prefix):
            doesnt.append(gibberish)
    '''
    print(doesnt)
    print('\n')
    '''

    p_two = requests.post(url+'validate/', data=json.dumps({'token': token, 'array': doesnt}))
    result = p_two.text
    print(p_two.status_code)
    print(result)
    return(result)

def step_five(token):
    p_one = requests.post('http://challenge.code2040.org/api/dating', {'token': token})
    d = ast.literal_eval(p_one.text)
    print(d)

if __name__ == '__main__':
    main()
