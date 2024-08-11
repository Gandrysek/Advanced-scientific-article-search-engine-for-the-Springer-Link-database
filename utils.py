import requests
from config import Config

def search_springer(query, year_range=None, field=None):
    base_url = "https://api.springernature.com/meta/v2/json"
    params = {
        "q": query,
        "p": 50,  # results per page
        "s": 1,   # start index
        "api_key": Config.SPRINGER_API_KEY,
    }
    if year_range:
        params["date-facet-mode"] = "between"
        params["date-facet"] = year_range
    if field:
        params["field"] = field

    response = requests.get(base_url, params=params)
    response.raise_for_status()
    return response.json()

def format_search_results(data):
    results = []
    for item in data.get('records', []):
        result = {
            "title": item.get('title'),
            "authors": item.get('creators'),
            "publication_date": item.get('publicationDate'),
            "abstract": item.get('abstract'),
            "open_access": item.get('openAccess'),
            "pdf_link": item.get('url')[0]['value'] if 'url' in item else None
        }
        results.append(result)
    return results
