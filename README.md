# blog

##Instalar as dependencias

``bash
pip install -r requirements.txt
``

##executar aplicação como serviço

``bash
gunicorn -w 4 -b 0.0.0.0:5000  wsgi:app
``


basta acessa a aplicação na porta 5000
