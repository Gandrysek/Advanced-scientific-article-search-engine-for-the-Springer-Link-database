from flask import Blueprint, request, jsonify, make_response
from utils import search_springer, format_search_results
from models import db, SearchLog

search_blueprint = Blueprint('search', __name__)


@search_blueprint.route('/api/search', methods=['GET'])
def search():
    query = request.args.get('query')
    year_range = request.args.get('year_range')
    field = request.args.get('field')

    if not query:
        return jsonify({"error": "Query parameter is required"}), 400

    # Perform the search using the utility function
    raw_results = search_springer(query, year_range, field)
    formatted_results = format_search_results(raw_results)

    # Log the search query
    search_log = SearchLog(query=query)
    db.session.add(search_log)
    db.session.commit()

    return jsonify(formatted_results)


@search_blueprint.route('/api/export_csv', methods=['POST'])
def export_csv():
    data = request.json
    csv_content = "Title, Authors, Publication Date, Abstract, Open Access, PDF Link\n"

    for item in data:
        csv_content += f"{item['title']}, {item['authors']}, {item['publication_date']}, "
        csv_content += f"{item['abstract']}, {item['open_access']}, {item['pdf_link']}\n"

    response = make_response(csv_content)
    response.headers["Content-Disposition"] = "attachment; filename=search_results.csv"
    response.headers["Content-type"] = "text/csv"
    return response
