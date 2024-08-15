import requests
from flask import Flask, jsonify, request

app = Flask(__name__)

# Springer Link API credentials
SPRINGER_API_KEY = "4907229a03e875715d1f3b3ee17a9df5"

@app.route('/test-springer-query')
def test_springer_query():

    base_url = "http://api.springernature.com/meta/v2/json"

    # Testing queries
    params = {
        'q': 'machine learning',
        'api_key': SPRINGER_API_KEY
    }


    response = requests.get(base_url, params=params)


    if response.status_code == 200:
        data = response.json()
        return jsonify(data['records'][:5])
    else:
        return jsonify({"error": "Failed to retrieve data from Springer Link API"}), response.status_code

if __name__ == '__main__':
    app.run(debug=True)
