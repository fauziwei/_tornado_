# coding: utf-8
url_patterns = []
'''
format url is 'directory_{something}'
e.g: '/auth_login/'
''' 

# authentication login and logout
from auth import urls
url_patterns.extend(urls.url_patterns)

# home or index
from home import urls
url_patterns.extend(urls.url_patterns)
