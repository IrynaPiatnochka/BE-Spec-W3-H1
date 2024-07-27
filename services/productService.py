from database import db
from models.product import Product
from sqlalchemy import select

def save(product_data):
    
    new_product = Product(name=product_data['name'], price=product_data['price'])
    
    db.session.add(new_product)
    db.session.commit()
    
    db.session.refresh(new_product)
    return new_product

def search_product(search_term):
    query = select(Product).where(Product.name.like(f'%{search_term}%'))
    search_products = db.session.execute(query).scalars().all()
    return search_products

def find_all():
    query = select(Product)
    all_products = db.session.execute(query).scalars().all()
    return all_products

def find_all_paginate(page, per_page):
    query = select(Product)
    products = db.paginate(query, page=page, per_page=per_page)
    return products