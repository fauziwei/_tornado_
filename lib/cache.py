# coding: utf-8
# fauziwei@yahoo.com

import redis
import redis.exceptions

class Cache:

	'''Redis for caching.

	This class is not only for session, but can do for other
	work which is connected to redis.

	'''
	def __init__(self, host='localhost', port=6379, db=0):


		# Backward compatibily support.
		# self.rds = redis.Redis(host=host, port=port, db=db)

		# Doesnt care backward compatibility.
		self.rds = redis.StrictRedis(host=host, port=port, db=db)


	def expire(self, key, ttl):
		'''set the expire key.

		ttl in second.
		1 day = 86400
		1 week = 604800

		'''
		self.rds.expire(key, ttl)


	def save(self, key, value):
		'''Saving to redis.

		original redis, has own method 'save()':
		e.g:
				r['test'] = 'OK'
				r.save()   <<< return True

		'''
		self.rds.set(key, value)


	def get(self, key):
		'''Get value based on key.'''
		return self.rds.get(key)


	def delete(self, key):
		'''Delete key/value from from redis.'''
		try:
			self.rds.delete(key)
		except redis.exceptions.ResponseError:
			pass


	def deleteKeysByIter(self, keys):
		'''keys pattern could be 'prefix:*'
		e.g:
				r.scan_iter('prefix:*')
		'''
		for key in self.rds.scan_iter(keys):
			self.delete(key)


	def keys(self, key=None):
		'''
		option1 = Get all keys().
		option2 = with input key.

		key pattern could be, 'name*'
		e.g:
				r.set('name1', 'a')
				r.set('name2', 'b')
				r.set('name3', 'c')

				print r.keys('name*')

		'''
		if key is None:
			# Get all keys
			return self.rds.keys()

		else:
			return self.rds.keys(key)


	def exists(self, key):
		'''Check existing key.

		return True/False

		'''
		return self.rds.exists(key)


	def incr(self, key):
		'''increasing value.

		e.g: r.set('age', 5)
				r.incr('age')
				print r.get('age')
		'''
		self.rds.incr(key)


	def decr(self, key):
		'''decreasing value.
		e.g: r.set('age', 5)
				r.decr('age')
				print r.get('age')
		'''
		self.rds.decr(key)


	def size(self):
		'''Get the size of current redis database.'''
		return self.rds.dbsize()


	def flushdb(self):
		''' flush current connection redis database.'''
		self.rds.flushdb()
