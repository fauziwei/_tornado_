# coding: utf-8
import json
import logging
from tornado import gen, web
from base.handlers import BaseHandler

from lib.decorator import authentication

l = logging.getLogger(__name__)


class IndexHandler(BaseHandler):

	@gen.coroutine
	@authentication
	def get(self, *args, **kwargs):
		# status_code, email = self.authentication()
		# if status_code != 200:
		# 	self.write( json.dumps({ 'success': False }))
		# 	return

		email = self.email

		message = yield self.func(email)

		self.write( json.dumps({
			'success': True,
			'message': message
		}) )
		self.finish()


	@gen.coroutine
	def func(self, email):
		s = 'hello: %s' % email
		raise gen.Return(s)



class LongPoolHandler(BaseHandler):
	'''
	IF Using:

	 @web.asynchronous

	must manually call  *self.finish()*
	otherwise connection always open

	'''
	@web.asynchronous
	@gen.engine
	@authentication
	def get(self, *args, **kwargs):

		message = yield gen.Task(self.longPool, 'hello')

		self.write( json.dumps({
			'success': True,
			'message': message
		}))
		self.finish()


	def longPool(self, say, callback):
		'''Async require *callback*.'''
		s = say*10
		return callback(s)
