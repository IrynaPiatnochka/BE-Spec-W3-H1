from flask import request, jsonify
from models.schemas.customerSchema import customer_schema, customers_schema
from services import customerService
from marshmallow import ValidationError
from caching import cache
from utils.util import admin_required, user_token_required


def login():
    try:
        credentials = request.json
        token = customerService.login(credentials['username'], credentials['password'])
    except KeyError:
        return jsonify({'messages': 'Invalid payload, expecting username and password'}), 401
    
    if token:
        return jsonify(token), 200
    else:
        return jsonify({'messages': "Invalid username or password"}), 401

@admin_required
def save():
    try:
        customer_data = customer_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400
    customer_saved = customerService.save(customer_data)
    return customer_schema.jsonify(customer_data), 201


@cache.cached(timeout=60)
@admin_required
def find_all():
    all_customers = customerService.find_all()
    return customers_schema.jsonify(all_customers), 200

@admin_required
def find_all_paginate():
    page = int(request.args.get("page"))
    per_page = int(request.args.get("per_page"))
    customers = customerService.find_all_paginate(page, per_page)
    return customers_schema.jsonify(customers), 200
    
@user_token_required
def update_customer(id):
    try:
        customer_data = request.json
        updated_customer = customerService.update_customer(id, customer_data)
        if updated_customer:
            return customer_schema.jsonify(updated_customer), 200
        else:
            return jsonify({"message": "Customer not found"}), 404
    except ValidationError as e:
        return jsonify(e.messages), 400
   
@user_token_required
def delete_customer(id):
    try:
        success = customerService.delete_customer(id)
        if success:
            return jsonify({"message": "Customer removed successfully"}), 200
        else:
            return jsonify({"message": "Customer not found"}), 404
    except ValidationError as e:
        return jsonify(e.messages), 400
    
    