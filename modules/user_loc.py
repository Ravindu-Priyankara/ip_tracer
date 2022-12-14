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
    response = requests.get(f'https://ipapi.co/{ip_addr}/json/').json()
    location_data = {
        "ip":ip_addr,
        "city":response.get('city'),
        "region":response.get('region'),
        "region_code" : response.get('region_code'),
        "country_code" : response.get('country_code'),
        "country_code_iso3" : response.get('country_code_iso3'),
        "country_name" : response.get('country_name'),
        "country_capital" : response.get('country_capital'),
        "country_tld" : response.get('country_tld'),
        "continent_code" : response.get('continent_code'),
        "in_eu" : response.get('in_eu'),
        "postal" : response.get('postal'),
        "latitude" : response.get('latitude'),
        "longitude" : response.get('longitude'),
        "timezone" : response.get('timezone'),
        "utc_offset" : response.get('utc_offset'),
        "country_calling_code" : response.get('country_calling_code'),
        "currency" : response.get('currency'),
        "currency_name" : response.get('currency_name'),
        "languages" : response.get('languages'),
        "asn" : response.get('asn'),
        "org" : response.get('org')
    }
    
    return location_data

#EOF