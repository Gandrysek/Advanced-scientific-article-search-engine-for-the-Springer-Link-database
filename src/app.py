
import os
from dotenv import load_dotenv
from blueprints.searchBlueprints import search_blueprint
from blueprints.exportBlueprints import export_blueprint
from flask import Flask

# set the current working directory to the app.py for the relative path usage
os.chdir(os.path.dirname(__file__))
load_dotenv('../.env')

app = Flask(__name__)


if "SPRINGER_API_KEY" in os.environ:
    app.register_blueprint(search_blueprint, url_prefix='/api')
    app.register_blueprint(export_blueprint, url_prefix='/api')
else:
    raise Exception("No api key found. Provide one with SPRINGER_API_KEY key in .env at the top of the project")

if __name__ == '__main__':
    app.run(debug=True)
