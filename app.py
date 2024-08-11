from flask import Flask
from routes import search_blueprint
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Register the blueprint for the routes
app.register_blueprint(search_blueprint)

if __name__ == '__main__':
    app.run(debug=True)
