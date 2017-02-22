# coding: utf-8
import json
import uuid
import base64
import hashlib
import logging
import traceback
from tornado import web

l = logging.getLogger(__name__)

class BaseHandler(web.RequestHandler):

	def __init__(self, *args, **kwargs):
		super(BaseHandler, self).__init__(*args, **kwargs)

	@property
	def cache(self):
		return self.application.cache

	@property
	def user_session(self):
		return self.application.user_session

	@property
	def models(self):
		return self.application.models

	def commit(self, session):
		try:
			session.flush()
			session.commit()
		except:
			traceback.print_exc()
			session.rollback()
		finally:
			session.close()


	# def statusCode(self):
	# 	'''STATUS CODE.'''
	# 	return {
	# 		200: 'OK',
	# 		400: 'Bad Request',
	# 		404: 'Not Found',
	# 		405: 'Method Not Allowed',
	# 		500: 'Internal Server Error'
	# 	}


	# def authorization(self):
	# 	'''Only for login PAGE.'''

	# 	auth_header = self.request.headers.get('Authorization', None)

	# 	if auth_header is None or not auth_header.startswith('Basic '):
	# 		status_code = 400 # Bad Request
	# 		return status_code, None
	# 	auth_decoded = base64.decodestring(auth_header[6:])
	# 	email, password = auth_decoded.split(':', 2)

	# 	session = self.models.Db().Session()

	# 	secure_password = hashlib.sha1(password).hexdigest()
	# 	user = session.query(self.models.User).filter_by(email=email, password=secure_password).first()
	# 	if not user:
	# 		self.commit(session)
	# 		status_code = 404 # Not Found
	# 		return status_code, None

	# 	self.commit(session)

	# 	# Create auth token
	# 	token = '%s-%s' % (hashlib.sha1(email).hexdigest(), uuid.uuid4())
	# 	self.token_user[token] = email

	# 	status_code = 200 # OK
	# 	return status_code, token


	# # for not login-page
	# def authentication(self):
	# 	# front-end should send token for next pages authentication.
	# 	try:
	# 		auth_header = self.request.headers.get('Authorization', None)
	# 		if auth_header is None:
	# 			status_code = 400 # Bad Request
	# 			return status_code, None

	# 		if auth_header not in self.token_user:
	# 			status_code = 404 # Not Found, user should goto login page
	# 			return status_code, None

	# 		# Login token is authenticated.
	# 		email = self.token_user[auth_header]

	# 		status_code = 200 # OK
	# 		return status_code, email

	# 	except:
	# 		status_code = 400 # Bad Request
	# 		return status_code, None
