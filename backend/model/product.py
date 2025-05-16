
from marshmallow import Schema, fields


class ProductSchemaAddproduct(Schema):
      name = fields.Email(required=True,error_messages={"required": "Email is required"})
      link = fields.String(required=True)
      category_id = fields.Number(required=True)
      thumbail_image = fields.String(required=True)
      full_image = fields.String(required=True)

class ProductSchemaUpdateproduct(Schema):
      email = fields.Email(required=False,error_messages={"required": "Email is required"})
      first_name = fields.String(required=False)
      last_name = fields.String(required=False)
      password = fields.String(required=False)
      is_active = fields.Boolean(required=False)


class ProductSchemaDeleteproduct(Schema):
      product_id = fields.Number(required=True,error_messages={"required": "product id is required"})
      
class ProductModel():
      def __init__(self,name,link,thumbail_image, full_image,short_description,full_description,qty,price):
         self.name=name
         self.link=link
         self.thumbail_image=thumbail_image
         self.full_image=full_image
         self.short_description=short_description
         self.full_description=full_description
         self.qty=qty
         self.price=price

ProductSchemaAddproduct=ProductSchemaAddproduct()
ProductSchemaUpdateproduct=ProductSchemaUpdateproduct()
ProductSchemaDeleteproduct=ProductSchemaDeleteproduct()