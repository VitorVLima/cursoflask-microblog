from app import app
import os

if __name__ == 'main':
    port = int(os.getenv('PORT'), '5000')
    app.run(host='0.0.0.0', port = port)



#comando para iniciar flask --app microblog.py run --debug
#instalar pip install flask
#instalar pip install flask-dotenv
#instalar pip install gunicorn - permite o uso do python como serviço web
#comando pip freeze > requirements.txt para criar arquivo requirements