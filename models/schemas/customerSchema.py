from . import ma
from marshmallow import fields

class CustomerSchema(ma.Schema):
    id = fields.Integer(required=False)
    name = fields.String(required=False)
    email = fields.Email(required=False)
    phone = fields.String(required=False)
    username = fields.String(required=False)
    password = fields.String(required=False)
    role_id = fields.Integer(required=True)
    
    
    class Meta:
        fields = ("id", "name", "email", "phone", "username", "password", "role_id")
        
        
customer_schema = CustomerSchema()
customers_schema = CustomerSchema(many=True, exclude=["password"])


class CustomerOrderSchema(ma.Schema):
    id = fields.Integer(required=False) 
    name = fields.String(required=True)
    email = fields.Email(required=True)
    phone = fields.String(required=True)
    username = fields.String(required=True)
    password = fields.String(required=True)
    orders = fields.Nested("OrderSchema", many=True)

    class Meta: 
        fields = ("id", "name", "email", "phone", "username", "password")

