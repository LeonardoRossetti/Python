import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('Site is not available at the moment.')
else:
    print('Site is up and running!')
    print(site.read())
