from flask import Flask

from general.general import general_bp
from products.products import products_bp
from API.api import api_bp

app = Flask(__name__)

app.register_blueprint(general_bp)
app.register_blueprint(products_bp)
app.register_blueprint(api_bp)
app.config['STATIC_FOLDER'] = 'static'

if __name__ == '__main__':
    app.run(debug=True, port=8001)