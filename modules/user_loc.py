#! /usr/bin/env python3

try:
    import requests
except ImportError as error:
    print(error.__class__.__name__+":"+error.message)

#callect user ip address
def get_ip_addr():
    response = requests.get('https://api64.ipify.org?format=json').json()
    return response['ip']

#collect user data
def get_location():
    ip_addr = get_ip_addr()
    response = requests.get(f'https://ipinfo.io/{ip_addr}/json/').json()
    location_data = {
        "ip":ip_addr,
        "city":response.get('city'),
        "region":response.get('region'),
        "country":response.get('country'),
        "postal" : response.get('postal'),
        "timezone" : response.get('timezone'),
        "organization" : response.get('org'),
        "location": response.get('loc')
    }
    
    return location_data

#EOF