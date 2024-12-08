from flask import request, current_app
import requests
from app.api import bp


def forward_request(endpoint, debug_shorten_response=False):
    target_url = f"{current_app.config['OPEN_WEBUI_URL']}/api/{endpoint}"
    method = request.method
    headers = dict(request.headers)
    headers['Authorization'] = f"Bearer {current_app.config['API_KEY']}"  # Füge den API-Key hinzu
    data = request.get_json() if request.is_json else request.form

    current_app.logger.debug(f"Request data: {data}")

    response = requests.request(
        method=method,
        url=target_url,
        headers=headers,
        json=data if request.is_json else None,
        params=request.args
    )

    current_app.logger.debug(f"Response status: {response.status_code}")
    current_app.logger.debug(
        f"Response content: {response.content[:100] if debug_shorten_response else response.content}"
    )

    return response.content, response.status_code, response.headers.items()


@bp.route('/<path:endpoint>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def default(endpoint):
    return forward_request(endpoint)


@bp.route('/embeddings', methods=['GET', 'POST', 'PUT', 'DELETE'])
def embeddings():
    return forward_request('embeddings', debug_shorten_response=True)
