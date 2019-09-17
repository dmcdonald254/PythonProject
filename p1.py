<<<<<<< HEAD
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
=======
import math
import sys
from os import rename

import requests

print(sys.version) 
print(sys.executable) 


def greet(who_to_greet):
    test = 'Test'
    greeting =  'Hello, {}'.format(who_to_greet)
    return greeting

r = requests.get("https://www.google.com")
print("Status Code: \n", r.status_code, " \n")
print("Cookies: \n", r.cookies, "\n")
print("Time elapsed: \n", r.elapsed, "\n\n")
>>>>>>> a0e11bbcbe3ae67e33e9a918e6004720742e08fd
