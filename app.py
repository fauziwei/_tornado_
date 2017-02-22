# coding: utf-8
from tornado import web, gen, ioloop, httpserver
from urls import url_patterns
from settings import settings
import lib.cache as cache
import lib.models as models

# cd C:"\Previous Work\tornado-new-way-like-django"

class Application(web.Application):

	cache = cache
	user_session = cache.Cache(host='localhost', port=6379, db=0)

	models = models

	def __init__(self):
		super(Application, self).__init__(url_patterns, **settings)


def main():
	app = Application()
	server = httpserver.HTTPServer(app)
	server.listen(8888, address='127.0.0.1')
	ioloop.IOLoop.instance().start()

if __name__ == '__main__':
	main()
