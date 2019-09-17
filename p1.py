import math
import sys
from os import rename

import requests

print(sys.version) 
print(sys.executable) 


def greet(who_to_greet):
    test = 'Test'
    greeting =  'Hello, {}'.format(who_to_greet)
    return test

r = requests.get("https://www.google.com")
print("Status Code: \n", r.status_code, " \n")
print("Cookies: \n", r.cookies, "\n")
print("Time elapsed: \n", r.elapsed, "\n")