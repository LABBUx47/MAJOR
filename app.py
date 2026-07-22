from datetime import datetime, timezone

from flask import Flask, jsonify, request

app = Flask(__name__)

services = [
    {"id": 1, "name": "Wash & Fold", "price": 15.0, "duration_hours": 24},
    {"id": 2, "name": "Dry Cleaning", "price": 20.0, "duration_hours": 48},
    {"id": 3, "name": "Ironing", "price": 10.0, "duration_hours": 12},
]

orders = []
next_order_id = 1


def _serialize_order(order):
    return {
        "id": order["id"],
        "customer_name": order["customer_name"],
        "service_id": order["service_id"],
        "service_name": order["service_name"],
        "items": order["items"],
        "status": order["status"],
        "created_at": order["created_at"],
    }


@app.get("/health")
def health():
    return jsonify({"status": "ok"}), 200


@app.get("/services")
def get_services():
    return jsonify(services), 200


@app.post("/orders")
def create_order():
    payload = request.get_json(silent=True) or {}

    customer_name = (payload.get("customer_name") or "").strip()
    service_id = payload.get("service_id")
    items = payload.get("items")

    if not customer_name:
        return jsonify({"error": "customer_name is required"}), 400

    if not isinstance(service_id, int):
        return jsonify({"error": "service_id must be an integer"}), 400

    if not isinstance(items, int) or items < 1:
        return jsonify({"error": "items must be a positive integer"}), 400

    service = next((item for item in services if item["id"] == service_id), None)
    if not service:
        return jsonify({"error": "service not found"}), 404

    order = {
        "id": next_order_id,
        "customer_name": customer_name,
        "service_id": service_id,
        "service_name": service["name"],
        "items": items,
        "status": "received",
        "created_at": datetime.now(timezone.utc).isoformat(),
    }

    orders.append(order)
    next_order_id += 1

    return jsonify(_serialize_order(order)), 201


@app.get("/orders")
def list_orders():
    return jsonify([_serialize_order(order) for order in orders]), 200


@app.get("/orders/<int:order_id>")
def get_order(order_id):
    order = next((item for item in orders if item["id"] == order_id), None)
    if not order:
        return jsonify({"error": "order not found"}), 404

    return jsonify(_serialize_order(order)), 200


@app.put("/orders/<int:order_id>")
def update_order(order_id):
    order = next((item for item in orders if item["id"] == order_id), None)
    if not order:
        return jsonify({"error": "order not found"}), 404

    payload = request.get_json(silent=True) or {}
    status = (payload.get("status") or "").strip().lower()

    allowed_statuses = {"received", "processing", "ready", "completed", "cancelled"}
    if status not in allowed_statuses:
        return jsonify({"error": "invalid status"}), 400

    order["status"] = status
    return jsonify(_serialize_order(order)), 200


if __name__ == "__main__":
    app.run(debug=True)