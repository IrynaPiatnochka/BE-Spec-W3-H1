from . import ma
from marshmallow import fields, validate

class ProductSchema(ma.Schema):
    id = fields.Integer(required=False)
    name = fields.String(required=False)
    price = fields.String(required=False)
    
    class Meta:
        fields = ("id", "name", "price")
        
        
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)
