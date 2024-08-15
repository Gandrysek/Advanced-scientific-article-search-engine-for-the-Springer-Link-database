import requests
import pandas as pd
from flask import Flask, jsonify, request, send_file
from io import BytesIO

app = Flask(__name__)


SPRINGER_API_KEY = "4907229a03e875715d1f3b3ee17a9df5"

@app.route('/search', methods=['GET'])
def search():

    query = request.args.get('query', default='machine learning', type=str)
    export_csv = request.args.get('export_csv', default='false', type=str).lower() == 'true'


    base_url = "http://api.springernature.com/meta/v2/json"

    # Query parameters
    params = {
        'q': query,
        'api_key': SPRINGER_API_KEY
    }


    response = requests.get(base_url, params=params)


    if response.status_code == 200:
        data = response.json()
        records = data.get('records', [])

        if export_csv:

            df = pd.DataFrame.from_records(records)


            csv_output = BytesIO()
            df.to_csv(csv_output, index=False)
            csv_output.seek(0)

            # Return the CSV file
            return send_file(
                csv_output,
                mimetype='text/csv',
                download_name=f'{query}_results.csv',
                as_attachment=True
            )


        return jsonify(records)
    else:
        return jsonify({"error": "Failed to retrieve data from Springer Link API"}), response.status_code

if __name__ == '__main__':
    app.run(debug=True)
