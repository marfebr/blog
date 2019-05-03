#gunicorn -w 4 -b 127.0.0.1:4000  wsgi:app
from wfdb import create_app

#app = create_app('edocka.config.DevConfig')
app = create_app('wfdb.config.ProdConfig')

if __name__ == "__main__":
    app.run()
