import requests
import random


def facts():
   r=requests.get('https://catfact.ninja/fact')
   fact=r.json()['fact']
   return fact


for i in range(10):
   fact = facts()
   print(fact)

