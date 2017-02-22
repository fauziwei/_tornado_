# coding: utf-8
import json
import logging
from tornado import gen
from base.handlers import BaseHandler

from lib.decorator import authorization, authentication

l = logging.getLogger(__name__)


class LoginHandler(BaseHandler):

	@gen.coroutine
	@authorization
	def post(self, *args, **kwargs):
		pass

		# status_code, token = self.authorization()

		# self.write( json.dumps({
			# 'token': token
		# }))


class LogoutHandler(BaseHandler):

	@gen.coroutine
	@authentication
	def get(self, *args, **kwargs):

		self.user_session.delete(self.user_session_id)
		self.write( json.dumps({ 'success': True }) )
