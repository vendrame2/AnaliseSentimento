from flask import Flask, render_template
from app.api import api

app = Flask(__name__,
            template_folder='app/templates',  # Definir a pasta de templates
            static_folder='app/static')  # Definir a pasta de arquivos estáticos

app.register_blueprint(api, url_prefix='/api')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)