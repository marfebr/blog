from gevent.wsgi import WSGIServer

from wfdb import create_app

app = create_app('wfdb.config.ProdConfig')

server = WSGIServer(('', 80), app)

server.serve_forever()