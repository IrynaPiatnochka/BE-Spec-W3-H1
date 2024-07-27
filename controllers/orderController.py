from flask import request, jsonify
from models.schemas.orderSchema import order_schema, orders_schema
from services import orderService
from marshmallow import ValidationError
from caching import cache
from utils.util import user_token_required, admin_required

@user_token_required
def save():
    try:
        order_data = order_schema.load(request.json)
        print(order_data)

    except ValidationError as e:
        return jsonify(e.messages), 400
    
    new_order = orderService.save(order_data)
    return order_schema.jsonify(new_order), 201

@cache.cached(timeout=60)
@admin_required
def find_all():
    all_orders = orderService.find_all()
    return orders_schema.jsonify(all_orders), 200

@admin_required
def find_all_paginate():
    page = int(request.args.get("page"))
    per_page = int(request.args.get("per_page"))
    orders = orderService.find_all_paginate(page, per_page)
    return orders_schema.jsonify(orders), 200

@user_token_required
def find_by_id(id):
    orders = orderService.find_by_id(id)
    return orders_schema.jsonify(orders), 200

@user_token_required
def find_by_customer_id(id, token_id):
    if id == token_id:
        orders = orderService.find_by_customer_id(id)
    else:
        return jsonify({"messages": "You do not have access"}), 401
    return orders_schema.jsonify(orders), 200

@user_token_required
def find_by_customer_email():
    email = request.json['email']
    orders = orderService.find_by_customer_email(email)
    return orders_schema.jsonify(orders), 200