# coding: utf-8
import time
import json
import requests
import requests.exceptions

token = None

try:
	# 1st goto login page
	# todo authorization.
	url = 'http://localhost:8888/login/'
	# r1 = requests.post(url, auth=('f', 'f'))
	r1 = requests.post(url, auth=('admin', 'admin'))

	if r1.status_code == 200:
		print 'OK'

		# if success, then goto index page
		# only use token for authentication.
		token = r1.json()['token']

		print 'token: %s' % token

		if token:

			# 2nd sending.
			url = 'http://localhost:8888/'
			try:
				payload = {'message': 'give me data'}
				r2 = requests.get(
					url,
					headers={'Authorization': token},
					json=payload
				)
				if r2.status_code == 200:
					if r2.json()['success']:
						print 'replied server: %s' % r2.json()['message']

			except requests.exceptions.RequestException:
				pass

		else:
			print 'Unauthorized!'


	elif r1.status_code == 400:
		print 'Bad Request'

	elif r1.status_code == 404:
		print 'Not Found'

	elif r1.status_code == 405:
		print 'Method Not Allowed'

	elif r1.status_code == 500:
		print 'Internal Server Error'

except requests.exceptions.RequestException:
	pass


# time.sleep(4)


# 3rd sending. with same token
if token is not None:
	url = 'http://localhost:8888/'
	try:
		r3 = requests.get(
			url,
			headers={'Authorization': token},
		)
		if r3.status_code == 200:
			if r3.json()['success']:
				print 'replied server: %s' % r3.json()['message']
			else:
				print 'Unauthorized'

	except requests.exceptions.RequestException:
		pass



# 4th longpool
if token is not None:
	url = 'http://localhost:8888/longpool/'
	try:
		r4 = requests.get(
			url,
			headers={'Authorization': token},
		)
		if r4.status_code == 200:
			if r4.json()['success']:
				print 'replied server: %s' % r4.json()['message']
			else:
				print 'Unauthorized'

	except requests.exceptions.RequestException:
		pass



# 5th sending, logout
if token is not None:
	url = 'http://localhost:8888/logout/'
	try:
		r5 = requests.get(
			url,
			headers={'Authorization': token},
		)
		if r5.status_code == 200:
			if r5.json()['success']:
				print 'OK Logout'

	except requests.exceptions.RequestException:
		pass




# 6th sending.
if token is not None:
	url = 'http://localhost:8888/'
	try:
		r6 = requests.get(
			url,
			headers={'Authorization': token},
		)
		if r6.status_code == 200:
			if r6.json()['success']:
				print 'replied server: %s' % r6.json()['message']
			else:
				print 'Unauthorized'

	except requests.exceptions.RequestException:
		pass
