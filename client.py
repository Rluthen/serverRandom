import requests
import pseudorandom

pload = {'number':'"'+str(pseudorandom.pseudorand())+'"'}
r = requests.post('http://localhost:8080',data = pload)
# r = requests.post('http://localhost:8080')

print(r.text)