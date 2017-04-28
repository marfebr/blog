from tornado.wsgi import WSGIContainer

from tornado.httpserver import HTTPServer

from tornado.ioloop import IOLoop

from wfdb import create_app

app = WSGIContainer(create_app("wfdb.config.ProdConfig"))

http_server = HTTPServer(app)

http_server.listen(80)

IOLoop.instance().start()