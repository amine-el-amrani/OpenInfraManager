from flask import Blueprint, request, jsonify


server_bp = Blueprint("/servers", __name__)

images_bp = Blueprint("/images", __name__)


@server_bp.route("/servers", methods=["POST"])
def create_server():
    # Get payload informations in json format
    payload = request.get_json()

    required_fields = ["name", "image_id", "flavor_id", "network_id"]
    missing_fields = [field for field in required_fields if field not in payload]

    if missing_fields :
        return jsonify({
            "error": "Invalid payload",
            "details": {"missing_fields": missing_fields}
        }), 404
    
    return jsonify({
        "server_id": "fake_server_id",
        "status": "created",
        "details": payload
    }), 201

@server_bp.route("servers", methods=["GET"])
def list_servers():
    return jsonify({
        "status": "success",
        "servers": [
            {"id": "srv-1", "name": "Web Server"},
            {"id": "srv-2", "name": "Database Server"}
        ]
    }), 200

@server_bp.route("servers/<server_id>", methods = ["GET"])
def get_server():


@images_bp.route("/images", methods=["GET"])
def list_images():
    return jsonify({
        "status": "success",
        "images": [
            {"id": "img-1", "name": "Ubuntu 20.04"},
            {"id": "img-2", "name": "CentOS 8"}
        ]
    }), 200