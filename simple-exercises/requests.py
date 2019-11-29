import requests
from requests import ReadTimeout

'''
# simple commands
r = requests.get('https://xkcd.com/353/')
print(dir(r))  # see the methods that we can access
print(r.text)  # for example, here we can access the HTML of the page
print(r.status_code)  # http status
'''
'''
# getting and image and download it
image = requests.get('https://imgs.xkcd.com/comics/python.png')
print(r.content)  # get the bytes of the image

with open('image.png', 'wb') as f:  # wb = write bytes
    f.write(r.content)  # it will save the image on the same file as our python module
'''
'''
# Query strings
# Get
payload = {'page': 2, 'count': 5}
r = requests.get('https://httpbin.org/get', params=payload)
print(r.url)
print(r.text)
'''
'''
#Post
payload = {'username': 'Leo', 'password': 'testing'}
r = requests.post('https://httpbin.org/post', data=payload)
print(r.url)
r_dict = r.json()  # now we can access the response as any other dictionary
print(r_dict['form'])

# Basic authentication
# After execute the Post request above as defined the username and pwd for these requests
r = requests.get('https://httpbin.org/basic-auth/Leo/testing', auth=('Leo', 'testing'), timeout=3)
print(f'Status code: {r.status_code}\nResponse: {r.text}')
'''

# Testing timeout
try:
    r = requests.get('https://httpbin.org/delay/6', timeout=3)  # it will have a delay of 6 seconds
    print(r)
except ReadTimeout as e:
    print(f'ReadTimeout error. Details: {e}')