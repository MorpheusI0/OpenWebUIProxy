from flask import current_app, request, Response,stream_with_context
import requests
from app.api import bp


def forward_request(endpoint, debug_shorten_response=False):
    target_url = f"{current_app.config['OPEN_WEBUI_URL']}/api/{endpoint}"
    method = request.method
    headers = {**dict(request.headers), 'Authorization': f"Bearer {current_app.config['API_KEY']}"}
    data = request.get_json() if request.is_json else request.form

    current_app.logger.debug(f"Request data: {data}")

    response = requests.request(
        method=method,
        url=target_url,
        headers=headers,
        json=data if request.is_json else None,
        params=request.args
    )

    response_content = response.content[:100] if debug_shorten_response else response.content
    current_app.logger.debug(f"Response status: {response.status_code}")
    current_app.logger.debug(f"Response content: {response_content}")

    return response.content, response.status_code, response.headers.items()


@bp.route('/<path:endpoint>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def default(endpoint):
    return forward_request(endpoint)


@bp.route('/chat', methods=['POST'])
def chat():
    target_url = f"{current_app.config['OPEN_WEBUI_URL']}/api/chat"
    headers = {**dict(request.headers), 'Authorization': f"Bearer {current_app.config['API_KEY']}"}

    current_app.logger.debug(f"Request data: {request.data}")

    with requests.post(
            target_url,
            headers=headers,
            data=request.get_data(),
            stream=True
    ) as response:
        current_app.logger.debug(f"Response status: {response.status_code}")
        current_app.logger.debug(f"Response content: {response.content}")

        return Response(
            stream_with_context(response.iter_content(chunk_size=1024)),
            status=response.status_code,
            headers=dict(response.headers),
        )


@bp.route('/embeddings', methods=['GET', 'POST', 'PUT', 'DELETE'])
def embeddings():
    return forward_request('embeddings', debug_shorten_response=True)
