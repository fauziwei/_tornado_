# coding: utf-8
# fauziwei@yahoo.com

import uuid
import json
import base64
import hashlib
import logging

l = logging.getLogger(__name__)


def authorization(f):
	'''Only for login PAGE.'''

	def _wrapper(self, *args, **kwargs):

		token = None

		auth_header = self.request.headers.get('Authorization', None)

		if auth_header is None or not auth_header.startswith('Basic '):
			# status_code = 400 # Bad Request
			# return status_code, None
			self.write( json.dumps({ 'token': token }) )
			self.finish()
			return

		auth_decoded = base64.decodestring(auth_header[6:])
		email, password = auth_decoded.split(':', 2)

		session = self.models.Db().Session()

		secure_password = hashlib.sha1(password).hexdigest()
		user = session.query(self.models.User).filter_by(email=email, password=secure_password).first()
		if not user:
			self.commit(session)
			# status_code = 404 # Not Found
			# return status_code, None
			self.write( json.dumps({ 'token': token }) )
			self.finish()
			return


		self.commit(session)

		# Create auth token
		token = '%s-%s' % (hashlib.sha1(email).hexdigest(), uuid.uuid4())
		# self.token_user[token] = email
		self.user_session.save(token, email)

		self.user_session.expire(token, 604800) # 1 week

		# status_code = 200 # OK
		# return status_code, token
		self.write( json.dumps({ 'token': token }) )
		self.finish()

		return f(self, *args, **kwargs)

	return _wrapper



def authentication(f):
	'''Other than login page which is authentication is required.'''

	def _wrapper(self, *args, **kwargs):

		try:
			auth_header = self.request.headers.get('Authorization', None)

			if auth_header is None:
				# status_code = 400 # Bad Request
				# return status_code, None
				self.write( json.dumps({ 'success': False }) )
				self.finish()
				return

			if not self.user_session.exists(auth_header):
				# status_code = 404 # Not Found, user should goto login page
				# return status_code, None
				self.write( json.dumps({ 'success': False }) )
				self.finish()
				return

			# Login token is authenticated.
			email = self.user_session.get(auth_header)

			self.user_session_id = auth_header
			self.email = email

			# status_code = 200 # OK
			# return status_code, email

		except:
			self.write( json.dumps({ 'success': False }) )
			self.finish()

		return f(self, *args, **kwargs)

	return _wrapper



# def login_required(f):   
# 	def _wrapper(self, *args, **kwargs):   
# 		print self.get_current_user()   
# 		logged = self.get_current_user()   
# 		if logged == None:   
# 			self.write('no login')   
# 			self.finish()   
# 		else:   
# 			ret = f(self,*args, **kwargs)   
# 	return _wrapper
