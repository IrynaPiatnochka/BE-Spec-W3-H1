from database import db
from models.customer import Customer
from sqlalchemy import select, delete
from utils.util import encode_token


def login(username, password): 
    query =select(Customer).where(Customer.username == username) 
    customer = db.session.execute(query).scalar_one_or_none() 

    if customer and customer.password == password: 
        auth_token = encode_token(customer.id, customer.role_id)

        response = {
            "status": "success",
            "message": "Successfully Logged In",
            "auth_token": auth_token
        }
        return response


def save(customer_data):
    new_customer = Customer(name=customer_data['name'], email=customer_data['email'], phone=customer_data['phone'], username=customer_data['username'], password=customer_data['password'], role_id=customer_data["role_id"])
    db.session.add(new_customer)
    db.session.commit()
    db.session.refresh(new_customer)
    return new_customer

def find_all():
    query = select(Customer)
    all_customers = db.session.execute(query).scalars().all()
    return all_customers

def find_all_paginate(page, per_page):
    query = select(Customer)
    customers = db.paginate(query, page=page, per_page=per_page)
    return customers


def update_customer(id, customer_data):
    customer = db.session.query(Customer).filter(Customer.id == id).first()
    if customer:
        for key, value in customer_data.items():
            setattr(customer, key, value)
        db.session.commit()
        db.session.refresh(customer)
        return customer
    else:
        return None

def delete_customer(id):
    query = delete(Customer).filter(Customer.id == id)
    db.session.execute(query)
    db.session.commit()
    return {'message': 'Customer deleted successfully'}, 200
    
    

