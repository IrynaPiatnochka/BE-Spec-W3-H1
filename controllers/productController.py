from flask import request, jsonify
from models.schemas.productSchema import product_schema, products_schema
from services import productService
from marshmallow import ValidationError
from caching import cache
from utils.util import admin_required

@admin_required
def save():
    try:
        product_data = product_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400
    
    product_saved = productService.save(product_data)
    return product_schema.jsonify(product_data), 201

def search_product():
     search_term = request.args.get("search")
     searched_items = productService.search_product(search_term)
     return products_schema.jsonify(searched_items)

@cache.cached(timeout=60)
def find_all():
    all_products = productService.find_all()
    return products_schema.jsonify(all_products), 200

def find_all_paginate():
    page = int(request.args.get("page"))
    per_page = int(request.args.get("per_page"))
    products = productService.find_all_paginate(page, per_page)
    return products_schema.jsonify(products), 200