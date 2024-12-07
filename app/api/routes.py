from flask import request, current_app
import requests
from app.api import bp


@bp.route('/<path:endpoint>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def proxy(endpoint):
    target_url = f"{current_app.config['OPEN_WEBUI_URL']}/api/{endpoint}"

    method = request.method
    headers = dict(request.headers)
    headers['Authorization'] = f"Bearer {current_app.config['API_KEY']}"  # Füge den API-Key hinzu
    data = request.get_json() if request.is_json else request.form

    response = requests.request(method, target_url, headers=headers, json=data if request.is_json else None,
                                params=request.args)

    return response.content, response.status_code, response.headers.items()
