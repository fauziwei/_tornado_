# coding: utf-8
from tornado.web import url
from .handlers import LoginHandler, LogoutHandler

'''
format url is 'directory_{something}'
e.g: '/auth_login/'
''' 

url_patterns = [
	url(r'/auth_login/', LoginHandler, name='login'),
	url(r'/auth_logout/', LogoutHandler, name='logout')
]