from app.api.v1 import api_bp


@api_bp.route("/users")
def get_users():
    return {"message": "Users endpoint"}