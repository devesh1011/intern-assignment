from flask import Blueprint, request, jsonify
from app.services.user_service import UserService
from bson import ObjectId

user_blueprint = Blueprint("user", __name__, url_prefix="/users")


@user_blueprint.route("/", methods=["GET"])
def get_users():
    users = UserService.get_all_users()
    return jsonify(users), 200


@user_blueprint.route("/<id>", methods=["GET"])
def get_user(id):
    user = UserService.get_user_by_id(id)
    if user:
        user["_id"] = str(user["_id"])
        return jsonify(user), 200
    return jsonify({"error": "User not found"}), 404


@user_blueprint.route("/", methods=["POST"])
def create_user():
    data = request.json
    if not data or "name" not in data or "email" not in data or "password" not in data:
        return jsonify({"error": "Input is not valid"}), 400

    user_id = UserService.create_user(data)
    return (
        jsonify({"message": "User has been created successfully", "id": str(user_id)}),
        201,
    )


@user_blueprint.route("/<id>", methods=["PUT"])
def update_user(id):
    user_data = request.json
    if not ObjectId.is_valid(id):
        return jsonify({"error": "Id is not valid"}), 400

    res = UserService.update_user(id, user_data)
    if res.matched_count:
        return jsonify({"message": "User has been updated"}), 200
    return jsonify({"error": "No User was found"}), 404


@user_blueprint.route("/<id>", methods=["DELETE"])
def delete_user(id):
    res = UserService.delete_user(id)
    if res:
        return jsonify({"message": "User deleted from database successfully"}), 200
    return jsonify({"error": "No User was found"}), 404
