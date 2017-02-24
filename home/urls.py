# coding: utf-8
from tornado.web import url
from .handlers import IndexHandler, LongPoolHandler

'''
format url is 'directory_{something}'
e.g: '/home_longpool/'
''' 

url_patterns = [
	url(r'/', IndexHandler, name='index'),
	url(r'/home_longpool/', LongPoolHandler, name='longpool')
]
