from flask import Flask, jsonify
from config import Config


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)


    from app.api import bp as api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    @app.route('/<path:any_other_path>', methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH'])
    def block_other_paths(any_other_path):
        """
        Blocksing access to any other path than the ones defined in the API.
        """
        return jsonify({"error": "Access to this endpoint is not allowed"}), 403

    return app
