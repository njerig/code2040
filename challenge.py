# njerig
# CODE2040 Challenge

import json
import urllib
import requests


def main():
    token = 'a272e0e398eaa14ddeeaaf9cdc21d55d'
    base_url = 'http://challenge.code2040.org/api/'

    step_one(token, base_url+'register/')
    step_two(token, base_url+'reverse/')

    #step3
    #step4

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

if __name__ == '__main__':
    main()
