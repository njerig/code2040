# !/usr/bin/python
# njerig
# CODE2040 Challenge

import requests
import ast


def main():
    token = 'a272e0e398eaa14ddeeaaf9cdc21d55d'
    base_url = 'http://challenge.code2040.org/api/'

    #step_one(token, base_url+'register/')
    #step_two(token, base_url+'reverse/')
    #step_three(token)
    step_four(token)

def step_one(token, url):
	data = {'token': token, 'github': 'https://github.com/njerig/code2040.git'}
	p = requests.post(url, data)
	result = p.text
	print(result)
	return result

def step_two(token, url):
    p_one = requests.post(url, {'token': token})

    the_string = p_one.text
    r_string = the_string[::-1]

    p_two = requests.post(url+'validate/', {'token': token, 'string': r_string})
    result = p_two.text
    print(result)
    return(result)

def step_three(token):
    p_one = requests.post('http://challenge.code2040.org/api/haystack', {'token': token})
    d = ast.literal_eval(p_one.text)

    needle = d['needle']
    haystack = d['haystack']
    if needle in haystack:
        index = haystack.index(needle)

    p_two = requests.post('http://challenge.code2040.org/api/haystack/validate', {'token': token, 'needle': index})
    result = p_two.text
    print(result)
    return(result)

def step_four(token):
    p_one = requests.post('http://challenge.code2040.org/api/prefix', {'token': token})
    d = ast.literal_eval(p_one.text)
    print(d)
    print('\n')
    array = d['array']
    prefix = d['prefix']
    doesnt = []
    for gibberish in array:
        if not gibberish.startswith(prefix):
            doesnt.append(gibberish)
    print(doesnt)
    print('\n')

    p_two = requests.post('http://challenge.code2040.org/api/prefix/validate', {'token': token, 'array': doesnt})
    result = p_two.text
    print(result)
    return(result)

if __name__ == '__main__':
    main()
