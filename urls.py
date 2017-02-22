# coding: utf-8
from tornado.web import url

from auth.handlers import LoginHandler, LogoutHandler
from index.handlers import IndexHandler, LongPoolHandler

url_patterns = [
	url(r'/', IndexHandler, name='index'),
	url(r'/login/', LoginHandler, name='login'),
	url(r'/logout/', LogoutHandler, name='logout'),
	url(r'/longpool/', LongPoolHandler, name='longpool')
]
